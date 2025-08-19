import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

# Initialise the search tool. Agents will use this to browse the internet
search_tool = SerperDevTool()

# --- Define Your Agents ---

# Agent 1: The Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover the latest developments and information on a given topic.',
    backstory="""You are a world-class research analyst, knwon for your ability
    to find interesting facts and data. You are an expert in using search tools to find the
    most relevant and up-to-date information.""",
    verbose=True,
    alow_delegation=False,
    tools=[search_tool]
)
