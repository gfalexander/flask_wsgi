from billing.models.user.dto import UserMapper
from billing.models.user.data import UserRepository

class AuthService:

    def register(self, request_json: dict):
        user = UserMapper.toCreateDto(request_json)

        created_user = UserRepository().save(user)
        breakpoint()

        if created_user is None:
            # TODO: Create a custom exception
            raise Exception("User already exists")
        else:
            return UserMapper.toDto(created_user)
        