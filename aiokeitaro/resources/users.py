from aiokeitaro.api import API


class User(API):

    def __init__(self, client, endpoint='users'):
        super(User, self).__init__(client, endpoint)

    async def get(self, user_id):
        """
        Gets user by user_id
        """
        return await super(User, self).get(user_id)

    async def create(self, login, password, user_type='USER'):
        """
        Creates new user with login, password and 
        type (USER or ADMIN), USER by default
        """
        return await super(User, self).post(
            login=login, new_password=password,
            new_password_confirmation=password, type=user_type)
