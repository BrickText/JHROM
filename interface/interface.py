from ast import literal_eval
import numpy


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


def show_seats(seats):
    b = numpy.array(list(range(1, settings.number_of_rows + 1)))
    print(str(b).replace(',', '').replace('[', '').replace(']', '')
                .replace('  ', ' '))
    a = numpy.array(seats)
    a = numpy.c_[a, [[i] for i in range(1, settings.number_of_cols + 1)]]
    print(' ' + str(a).replace(',', '').replace('\'', '')
                      .replace('[', '').replace(']', ''))


def choose_seat(number_of_seat):
    return literal_eval(input('Choose seat {0} (row, col)> '
                              .format(number_of_seat)))


def out_of_range():
    print('Seat out of range')


def taken_seat():
    print('This seat is taken!')


def help():
    for el in settings.options:
        print(el)
