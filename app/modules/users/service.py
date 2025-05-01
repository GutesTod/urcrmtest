from modules.common.services import BaseService

from modules.users.repository import UserRepository

class UserService(BaseService):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)