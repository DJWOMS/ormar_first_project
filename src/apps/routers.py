from fastapi import APIRouter
from src.apps.board.routers import board_router


api_router = APIRouter()


api_router.include_router(board_router, prefix="/board", tags=["board"])
