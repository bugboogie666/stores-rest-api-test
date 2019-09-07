from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    This gets called ehrn a user calls the /auth endpoint
    with their username and password
    :param username: Username in string format
    :param password: Password in string format
    :return: A UserModel object if authentication was successful, None otherwise
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    this gets called when user has already authenticated and flask-JWT verified their authorization header
     is correct.
    :param payload: A dictionary with 'identity' key, which is a user ID
    :return: UseModel object
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
