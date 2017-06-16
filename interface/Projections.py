from database.queries.insert_queries import INSERT_PROJECTION
from database.queries.delete_queries import DELETE_PROJECTION
from database.queries.update_queries import UPDATE_PROJECTION
from database.queries.select_queries import SELECT_PROJECTION_ORDERED_BY_DATE,\
                                            SELECT_PROJECTION_BY_ID

from database.connection.execute_query import execute_query

from settings.SharedVariables import SharedVariables
from prettytable import PrettyTable


class Projection:

    def __init__(self, movie_id, projection_date):
        try:
            self.data = execute_query(SELECT_PROJECTION_ORDERED_BY_DATE,
                                      [movie_id, projection_date,
                                       projection_date +
                                       " " + SharedVariables.end_of_day, ])
        except Exception:
            print("Database not initilized or connected")

    def __str__(self):
        t = PrettyTable(SharedVariables.projection_col)
        for row in self.data:
            t.add_row([row[0], row[1], row[2], row[3], (100 - row[4])])
        return str(t)

    @staticmethod
    def get_projection(id):
        try:
            data = execute_query(SELECT_PROJECTION_BY_ID, [id, ])

            t = PrettyTable(['Projection ID', 'Movie ID',
                            'Movie Type', 'Date Time'])
            for row in data:
                t.add_row([row[0], row[1], row[2], row[3]])
            return str(t)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def delete_projection(id):
        try:
            execute_query(DELETE_PROJECTION, [id, ], commit=True)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def update_projection(id, movie_id, movie_type, date):
        try:
            execute_query(UPDATE_PROJECTION,
                          [movie_id, movie_type, date, id, ], commit=True)
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def add_projection(movie_id, movie_type, date):
        try:
            execute_query(INSERT_PROJECTION, [movie_id, movie_type, date, ],
                          commit=True)
        except Exception:
            print("Database not initilized or connected")


if __name__ == '__main__':
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    Projection.add_projection(1, "2D", "2018-08-11 11:11:11")
    print(Projection(1, "2018-08-11"))
    Projection.update_projection(1, 1, "3D", "2018-08-11 11:11:11")
    print(Projection(1, "2018-08-11"))
