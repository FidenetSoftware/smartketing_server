from fastapi import APIRouter

from ..config import ROUTE_PREFIX_V1

from . import users
from . import search
from . import user_search

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(users.router)
    router.include_router(search.router)
    router.include_router(user_search.router)
  

include_api_routes()