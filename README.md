# AI/LLM Projects
This repo lists the AI/LLM projects I have built and the skills I have learnt.

### Bank Call Center
       A chatbot that guides a user's money transfer requests. It can ask for more information if needed and execute the transfer.
       Stack: gpt-4, prompt engineering(Role setting, Few Shot Examples, Data Extraction)
### Chatbot with voice
       Conversational chatbot with voice input and character-like voice output.
       Stack: openai (whisper, gpt-3.5), gradio, elevenlabs
### Fine tuning with movie dialogues
       This notebook scrape the dialogs between Theodore and Samantha from movie Her
       Feed them into openAI for fine tuning and retrieve a new model for query.
       Stack: beautifulsoup, openai fine_tunes, davinci
### Retrieval Augmentation From Web Scraping 
       Answer questions using knowledge in the domain www.standford.edu.
       Stack: requests, beautifulsoup, pandas, tiktoken, csv as vectorstore, openai, numpy, openai (ada, gpt-4)
### Langchain agent
        Answer latest questions about 2023 winter xgame with google search.
        Stack: serpapi (google search), langchain (self-ask-with-search agent, zero-shot-rect-description agent)
### Conversation chain 
        Build chatGPT with langchain.
        Stack: langchain (ConversationBufferMemory, ConversationSummaryMemory, ConversationBufferWindowMemory, ConversationKGMemory)
### Image to text conversion 
       Extract text from image and pdf.
       Stack: tesseract, pytesseract, PIL.Image, pypdf2
### Recursive Text Spliter 
       Build a text splitter from scratch.
       Stack: recurssion algorithm.
### Transcribe youtube to text 
       Convert the youtube video: Inflection AI | The AI Friend Zone to text 
       Stack:
       - pytube: import youtube video and get the voice streams.
       - pydub: Chunk large audios into smaller parts .
       - OpenAI Whisper API: Convert them into text. Do the proper formating. 
       - youtube-transcript-api: Alternatively to get the transcript directly if it is subtitle enabled.
### Retrieval agumented conversational agent 
       Chat with an agent on topics related to the nccn liver cancer pdf handbook with retriveal augmentation. 
       Stack: pinecone, langchain (RecursiveCharacterTextSplitter, ConversationBufferMemory, conversational-react-description agent), tiktoken