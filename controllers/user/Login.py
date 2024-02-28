import datetime

# Import from system libraries
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from mongoengine import DoesNotExist

# Import from application modules
from errors import UnauthorizedError, InternalServerError
from service.auth import AuthService


# Class Login API to load in Routes
class LoginApi(Resource):
    # Function to Login with HTTP POST Method
    def post(self):
        try:
            return AuthService.login()
        # Throw error
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError
                