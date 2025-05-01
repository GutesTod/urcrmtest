from modules.common.views import viewsets
from modules.users.container import UserContainer
from modules.users.service import UserService
from modules.users.schemas import (
    UserResponse,
    UserCreate,
    UserUpdateFull,
    UserPartialUpdate
)

class UserViewset(viewsets.ModelViewset):
    def __init__(self, container=None):
        self.container = container or UserContainer()
        self._service = self.container.user_service()
        super().__init__(prefix="/users", tags=['Users'])
        self._setup_mixin_routes()

    @property
    def service(self) -> UserService:
        return self._service

    @property
    def response_model(self):
        return UserResponse

    @property
    def create_model(self):
        return UserCreate

    @property
    def update_model(self):
        return UserUpdateFull

    @property
    def partial_update_model(self):
        return UserPartialUpdate
    