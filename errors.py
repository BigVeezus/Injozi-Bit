class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class NoAuthorizationError(Exception):
    pass


class UpdatingUserError(Exception):
    pass


class ExpiredSignatureError(Exception):
    pass


class DeletingUserError(Exception):
    pass


class UserNotExistsError(Exception):
    pass


class InvalidRolesError(Exception):
    pass

class ResetPasswordFieldError(Exception):
    pass


class UnboundLocalError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "NoAuthorizationError": {
        "message": "Missing Authorization Header",
        "status": 401
    },
    "UpdatingUserError": {
        "message": "Updating user added by other is forbidden",
        "status": 403
    },
    "DeletingUserError": {
        "message": "Deleting user added by other is forbidden",
        "status": 403
    },
    "UserNotExistsError": {
        "message": "User with given id doesn't exists",
        "status": 400
    },
    "InvalidRolesError": {
        "message": "Invalid Role or Cant access this resource",
        "status": 400
    },
    "ResetPasswordFieldError": {
        "message": "currentPassword and newPassword fields must be available",
        "status": 400
    },
    "ExpiredSignatureError": {
        "message": "jwt has expired",
        "status": 400
    },
    "UnboundLocalError": {
        "message": "only SUPER role can access this resource",
        "status": 401
    }
}
