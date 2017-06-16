from database.queries.insert_queries import INSERT_RESERVATION
from database.queries.delete_queries import DELETE_RESERVATION
from database.queries.select_queries import SELECT_RESERVATIONS_FOR_USER

from database.connection.execute_query import execute_query

from prettytable import PrettyTable


class Reservation:

    @staticmethod
    def make_reservation(data):
        try:
            execute_query(INSERT_RESERVATION, data,
                          commit=True, execute_many=True)
        except Exception as e:
            print(e)
            print("Error when creating reservation")

    @staticmethod
    def delete_reservation(id):
        try:
            execute_query(DELETE_RESERVATION, [id, ], commit=True)
        except Exception as e:
            raise e

    @staticmethod
    def give_user_reservations(id):
        try:
            t = PrettyTable(["Reservation ID", "Movie", "ROW", "COL"])
            data = execute_query(SELECT_RESERVATIONS_FOR_USER, [id, ])
            for row in data:
                t.add_row([row[0], row[1], row[2], row[3]])
            return str(t)
        except Exception as e:
            print(e)
            print("Error while taking information")


if __name__ == '__main__':
    from settings.SharedVariables import SharedVariables
    from database.connection.database_connection import Database
    SharedVariables.database = Database()
    print(Reservation.show_user_reservations(1))
