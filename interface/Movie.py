from database.queries.insert_queries import INSERT_MOVIE
from settings.SharedVariables import SharedVariables


class Movies():

    def __init__(self):
        # SELCT ALL MOVIES
        pass

    def __str__(self):
        return "Movies"

    @staticmethod
    def add_movie(name, rating):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(INSERT_MOVIE, [name, rating, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initialized")


if __name__ == '__main__':
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    Movies.add_movie("Baywatch", 10)
