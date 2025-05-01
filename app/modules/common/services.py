from modules.common.repositories import BaseRepository

from sqlmodel import SQLModel

class BaseService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository
        
    async def get_list(self):
        return await self._repository.get_list()
    
    async def get_by_id(self, id: int):
        return await self._repository.get_one(id)
    
    async def create(self, item: SQLModel):
        return await self._repository.create(item)
    
    async def update(self, item: SQLModel, partial = False):
        return await self._repository.update(item, partial)
    
    async def delete(self, id: int):
        return await self._repository.delete(id)
        