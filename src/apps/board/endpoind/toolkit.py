from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service, models


toolkit_router = APIRouter()


@toolkit_router.post('/', response_model=schemas.OutToolkit)
async def create_toolkit(schema: schemas.CreateToolKit):
    return await models.Toolkit.objects.create(**schema.dict())


@toolkit_router.get('/', response_model=List[schemas.OutToolkit])
async def get_toolkit():
    return await models.Toolkit.objects.filter().all()

#
# @toolkit_router.put('/{pk}', response_model=schemas.GetToolkit)
# async def update_toolkit(
#        pk: int, schema: schemas.CreateToolkit, user: models.User = Depends(get_superuser)
# ):
#     return await service.toolkit_s.update(schema, id=pk)
#
#
# @toolkit_router.delete('/{pk}', status_code=204)
# async def delete_toolkit(pk: int, user: models.User = Depends(get_superuser)):
#     return await service.toolkit_s.delete(id=pk)
