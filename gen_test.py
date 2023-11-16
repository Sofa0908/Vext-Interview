from langchain.chains import LLMChain
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = Cohere(cohere_api_key="DTwV9xX1ce0k2jXy3HrC7TfoxVRMFxZr3kURv5TV")
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(question)
print(llm_chain.run(question))