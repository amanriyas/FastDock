import os
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def generate_dockerfile(stack: str, production: bool) -> str:
    # Use ChatOpenAI with Groq base URL and key
    llm = ChatOpenAI(
        openai_api_key=os.getenv("GROQ_API_KEY"),
        openai_api_base="https://api.groq.com/openai/v1",  # Groq's endpoint
        model_name="llama3-8b-8192",
        temperature=0.7
    )

    prompt_template = PromptTemplate(
        input_variables=["stack", "mode"],
        template="""
        You are a DevOps expert. Generate a complete Dockerfile for the following tech stack:
        {stack}
        The Dockerfile should be optimized for {mode} use.

        First you should give the complete dockerfile and then afterward then can explain the dockerfile
        line by line so that everyone can understand the dockerfile effectively.
        """
    )

    mode = "production" if production else "development"
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({"stack": stack, "mode": mode})
    
    return response.strip()
