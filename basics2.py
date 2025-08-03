import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams


async def main():
    model_client = OpenAIChatCompletionClient(model='gpt-4o')
    agent_one = AssistantAgent(name='MathTeacher',model_client=model_client,system_message='You are a Math Teacher, explain concepts clearly and ask follow-up questions if required')
    agent_two = AssistantAgent(name='Student',model_client=model_client,system_message='You are a Student, ask questions and be more curious')
    team = RoundRobinGroupChat(participants=[agent_one,agent_two],termination_condition=MaxMessageTermination(max_messages=4))
    await Console(team.run_stream(task='Let us discuss on Multiplication'))
    await  model_client.close()

asyncio.run(main())
