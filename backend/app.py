# backend/app.py

from typing import Dict, List, NoReturn

from pydantic import ConfigDict
from dotenv import dotenv_values

from fastapi import FastAPI, Path, Body, Query, HTTPException, status, Request, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from utils import utils
from .mock_data import DEFAULT_PERSON, PEOPLE
from .models import Person, Message, Error


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
    limit: int = Query(default=10, examples=[10])
) -> List[Person]:
    return [PEOPLE.values()]


@app.post(
    "/api/people",
    summary="Create a new person",
    status_code=status.HTTP_201_CREATED,
    response_model=Person,
    responses={status.HTTP_406_NOT_ACCEPTABLE: {"model": Error}},
    tags=["people"]
)
async def create_person(
    request: Request,
    person: Person = Body(..., title="New person information", examples=[DEFAULT_PERSON]),
) -> Person | NoReturn:
    fname = person.fname
    lname = person.lname

    if fname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": utils.get_timestamp()
        }
        return PEOPLE[lname]
    raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Person with last name {lname} already exists!"
        )


@app.get(
    "/api/people/{lname}",
    summary="Read a particular person",
    status_code=status.HTTP_200_OK,
    response_model=Person,
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    tags=["people"]
)
async def read_person(
    request: Request,
    lname: str = Path(..., title="Required last name", examples=["Fairy"])
) -> Person | NoReturn:
    if lname in PEOPLE:
        return PEOPLE[lname]
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with last name {lname} not found!"
        )


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
    lname: str = Path(..., title="Required last name", examples=["Fairy"]),
    person: Person = Body(..., title="Person data to be updated", examples=[DEFAULT_PERSON])
) -> Message | NoReturn:
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.fname
        PEOPLE[lname]["timestamp"] = utils.get_timestamp()
        return Message(
            message=f"Person with last name {lname} was updated successfully"
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Person with last name {lname} not found!"
    )


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
    lname: str = Path(..., title="Required last name", examples=["Fairy"]),
) -> Message | JSONResponse:
    if lname in PEOPLE:
        del PEOPLE[lname]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=Message(
                message=f"Person with last name {lname} successfully deleted!",
            ).model_dump()
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Person with last name {lname} not found!"
    )
