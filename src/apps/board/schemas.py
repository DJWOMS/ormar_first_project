from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class CreateCategory(BaseModel):
    name: str


class OutCategory(BaseModel):
    id: int
    name: str


class CreateToolKit(BaseModel):
    name: str


class OutToolkit(BaseModel):
    id: int
    name: str


class CreateProject(BaseModel):
    name: str
    description: str
    category: int
    toolkit: int
    team: List[int]


class OutProject(BaseModel):
    id: int
    name: str
    description: str
    create_date: datetime
    category: OutCategory
    toolkit: OutToolkit


# class Category(PydanticModel):
#     id: int
#     name: str
#
#     class Config:
#         orm_mode = True
#
#
# class CreateTask(PydanticModel):
#     description: str
#     start_date: datetime
#     end_date: datetime
#     project_id: int
#     worker_id: int = None
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "description": "string",
#                 "start_date": "2020-10-18 15:26:17",
#                 "end_date": "2020-10-18 15:26:17",
#                 "project_id": 0,
#                 "worker_id": 0,
#             }
#         }
#
#
# class CreateCommentTask(PydanticModel):
#     user_id: int
#     task_id: int
#     message: str
#
#
#
# class CreateTeam(BaseModel):
#     project: int
#     team: List[int]
