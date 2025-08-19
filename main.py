from csv import writer
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

# Initialise the search tool. Agents will use this to browse the internet
search_tool = SerperDevTool()

# --- Define the agents ---

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

# Agent 2: The Writer
writer = Agent(
    role='Expert Tech Content Strategist',
    goal='Craft compelling and informative reports from research findigs.',
    backstory="""You are a content strategist, famous for your ability to transform complex
    research into clear and insightful reports. You know how to structure a narrative that is both 
    informative and easy to read.""",
    verbose=True,
    allow_delegation=True
)

# --- Define the tasks ---

# Task 1: The Research Task
research_task = Task(
    description="""Conduct an in-depth analysis of the latest trends in {topic}. Identify
    key players, innovations, and market dynamics. Your final answer MUST be a full analysis report.""",
    expected_output='A comprehensive, data-driven report on the latest AI trends.',
    agent=researcher
)

# Task 2: The Writing Task
write_task = Task (
    description="""Using the research findings, write an engaging report on {topic}.
    The report should be well-structured with a clear introduction, body, and conclusion. It should highlight
    the most important trends and insights.""",
    expected_output='A polished and insightful report on {topic}, formatted as markdown.',
    agent=writer
)

# --- Assemble the Crew ---
# Create the Crew, specify agents, tasks and process
research_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

topic_to_research = 'The Future of AI in Sports'
result = research_crew.kickoff(inputs={'topic': topic_to_research})

print("--- Here is the result ---")
print("\n", result)
