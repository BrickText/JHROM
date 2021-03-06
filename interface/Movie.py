from database.queries.insert_queries import INSERT_MOVIE
from database.queries.update_queries import UPDATE_MOVIE
from database.queries.delete_queries import DELETE_MOVIE
from database.queries.select_queries import SELECT_MOVIES_ORDERED_BY_RATING,\
                                            SELECT_PROJECTION_FOR_MOVIE, \
                                            SELECT_MOVIE_BY_ID

from database.connection.execute_query import execute_query

from settings.SharedVariables import SharedVariables
from prettytable import PrettyTable


class Movies:

    def __init__(self):
        try:
            self.data = execute_query(SELECT_MOVIES_ORDERED_BY_RATING, [])
        except Exception:
            print("Database not initilized or connected")

    def __str__(self):
        t = PrettyTable(SharedVariables.movie_col)
        for row in self.data:
            t.add_row([row[0], row[1], row[2]])
        return str(t)

    @staticmethod
    def get_movie(id):
        try:
            data = execute_query(SELECT_MOVIE_BY_ID, [id, ])
        except Exception:
            print("Database not initilized or connected")

        t = PrettyTable(SharedVariables.movie_col)
        for row in data:
            t.add_row([row[0], row[1], row[2]])
        return str(t)

    @staticmethod
    def add_movie(name, rating):
        try:
            execute_query(INSERT_MOVIE, [name, rating, ], commit=True)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def delete_movie(id):
        try:
            execute_query(DELETE_MOVIE, [id, ], commit=True)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def update_movie(id, name, rating):
        try:
            execute_query(UPDATE_MOVIE, [name, rating, id, ], commit=True)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def movie_projections(id):
        try:
            data = execute_query(SELECT_PROJECTION_FOR_MOVIE, [id, ])

            t = PrettyTable(SharedVariables.projection_col)
            for row in data:
                t.add_row([row[0], row[1], row[2], row[3], (100 - row[4])])
            return str(t)
        except Exception:
            print("Database not initilized or connected!")


if __name__ == '__main__':
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    Movies.add_movie("Baywatch", 10)
    print(Movies.get_movie(2))
