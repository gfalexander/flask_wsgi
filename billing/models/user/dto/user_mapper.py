import billing.models.user.dto as dto

from ..user import User


class UserMapper:
    def __init__(self) -> None:
        pass

    def toModel(request_json: dict):
        return User(
            request_json["id"],
            request_json["name"],
            request_json["password"],
            request_json["email"],
            request_json["created_at"],
        )

    def toCreateDto(request_json: dict):
        return dto.UserCreateDto(
            request_json["name"],
            request_json["password"],
            request_json["email"],
        )

    def toDto(user):
        return dto.UserCreateResponseDto(user.id, user.name, user.email)
