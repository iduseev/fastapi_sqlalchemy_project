# backend/app.py

from typing import Dict, List, Union, NoReturn

from pydantic import ConfigDict
from dotenv import dotenv_values

from fastapi import FastAPI, Path, Body, Query, HTTPException, status, Request, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from mock_data import DEFAULT_PERSON
from models import Person, Message, Error


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
    response_model=List[Person],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}},
    tags=["people"]
)
async def show_people(
    request: Request,
    limit: int = Query(default=10, example=10)
) -> List[Person]:
    raise NotImplementedError


@app.post(
    "/api/people",
    summary="Create a new person",
    status_code=status.HTTP_201_CREATED,
    response_model=Person,
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}},
    tags=["people"]
)
async def create_person(
    request: Request
) -> Person:
    raise NotImplementedError


@app.get(
    "/api/people/{lname}",
    summary="Read a particular person",
    status_code=status.HTTP_200_OK,
    response_model=Person,
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}},
    tags=["people"]
)
async def read_person(
    request: Request,
    lname: str = Path(..., title="Required last name", example="Fairy")
) -> Person:
    raise NotImplementedError


@app.put(
    "/api/people/{lname}",
    summary="Update an existing person",
    status_code=status.HTTP_200_OK,
    response_model=Message,
    responses={
        status.HTTP_409_CONFLICT: {"model": Error},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}
    },
    tags=["people"]
)
async def update_person(
    request: Request,
    lname: str = Path(..., title="Required last name", example="Fairy"),
    person: Person = Body(..., title="Person data to be updated", example=DEFAULT_PERSON)
) -> Union[Message, NoReturn]:
    raise NotImplementedError


@app.delete(
    "/api/people/{lname}",
    summary="Delete an existing person",
    status_code=status.HTTP_200_OK,
    response_model=Message,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": Error},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Error}
    },
    tags=["people"]
)
async def delete_person(
    request: Request,
    lname: str = Path(..., title="Required last name", example="Fairy"),
) -> Union[Message, JSONResponse]:
    raise NotImplementedError
