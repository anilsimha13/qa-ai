import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    print('I am inside function')
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent(name ="assistant",model_client=openai_model_client)
    image = Image.from_file('/Users/anilsimha/Documents/Upskilling/qa/qa-ai/IMG_3471.jpeg')
    multimedia_message = MultiModalMessage(content = ['Who is the guy in the photo',image], source='user')
    await  Console(assistant.run_stream(task=multimedia_message))
    #await  Console(assistant.run_stream(task='What is 25 * 25?'))
    await openai_model_client.close()

asyncio.run(main())