from database.queries.insert_queries import INSERT_MOVIE
from database.queries.select_queries import SELECT_MOVIES_ORDERED_BY_RATING
from settings.SharedVariables import SharedVariables
from prettytable import PrettyTable


class Movies():

    def __init__(self):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            self.data = c.execute(SELECT_MOVIES_ORDERED_BY_RATING)
        except Exception:
            print("Database not initilized")

    def __str__(self):
        t = PrettyTable(SharedVariables.movie_col)
        for row in self.data:
            t.add_row([row[0], row[1], row[2]])
        return str(t)

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
    print(Movies())
