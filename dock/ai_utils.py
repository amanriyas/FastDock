import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq  # ✅ Use this for Groq Cloud

def generate_dockerfile(stack: str, production: bool) -> str:
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192"  # ✅ Explicitly use Groq-supported model
    )

    prompt_template = PromptTemplate(
        input_variables=["stack", "mode"],
        template="""
        You are a DevOps expert. Generate a complete Dockerfile for the following tech stack:
        {stack}
        The Dockerfile should be optimized for {mode} use.
        """
    )

    mode = "production" if production else "development"

    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({"stack": stack, "mode": mode})
    
    return response.strip()
