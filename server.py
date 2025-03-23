from fastapi import FastAPI
from pydantic import BaseModel
from ChatInterface import generate_response
from gitCloner import fetch_repo_from_git_link

class Question(BaseModel):
    question: str

class Url(BaseModel):
    url: str

app = FastAPI()

@app.get("/health")
def getHealth():
    return { "Status" : "Ok"}

@app.post("/generate")
def generate_from_llm(question: Question):
    response = generate_response(question.question)
    return {"Response": response}


@app.post("/clonerepo")
def clone_repo_from_url(url: Url):
    status = fetch_repo_from_git_link(url.url)
    if status:
        return {"status": "Ok" }
    else:
        return {"status": "Error"}
