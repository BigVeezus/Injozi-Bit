from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, JWTManager
from flask_bcrypt import generate_password_hash
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource, Api
from mongoengine import FieldDoesNotExist, NotUniqueError, DoesNotExist

from errors import NoAuthorizationError, InternalServerError, SchemaValidationError, EmailAlreadyExistsError, \
     UpdatingUserError, ResetPasswordFieldError, UnauthorizedError, ExpiredSignatureError, \
    UnboundLocalError, InvalidRolesError
from models.User import User


class UserService():
    # Function to Login with HTTP POST Method
    def getAllUsers():
        try:
            # if 'SUPER' in get_jwt_claims()['roles']:
            users = User.objects().exclude('password').to_json()
            return Response(users, mimetype='application/json', status=200)
        # if request failed or does not meet specifications
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except NoAuthorizationError:
            raise NoAuthorizationError
        except ExpiredSignatureError:
            raise ExpiredSignatureError
        except UnboundLocalError:
            raise UnboundLocalError
        
    def createNewUser():
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 201
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        
    def changePassWord():
        try:
            body = request.get_json()
            newPass = body.get('newPassword')
            oldPass = body.get('oldPassword')
            if newPass is None or oldPass is None:
                raise ResetPasswordFieldError

            data = get_jwt_identity()
            user = User.objects().get(username=data)
            
            authorized = user.check_password_hash(body.get('oldPassword'))
            if not authorized:
                raise UnauthorizedError            
            newHashPassword = generate_password_hash(body.get('newPassword')).decode('utf8')
            User.objects.get(username=data).update(password=newHashPassword)
            return Response("password changed successfully", mimetype='application/json', status=200)
        except DoesNotExist:
            raise UpdatingUserError
        

    def deleteUser(id):
            user = User.objects().get(id=id)
            user.delete()
            return Response("user deleted successfully", mimetype='application/json', status=200)
        

    def getUserById(id):
            userbyId = User.objects.exclude('password').get(id=id)
            data = get_jwt_identity()
            user = User.objects().get(username=data)
            if 'ADMIN' not in get_jwt_claims()['roles'] or 'SUPER' not in get_jwt_claims()['roles'] or userbyId['username'] != user['username']:
                raise InvalidRolesError
            userbyId = userbyId.to_json()
            return Response(userbyId, mimetype='application/json', status=200)

        
    def editUserById(id):
                body = request.get_json()
                newPass = body.get('password')
                if newPass != None:
                    raise Exception("password cant be updated with this endpoint")
                User.objects.get(id=id).update(**body)
                return Response("successfully updated", mimetype='application/json', status=200)
