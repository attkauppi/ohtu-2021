import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if password != password_confirmation:
            raise UserInputError("Passwords did not match")

        # Tarkistaa onko alle 2 merkkiä pitkä tai lyhyempi
        pattern_username = '([^a-z\s])|((^|\s)[a-z]{1,2}(\s|$))'
        # Tarkistaa, onko merkkijonossa vain kirjaimia (isoja/pieniä)
        pattern_pass = re.compile("^[a-zA-Z]+$")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if re.match(pattern_username, username):
            raise UserInputError("Username has to be at least 3 characters long")
        
        # Reject if no special characters or numbers or length under 8
        if re.match(pattern_pass, password) or len(password) < 8:
            raise UserInputError("Password has to be at least 8 symbols long and can't contain only letters")


user_service = UserService()
