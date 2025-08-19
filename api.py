from fastapi import FastAPI
from pydantic import BaseModel
from main import research_crew

app = FastAPI()

class ResearchRequest(BaseModel):
    topic:str

@app.get("/")
def read_root():
    return {"status": "Research crew is online."}

@app.post("/research")
def run_research(request: ResearchRequest):
    """
    Kicks off the research crew with a given topic.
    """
    try:
        result = research_crew.kickoff(inputs={'topic': request.topic})
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
        