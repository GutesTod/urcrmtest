from abc import ABC

from fastapi import APIRouter

from typing import List, Optional

from modules.common.views import mixins

class BaseRouter(ABC):
    def __init__(self, prefix: str = "", tags: Optional[List[str]] = None):
        self._router = APIRouter(prefix=prefix, tags=tags or [])
    
    def _setup_mixin_routes(self):
        for base in self.__class__.__mro__:
            if base != BaseRouter and hasattr(base, 'setup_routes') and base != self.__class__:
                base.setup_routes(self)
                
    def get_router(self) -> APIRouter:
        return self._router
    
class ModelViewset(
    BaseRouter,
    mixins.ListMixin,
    mixins.RetrieveMixin,
    mixins.CreateMixin,
    mixins.UpdateMixin,
    mixins.PartialUpdateMixin,
    mixins.DeleteMixin
):
    pass