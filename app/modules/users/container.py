from dependency_injector import containers, providers
from database import Database

from modules.users.repository import UserRepository
from modules.users.service import UserService

class UserContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database)
    
    user_repository = providers.Factory(
        UserRepository,
        db_session=db.provided.get_session
    )
    
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )