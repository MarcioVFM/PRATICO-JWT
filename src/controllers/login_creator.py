from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError


class LoginCreator:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username)
        user_id = user[0]
        hashed_password = user[2]

        self.__verify_password(password, hashed_password)
        jwt_token = self.__create_jwt_token(user_id)
        return self.__format_response(username, jwt_token)


    def __find_user(self, username: str) -> tuple[int, str, str]:
        user = self.__user_repository.find_user_by_username(username)
        if not user: raise HttpNotFoundError('User not found')
        return user
    
    def __verify_password(self, password: str, hashed_password: str) -> None:
        correct_password = self.__password_handler.check_password(password, hashed_password)
        if not correct_password: raise HttpBadRequestError('Wrong password')

    def __create_jwt_token(self, user_id: int) -> str:
        payload = {'user_id': user_id}
        jwt_token = self.__jwt_handler.create_token_jwt(payload)
        return jwt_token

    def __format_response(self, username: str, jwt_token: str) -> dict:
        return {
            'message': 'Acess True',
            'username': username,
            'token': jwt_token
        }