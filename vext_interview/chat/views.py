import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view

from langchain.chains import LLMChain
from langchain.llms import Cohere
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory

llm = Cohere(cohere_api_key="DTwV9xX1ce0k2jXy3HrC7TfoxVRMFxZr3kURv5TV")

prompt = ChatPromptTemplate(messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a car sales that is trying to make a sale."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

@api_view(["POST"])
def chat(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    response = conversation({"question": body["question"]})
    return JsonResponse({"bot_response": response["text"]})