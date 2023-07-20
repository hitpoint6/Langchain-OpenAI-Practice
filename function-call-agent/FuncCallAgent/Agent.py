from typing import Optional
import openai
import json
import ast
import inspect

# AI agent built on openai's function call API
# It has the following features:
# - Intelligently choose a function to improve answer for an given question.
# - Generate a description of a function given its source code.
class Agent:
    def __init__(self, functions: Optional[list], model: str = "gpt-4"):
        self.model = model
        self.messages = []
        self.functions = functions
        self.create_functional_map_(functions)

    def create_functional_map_(self, functions: list) -> dict:
        self.function_maps = {}
        for function in functions:
            self.function_maps[function.__name__] = function
        return self.function_maps

    def create_function_descriptions_(self, functions: list) -> list[dict]:
        return [self.create_function_description_(function) for function in functions]

    def create_function_description_(self, function: str) -> dict:
        function_str = inspect.getsource(function)
        prompt = f"""
        Role: 
        You are an assitant to describe a function. You goal is to generate a description of a function. 
        
        Requirement:
        You must map the python types to openai function api types as follows:
        float -> number
        int -> integer
        str -> string

        Example:
        User: def multiply(a: int, b: int) -> int:
            return a * b
        Assistant:{{
            "name": "multiply",
            "description": "Multiplies two integers",
            "parameters": {{
                "type": "object",
                "properties": {{
                "a": {{
                    "type": "integer",
                    "description": "An integer to be multiplied"
                }},
                "b": {{
                    "type": "integer",
                    "description": "Another integer to be multiplied"
                }}
                }},
                "required": ["a", "b"]
            }}
        }}
        User:def circumference_calculator(radius: float, something: float = 4.4) -> float:
            return 2 * 3.14 * radius
        Assistant: {{
            "name": "circumference_calculator",
            "description": "Calculates the circumference of a circle given the radius",
            "parameters": {{
                "type": "object",
                "properties": {{
                    "radius": {{
                        "type": "number",
                        "description": "The radius of the circle"
                    }},
                    "something": {{
                        "type": "number",
                        "description": "An optional parameter with default value 4.4"
                    }}
                }},
                "required": ["radius"]
            }}
        }}

        User: {function_str}
        Assistant:
        """
        r = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        description_str = r["choices"][0]["message"]["content"]

        return ast.literal_eval(description_str)

    def thiking_(self) -> str:
        while True:
            function_decs = self.create_function_descriptions_(self.functions)
            res = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
                functions=function_decs)
            finish_reason = res["choices"][0]["finish_reason"]

            if finish_reason == "stop" or len(self.messages) > 3:
                return res["choices"][0]["message"]["content"]
            elif finish_reason == "function_call":
                func_name = res["choices"][0]["message"]["function_call"]["name"]
                func_args = res["choices"][0]["message"]["function_call"]["arguments"]
                func = self.function_maps[func_name]
                func_args = ast.literal_eval(func_args)
                func_res =func(**func_args)
                res_dict = {}
                if type(func_res) == str:
                    res_dict = {"result": func_res}
                elif type(func_res) == dict:
                    res_dict = func_res
                else:
                    res_dict = {"result": str(func_res)}
                res_msg = {"role": "function", "name": func_name, "content": json.dumps(res_dict)}
                self.messages.append(res_msg)
            else:
                raise ValueError(f"Unknown finish reason: {finish_reason}")
    
    def run(self, query: str) -> str:
        self.messages.append({"role": "user", "content": query})
        final_answer = self.thiking_()
        self.messages.append({"role": "assistant", "content": final_answer})
        return final_answer
