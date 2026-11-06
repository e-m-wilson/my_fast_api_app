from contextlib import asynccontextmanager

from fastapi import FastAPI
from langchain_ollama import ChatOllama

from my_fast_api_app.api.routers import student_router
from my_fast_api_app.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    #application startup 
    app.state.llm = ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
        temperature=0,
        keep_alive='30m'
    )

    yield

    # application shuts down
    app.state.llm = None



app = FastAPI(lifespan=lifespan)

app.include_router(student_router.router)