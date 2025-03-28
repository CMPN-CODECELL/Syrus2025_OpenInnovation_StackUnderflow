from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("GPT_API_KEY")
print(OPENAI_API_KEY)

llm_config = {
"model": "gpt-3.5-turbo",
"api_key": OPENAI_API_KEY,

}


tax_calculation_agent = AssistantAgent(
    name="TaxCalculator",
    llm_config=llm_config,
    system_message="You are an expert in calculating income tax based on predefined Indian tax regimes."
)

user_context_agent = AssistantAgent(
    name="UserContextManager",
    llm_config=llm_config,
    system_message="You manage and recall user-specific data to assist in filling tax return forms."
)

tax_optimization_agent = AssistantAgent(
    name="TaxOptimizer",
    llm_config=llm_config,
    system_message="You provide tax-saving strategies based on Indian tax laws."
)

user_proxy = UserProxyAgent(
    name="UserProxy",
    llm_config=llm_config,
    system_message="You facilitate communication between the user and the specialized tax agents.",
    code_execution_config={"use_docker": False}
)