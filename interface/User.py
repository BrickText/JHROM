from database.queries.select_queries import IS_USER_IN_USERS
from database.queries.insert_queries import INSERT_USER

from settings.SharedVariables import SharedVariables


class Users:
    def __init__(self):
        try:
            self.c = SharedVariables.database.get_cursor()
        except Exception:
            print("Databse connection problem")

    def is_user(self, user_and_pass):
        result = self.c.execute(IS_USER_IN_USERS,
                                [user_and_pass[0], user_and_pass[1], ])
        first = result.fetchone()
        if first is not None:
            return first
        else:
            return None

    def is_username(self, username):
        result = self.c.execute(IS_USER_IN_USERS, [username, '%%', ])
        first = result.fetchone()
        if first is not None:
            return True
        else:
            return False

    def registration(self, user_and_pass):
        self.c.execute(INSERT_USER, [user_and_pass[0], user_and_pass[1], 1, ])
        SharedVariables.database.get_db().commit()
        return self.is_user(user_and_pass)
