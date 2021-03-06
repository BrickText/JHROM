UPDATE_MOVIE = '''
    UPDATE MOVIE
    SET NAME=?, RATING=?
    WHERE MOVIE.ID=?;
'''

UPDATE_PROJECTION = '''
    UPDATE PROJECTION
    SET MOVIE_ID=?, TYPE=?, DATE=?
    WHERE PROJECTION.ID=?;
'''

DELETE_RESERVATION = '''
    UPDATE RESERVATION
    SET USER_ID=?, PROJECTION_ID=?, ROW=?, COL=?
    WHERE RESERVATION.ID=?;
'''
