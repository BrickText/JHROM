from ast import literal_eval
import numpy
from getpass import getpass
import hashlib

from settings.SharedVariables import SharedVariables
from settings.validators import validate_password


def input_command():
    return input('> ')


def print_name(user):
    print('Hello, ' + user[1])


def choose_number_of_tickets():
    return input('Choose number of tickets> ')


def choose_movie():
    return input('Choose a movie> ')


def choose_projection():
    return input('Choose a projection> ')


def registration_or_login():
    return input('Do you have account?(y, n)')
    print('You need to be a user in the system to make reservations!')


def show_seats(seats):
    b = numpy.array(list(range(1, SharedVariables.number_of_rows + 1)))
    print(str(b).replace(',', '').replace('[', '').replace(']', '')
                .replace('  ', ' '))
    a = numpy.array(seats)
    a = numpy.c_[a,
                 [[i] for i in range(1, SharedVariables.number_of_cols + 1)]]
    print(' ' + str(a).replace(',', '').replace('\'', '')
                      .replace('[', '').replace(']', ''))


def choose_seat(number_of_seat):
    return literal_eval(input('Choose seat {0} (row, col)> '
                              .format(number_of_seat)))


def login():
    username = input('Username: ')
    password = getpass('Password: ')
    hash_pass = hashlib.sha512(password.encode()).hexdigest()
    return (username, hash_pass)


def registration():
    username = input('Username: ')
    password = getpass('Password: ')

    if getpass('Repeat Password: ') != password:
        print('Two passwords doesn\'t match')
        if getpass('Try again: ') != password:
            print('Two passwords doesn\'t match')
            return 0
    if validate_password(password):
        hash_pass = hashlib.sha512(password.encode()).hexdigest()
        return (username, hash_pass)
    else:
        print('Your password is invalid. Password must have digit, lower and' +
              ' upper letters and to be at least 7 symbols.')
        return 0


def wrong_user_or_pass():
    print('Your username or password is incorrect')


def username_not_free():
    print('Username is not free')


def out_of_range():
    print('Seat out of range')


def taken_seat():
    print('This seat is taken!')


def help():
    for el in SharedVariables.options:
        print(el)
