import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    print('I am inside function')
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
    )
    assistant = AssistantAgent(name ="assistant",model_client=openai_model_client)
    await  Console(assistant.run_stream(task='What is 25 * 25?'))
    await openai_model_client.close()

asyncio.run(main())