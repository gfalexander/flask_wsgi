from billing.models.user.data import UserRepository
from billing.models.user.dto import UserMapper


class AuthService:
    def register(self, request_json: dict):
        user = UserMapper.toCreateDto(request_json)

        created_user = UserRepository().save(user)

        if created_user is None:
            # TODO: Create a custom exception
            raise Exception("User already exists")
        else:
            return UserMapper.toDto(created_user)
