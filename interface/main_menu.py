import sys


from interface.Movie import Movies
from interface.Projections import Projection
from interface.User import Users
import interface.interface as interface

from database.connection.database_connection import Database
from settings.SharedVariables import SharedVariables


class MainMenu():

    def __init__(self):
        SharedVariables.database = Database()
        self.users = Users()
        self.reservation = None
        self.is_logged = False
        self.current_user = None
        self.loop()

    def loop(self):
        while True:
            command = interface.input_command()
            if command == 'show movies':
                self.show_movies()
            elif command.find('show movie projection') >= 0:
                if len(command.split()) == 4:
                    self.show_movie_projection(command.split()[-1:])
                else:
                    self.show_movie_projection(command.split()[-2:])
            elif command == 'make reservation':
                self.make_reservation()
            elif command == 'add movie':
                self.add_movie()
            elif command == 'add projection':
                self.add_projection()
            elif command.find('update movie') >= 0:
                if len(command.split()) == 3:
                    self.update_movie(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command.find('update projection') >= 0:
                if len(command.split()) == 3:
                    self.update_projection(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command.find('update reservation') >= 0:
                if len(command.split()) == 3:
                    self.update_reservation(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command.find('delete movie') >= 0:
                if len(command.split()) == 3:
                    self.delete_movie(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command.find('delete projection') >= 0:
                if len(command.split()) == 3:
                    self.delete_projection(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command.find('delete reservation') >= 0:
                if len(command.split()) == 3:
                    self.delete_reservation(int(command.split()[-1:][0]))
                else:
                    interface.incorrect_option()
            elif command == 'reset database':
                SharedVariables.database.reset_database()
            elif command == 'help':
                interface.help()
            elif command == 'exit':
                sys.exit()
            else:
                interface.incorrect_option()

    def show_movies(self):
        print(Movies())

    def show_movie_projection(self, command_split):
        if len(command_split) == 1:
            print(Movies.movie_projections(int(command_split[0])))
        elif len(command_split) == 2:
            print(Projection(int(command_split[0]), command_split[1]))

    def check_taken_seats(self, projection):
        seats = SharedVariables.get_seats()
        taken_seats = []
        reversed_seats = self.reservations.get_taken_seats(projection)
        for row in reversed_seats:
            seats[row[0] - 1][row[1] - 1] = SharedVariables.taken_seat
            taken_seats.append((row[0], row[1]))
        return (seats, taken_seats)

    def choose_seats(self, number_of_tickets, taken_seats):
        temp = 1
        seats = []
        while True:
            temp_seats = interface.choose_seat(temp)
            if temp_seats[0] > SharedVariables.number_of_rows or\
               temp_seats[1] > SharedVariables.number_of_cols:
                interface.out_of_range()
            elif temp_seats in taken_seats or temp_seats in seats:
                interface.taken_seat()
            else:
                seats.append(temp_seats)
                if temp == number_of_tickets:
                    return seats
                    break
                temp += 1

    def make_reservation(self):
        if not self.is_logged:
            self.login_and_registration()
        if self.current_user:
            interface.print_name(self.current_user)

            number_of_tickets = int(interface.choose_number_of_tickets())

            self.show_movies()
            movie = int(interface.choose_movie())

            self.show_movie_projection([movie])
            projection = int(interface.choose_projection())

            seats, taken_seats = self.check_taken_seats(projection)
            self.projection.show_seats(seats)

            reservation_seats = self.choose_seats(number_of_tickets,
                                                  taken_seats)
            reservation_data = self.make_reservation_values(self.
                                                            current_user[0],
                                                            projection,
                                                            reservation_seats)
            self.reservations.reservation(reservation_data)

    def make_reservation_values(self, user_id, projection_id, seats):
        return [(user_id, projection_id, seat[0], seat[1]) for seat in seats]

    def login_and_registration(self):
        option = interface.registration_or_login()
        if option == 'y':
            self.login()
        elif option == 'n':
            self.register()
        else:
            interface.incorrect_option()

    def login(self):
        self.current_user = self.users.is_user(interface.login())
        if self.current_user:
            self.is_logged = True
        else:
            interface.wrong_user_or_pass()
            sys.exit()

    def register(self):
        registration_data = interface.registration()
        if registration_data:
            if not self.users.is_username(registration_data[0]):
                self.current_user = self.users.registration(registration_data)
                self.is_logged = True
            else:
                interface.username_not_free()
        else:
            interface.username_not_free()

    def add_movie(self):
        movie = interface.add_movie()
        Movies.add_movie(movie[0], movie[1])

    def add_projection(self):
        projection = interface.add_projection()
        Projection.add_projection(projection[0], projection[1], projection[2])

    def update_movie(self, movie_id):
        movie = interface.update_movie(Movies.get_movie(movie_id))
        Movies.update_movie(movie_id, movie[0], movie[1])

    def update_projection(self, projection_id):
        projection = interface.update_projection(Projection.
                                                 get_projection(projection_id))
        Projection.update_projection(projection_id, projection[0],
                                     projection[1], projection[2])

    def delete_movie(self, movie_id):
        Movies.delete_movie(movie_id)
        interface.success_delete()

    def delete_projection(self, projection_id):
        Projection.delete_projection(projection_id)
        interface.success_delete()

    def delete_reservation(self, reservation_id):
        Reservstion.delete_reservation(reservation_id)
