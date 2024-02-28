from flask import Response, request, Flask
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, JWTManager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource
from mongoengine import  DoesNotExist, InvalidQueryError

from errors import NoAuthorizationError, InternalServerError, SchemaValidationError,  \
     UpdatingUserError,  UnauthorizedError, \
    UnboundLocalError, UserNotExistsError, InvalidRolesError
from models.User import User
from service.user import UserService



class User2Api(Resource):
    @jwt_required
    def get(self):
        try:
             if 'SUPER' in get_jwt_claims()['roles']:
                return UserService.getAllUsers()
        except InternalServerError:
            raise InternalServerError

    @jwt_required
    def post(self):
        try:
            if 'ADMIN' in get_jwt_claims()['roles'] or 'SUPER' in get_jwt_claims()['roles']:
                return UserService.createNewUser()
        except Exception:
            raise InternalServerError


class UserPasswordReset(Resource):
    @jwt_required
    def post(self):
        try:
            return UserService.changePassWord()
        except UnauthorizedError:
            raise UnauthorizedError
        except Exception:
            raise InternalServerError


class UserApi(Resource):
    @jwt_required
    def delete(self, id):
        try:
            if 'ADMIN' not in get_jwt_claims()['roles'] and 'SUPER' not in get_jwt_claims()['roles']:
                raise InvalidRolesError
            return UserService.deleteUser(id)  
        except DoesNotExist:
            raise UserNotExistsError
        except UserNotExistsError:
            raise UserNotExistsError
        except InvalidRolesError:
            raise InvalidRolesError
        except Exception:
            raise InternalServerError

    @jwt_required
    def get(self, id):
        try:
            return UserService.getUserById(id)
        except NoAuthorizationError:
            raise NoAuthorizationError
        except DoesNotExist:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, id):
        try:
            userbyId = User.objects.get(id=id)
            data = get_jwt_identity()
            user = User.objects().get(username=data)
            if 'ADMIN' not in get_jwt_claims()['roles'] and 'SUPER' not in get_jwt_claims()['roles'] and userbyId['username'] != user['username']:
                raise InvalidRolesError
            return UserService.editUserById(id)
        except InvalidQueryError:
            raise SchemaValidationError
        except InvalidRolesError:
            raise InvalidRolesError
        except DoesNotExist:
            raise UpdatingUserError
        except Exception:
            raise InternalServerError
