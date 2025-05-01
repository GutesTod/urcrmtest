from modules.common.repositories import BaseRepository
from modules.users.models import UserModel

from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository(BaseRepository[UserModel]):
    def __init__(self, db_session: AsyncSession):
        super(UserRepository, self).__init__(UserModel, db_session)