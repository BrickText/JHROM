DELETE_MOVIE = '''
    DELETE FROM MOVIE
    WHERE MOVIE.ID=?;
'''

DELETE_PROJECTION = '''
    DELETE FROM PROJECTION
    WHERE PROJECTION.ID=?;
'''

DELETE_RESERVATION = '''
    DELETE FROM RESERVATION
    WHERE RESERVATION.ID=?;
'''