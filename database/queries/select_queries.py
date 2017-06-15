SELECT_MOVIES_ORDERED_BY_RATING = '''
    SELECT *
    FROM MOVIES
    ORDER BY RATING;
'''

SELECT_PROJECTIONS_ORDERED_BY_DATE = '''
    SELECT PROJECTIONS.*, COUNT(RESERVATIONS.ROW * RESERVATIONS.COL)
    FROM PROJECTIONS
    LEFT JOIN RESERVATIONS
    ON RESERVATIONS.PROJECTION_ID = PROJECTIONS.ID
    WHERE PROJECTIONS.MOVIE_ID = ? AND PROJECTIONS.PROJECTIONS_DATE LIKE ?
    GROUP BY PROJECTIONS.ID
    ORDER BY PROJECTIONS.PROJECTIONS_DATE;
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
