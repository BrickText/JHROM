from database.queries.insert_queries import INSERT_RESERVATION
from database.queries.delete_queries import DELETE_RESERVATION

from database.connection.execute_query import execute_query


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
