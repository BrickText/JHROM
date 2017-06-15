from database.queries.insert_queries import INSERT_PROJECTION
from database.queries.delete_queries import DELETE_PROJECTION
from database.queries.update_queries import UPDATE_PROJECTION
from database.queries.select_queries import SELECT_PROJECTION_ORDERED_BY_DATE,\
                                            SELECT_PROJECTION_BY_ID

from settings.SharedVariables import SharedVariables
from prettytable import PrettyTable


class Projection:

    def __init__(self, movie_id, projection_date):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            self.data = c.execute(SELECT_PROJECTION_ORDERED_BY_DATE,
                                  [movie_id, projection_date, projection_date +
                                   " " + SharedVariables.end_of_day, ])
        except Exception:
            print("Database not initilized or connected")

    def __str__(self):
        t = PrettyTable(SharedVariables.projection_col)
        for row in self.data:
            # print(row[0], row[1], row[2], row[3], row[4])
            t.add_row([row[0], row[1], row[2], row[3], (100 - row[4])])
        return str(t)

    @staticmethod
    def show_projection(id):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(SELECT_PROJECTION_BY_ID, [id, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def delete_projection(id):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(DELETE_PROJECTION, [id, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def update_projection(id, movie_id, movie_type, date):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(UPDATE_PROJECTION, [movie_id, movie_type, date, id, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initilized or connected")

    @staticmethod
    def add_projection(movie_id, movie_type, date):
        try:
            db_wrapper = SharedVariables.database
            c = db_wrapper.get_cursor()
            c.execute(INSERT_PROJECTION, [movie_id, movie_type, date, ])
            db_wrapper.get_db().commit()
        except Exception:
            print("Database not initilized or connected")


if __name__ == '__main__':
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    Projection.add_projection(1, "2D", "2018-08-11 11:11:11")
    print(Projection(1, "2018-08-11"))
    Projection.update_projection(1, 1, "3D", "2018-08-11 11:11:11")
    print(Projection(1, "2018-08-11"))
