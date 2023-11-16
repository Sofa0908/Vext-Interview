from langchain.chains import LLMChain
from langchain.llms import Cohere
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate(messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a car sales that is trying to make a sale."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ])

llm = Cohere(cohere_api_key="DTwV9xX1ce0k2jXy3HrC7TfoxVRMFxZr3kURv5TV")

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

# Notice that we just pass in the `question` variables - `chat_history` gets populated by memory
conversation({"question": "hi"})

while True:
    message = input("User: ")
    
    # Typing "quit" ends the conversation
    if message.lower() == "quit":
        print("Ending chat.")
        break

    # Chatbot response
    response = conversation({"question": message})
    print(response['text'])
