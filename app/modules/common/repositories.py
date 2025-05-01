from typing import Generic, Type, TypeVar
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

from sqlmodel import SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.table = model
        self.db_session = db_session

    async def get_list(self):
        async with self.db_session as session:
            query = await session.execute(
                select(self.table).order_by(self.table.id.desc())
            )
            return query.scalars().all()

    async def get_one(self, id):
        async with self.db_session as session:
            query = await session.execute(
                select(self.table).filter(self.table.id == id)
            )
            id_item = query.scalar()
        if not id_item:
            raise HTTPException(status_code=404, detail="Page is not found")
        return id_item

    async def create(self, data: SQLModel):
        async with self.db_session as session:
            item = self.table(**data.model_dump())
            session.add(item)
            await session.commit()
            await session.refresh(item)
        return item

    async def update(self, data: SQLModel, partial: bool = False):
        serializer_data = data.model_dump()
        async with self.db_session as session:
            if partial:
                serializer_data = {k: v for k, v in serializer_data.items() if v is not None}
            if not data:
                raise HTTPException(status_code=400, detail="No data provided for update")
            query = await session.execute(
                update(self.table).values(**serializer_data)
            )
            await session.commit()
        return await query.scalars().all()

    async def delete(self, id):
        async with self.db_session as session:
            await session.execute(
                delete(self.table).filter(self.table.id == id)
            )
            await session.commit()
        return None