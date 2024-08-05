# backend/app.py

from typing import Dict, List

from dotenv import dotenv_values
from pydantic import ConfigDict

from fastapi import FastAPI, Path, Body, Query, HTTPException, status, Request, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from models import People, Message, Error


# extract environmental variables from .env file
config = dotenv_values(".env")

# initialize FastAPI application instance
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["root"], response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

@app.get(
    "/api/people",
    summary="Read a collection of people",
    status_code=status.HTTP_200_OK,
    response_model=List[People],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}},
    tags=["people"],
)
async def show_people(
    request: Request,
    limit: int = Query(default=10, example=10) 
) -> List[People]:
    raise NotImplementedError
