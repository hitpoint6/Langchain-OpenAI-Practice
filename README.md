# AI/LLM Projects
This repo lists the AI/LLM projects I have built and the skills I have learnt.

### Bank Call Center Chatbot
       A chatbot that guides a user's money transfer requests. It can ask for more information if needed and execute the transfer.
       Stack: gpt-4, prompt engineering(Role setting, Few Shot Examples, Data Extraction), openai function call api
### Chatbot with Voice
       Conversational chatbot with voice input and character-like voice output.
       Stack: openai (whisper, gpt-3.5), gradio, elevenlabs
### Retrieval Augmentation From Web Scraping 
       Answer questions using knowledge in the domain www.standford.edu.
       Stack: requests, beautifulsoup, pandas, tiktoken, csv as vectorstore, openai, numpy, openai (ada, gpt-4)
### Fine Tuning with Movie Dialogues
       This notebook scrape the dialogs between Theodore and Samantha from movie Her
       Feed them into openAI for fine tuning and retrieve a new model for query.
       Stack: beautifulsoup, openai fine_tunes, davinci
### OpenAI Function Call Agent
       Built a langchain like agent using OpenAI's function call API. Capable of
       - Intelligently choose a function to improve answer for an given question.
       - Generate a description of a function given its source code.
       Stack: OpenAI function call API
### Summarize Topics
       Find topics in a given dataset.
       Stack: LLM summary, mapreduce alogrithm, sklearn.cluster.KMeans, silhouette_score
### Chat Stream
       Chat streaming chunk the outputs and send them to client section by section.
       Stack: OpenAI ChatCompletion Stream mode
### Langchain Agent
        Answer latest questions about 2023 winter xgame with google search.
        Stack: serpapi (google search), langchain (self-ask-with-search agent, zero-shot-rect-description agent)
### Conversation Chain 
        Build chatGPT with langchain.
        Stack: langchain (ConversationBufferMemory, ConversationSummaryMemory, ConversationBufferWindowMemory, ConversationKGMemory)
### Image to Text Conversion 
       Extract text from image and pdf.
       Stack: tesseract, pytesseract, PIL.Image, pypdf2
### Transcribe Youtube to Text 
       Convert the youtube video: Inflection AI | The AI Friend Zone to text 
       Stack:
       - pytube: import youtube video and get the voice streams.
       - pydub: Chunk large audios into smaller parts .
       - OpenAI Whisper API: Convert them into text. Do the proper formating. 
       - youtube-transcript-api: Alternatively to get the transcript directly if it is subtitle enabled.
### Retrieval Agumented Conversational Agent 
       Chat with an agent on topics related to the nccn liver cancer pdf handbook with retriveal augmentation. 
       Stack: pinecone, langchain (RecursiveCharacterTextSplitter, ConversationBufferMemory, conversational-react-description agent), tiktoken
### Recursive Text Spliter 
       Build a text splitter from scratch.
       Stack: recurssion algorithm.