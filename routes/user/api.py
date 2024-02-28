# Import from application modules
from controllers.user.Login import LoginApi
from controllers.user.User import User2Api, UserApi , UserPasswordReset


# Function to initialize route to API Flask
def initialize_routes(api):
    api.add_resource(LoginApi, '/api/v1/login')
    api.add_resource(User2Api, '/api/v1/user')
    api.add_resource(UserApi, '/api/v1/user/<id>')
    api.add_resource(UserPasswordReset, '/api/v1/password-reset')
