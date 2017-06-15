class SharedVariables:
    database = None

    movie_col = ['Id', 'Name', 'Rating']
    projection_col = ['Id', 'Movie_ID', 'Type', 'Projections Date Time',
                      'Available Spots']

    options = ['show movies', 'show movie projection <movieid> '
               '[<projection date>]', 'make reservation', 'reset database',
               'add movie', 'add projection', 'update movie',
               'update projection', 'update reservation', 'delete movie',
               'delete projection', 'update reservation', 'help', 'exit']

    available_seat = '.'
    taken_seat = 'x'

    number_of_rows = 10
    number_of_cols = 10

    end_of_day = "23:59:59"

    @classmethod
    def get_seats():
        seats = []
        for i in range(SharedVariables.number_of_rows):
            seats.append(list(SharedVariables.number_of_cols *
                              SharedVariables.available_seat))
        return seats
