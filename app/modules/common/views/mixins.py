from abc import abstractmethod

from typing import List

from modules.common.services import BaseService

from sqlmodel import SQLModel
    
class ListMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    @property
    @abstractmethod
    def response_model(self) -> SQLModel:
        pass
    
    
    def setup_routes(self) -> None:
        @self._router.get("/", response_model=List[self.response_model])
        async def get_list():
            return await self.service.get_list()
        
class RetrieveMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    @property
    @abstractmethod
    def response_model(self) -> SQLModel:
        pass
 
    def setup_routes(self) -> None:
        @self._router.get("/{id}", response_model=self.response_model)
        async def get_retrieve(id: int):
            return await self.service.get_one(id)
        
class CreateMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    @property
    @abstractmethod
    def response_model(self) -> SQLModel:
        pass
    
    @property
    @abstractmethod
    def create_model(self) -> SQLModel:
        pass
    
    def setup_routes(self) -> None:
        @self._router.post("/", response_model=self.response_model)
        async def create(item: self.create_model):
            return await self.service.create(item)
        
class UpdateMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    @property
    @abstractmethod
    def response_model(self) -> SQLModel:
        pass
    
    @property
    @abstractmethod
    def update_model(self) -> SQLModel:
        pass
    
    def setup_routes(self) -> None:
        @self._router.put("/", response_model=self.response_model)
        async def update(item: self.update_model, ):
            return await self.service.update(item)
        
class PartialUpdateMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    @property
    @abstractmethod
    def response_model(self) -> SQLModel:
        pass
    
    @property
    @abstractmethod
    def partial_update_model(self) -> SQLModel:
        pass
    
    def setup_routes(self) -> None:
        @self._router.patch("/", response_model=self.response_model)
        async def patch(item: self.partial_update_model):
            return await self.service.update(item, True)
        
class DeleteMixin:
    @property
    @abstractmethod
    def service(self) -> BaseService:
        pass
    
    def setup_routes(self) -> None:
        @self._router.delete("/{id}")
        async def delete(id: int):
            return await self.service.delete(id)
        