from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # Tarkistaa onko alle 2 merkkiä pitkä tai lyhyempi
        pattern_username = '([^a-z\s])|((^|\s)[a-z]{1,2}(\s|$))'
        # Tarkistaa onko 7 merkkiä pitkä tai lyhyempi
        pattern_pass = '([^a-z\s])|((^|\s)[a-z]{1,7}(\s|$))'

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if re.match(pattern_username, username):
            raise UserInputError("Username has to be at least 3 characters long")
        
        if re.match(pattern_pass, password):
            raise UserInputError("Password has to be at least 8 characters long")


