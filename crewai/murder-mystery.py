from crewai import Agent, Crew, Task
from crewai.tools import tool
from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()

response = completion(
  model="sap/gpt-4o",
  messages=[{"role": "user", "content": "I want to check my setup. Is this working?"}],
)
print("Startup check:", response)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(
    ROOT_DIR, "data", "images", "crime-scene.PNG"
)

crime_scene_investigator = Agent(
    role="Crime Scene Investigator",
    goal="Analyze the crime scene shown in the image and extract possible clues, victims, murder weapons, and other relevant details.",
    backstory="An expert crime investigator specialiced on securing evidence.",
    llm="sap/gpt-4o",
    multimodal=True,  # This enables multimodal capabilities
    verbose=True
)

# Create a task for image analysis
inspection_task = Task(
    description=f"Analyze the crime scene image at {IMAGE_PATH} and provide a description of relevant objects.",
    expected_output="A description of the found objects relevant to the crime scene.",
    agent=crime_scene_investigator
)

# Create and run the crew
crew = Crew(
    agents=[crime_scene_investigator],
    tasks=[inspection_task]
)

result = crew.kickoff()
print(result)