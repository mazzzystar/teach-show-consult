import os
import pickle
import API_KEY
from teach import ALDA_LANG_RULE
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain

os.environ["OPENAI_API_KEY"] = API_KEY.OPENAI_API_KEY

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
You can assume the question about music composition.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = ALDA_LANG_RULE+"""You are given the following extracted parts of the fragments taken from many beautiful musical works written in Alda language and a user input fregment. Provide a conversational answer to guide the user on what to write next. 
You need to let the parts you suggest and the parts provided by the user make up the beautiful music. Your answer must be a complete and correct Alda code and the note section must begin with the one provided by the user.
User Input: {question}
=========
{context}
=========
Your answer in full Adla format code:"""
QA_PROMPT = PromptTemplate(template=template, input_variables=["question", "context"])


def get_chain(vectorstore):
    llm = OpenAI(temperature=0)
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain


if __name__ == "__main__":
    with open("vectorstore.pkl", "rb") as f:
        vectorstore = pickle.load(f)
    qa_chain = get_chain(vectorstore)
    chat_history = []
    print("Let's consult the music master!")
    while True:
        print("You:")
        question = input()
        result = qa_chain({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        print("Music Master:")
        print(result["answer"])
        f = open('output.alda', 'w')
        f.write(result["answer"])
        f.close()
        print("\n[INFO] Notes saved to: output.alda")