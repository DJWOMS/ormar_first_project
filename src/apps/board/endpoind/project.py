from typing import List
from fastapi import APIRouter, Depends, Body

from .. import schemas, service, models


project_router = APIRouter()


@project_router.post('/', response_model=models.Project)
async def create_project(schema: schemas.CreateProject, repo_name: str = Body(...)):
    proj = models.Project(**schema.dict(exclude={'team'}))
    await proj.save()
    team = await models.Team.objects.get(pk=schema.dict().pop('team')[0])
    await proj.team.add(team)
    return proj


@project_router.get('/', response_model=List[models.Project])
async def get_all_projects():
    return await models.Project.objects.select_related(['category', 'toolkit', 'team']).all()


@project_router.post('/team', response_model=models.Team)
async def create_team(schema: models.Team):
    return await schema.save()


@project_router.get('/team', response_model=List[models.Team])
async def get_all_teams():
    return await models.Team.objects.all()

# @project_router.put('/{pk}', response_model=schemas.OutProject)
# async def update_project(
#         pk: int, schema: schemas.CreateProject, user: models.User = Depends(get_user)
# ):
#     return await service.project_s.update(schema, id=pk, user_id=user.id)
#
#
# @project_router.delete('/{pk}', status_code=204)
# async def delete_project(pk: int, user: models.User = Depends(get_user)):
#     return await service.project_s.delete(id=pk, user_id=user.id)
#
#
# @project_router.post('/team', response_model=schemas.CreateTeam)
# async def create_team(schema: schemas.CreateTeam, user: models.User = Depends(get_user)):
#     return await service.project_s.create_team(schema, user)
#
#
# # @project_router.put('/team/', response_model=schemas.CreateTeam)
# # async def create_team(schema: schemas.CreateTeam):
# #     return await service.project_s.create_team(schema)
