from database.queries.insert_queries import INSERT_PROJECTION
from settings.SharedVariables import SharedVariables


class Projection():
    def __init__(self, movie_id, projection_date):
        pass

    def __str__(self):
        pass

    @staticmethod
    def add_projection(movie_id, movie_type, date):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(INSERT_PROJECTION, [movie_id, movie_type, date, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initialized")


if __name__ == '__main__':
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    Projection.add_projection(1, "2D", "2018-08-11 11:11:11")
