SELECT_MOVIES_ORDERED_BY_RATING = '''
    SELECT *
    FROM MOVIE
    ORDER BY RATING;
'''

SELECT_PROJECTION_ORDERED_BY_DATE = '''
    SELECT PROJECTION.*, COUNT(RESERVATION.ROW * RESERVATION.COL)
    FROM PROJECTION
    LEFT JOIN RESERVATION
    ON RESERVATION.PROJECTION_ID = PROJECTION.ID
    WHERE PROJECTION.MOVIE_ID = ? AND PROJECTION.DATE BETWEEN ? AND ?
    GROUP BY PROJECTION.ID
    ORDER BY PROJECTION.DATE;
'''

IS_USER_IN_USERS = '''
    SELECT *
    FROM USERS
    WHERE USERNAME = ? and PASSWORD LIKE ?;
'''

SELECT_AVAILABLE_SEATS = '''
    SELECT ROW, COL
    FROM RESERVATIONS
    WHERE PROJECTION_ID = ? AND ROW IS NOT NULL AND COL IS NOT NULL;
'''
