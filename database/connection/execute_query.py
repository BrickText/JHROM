from settings.SharedVariables import SharedVariables


def execute_query(query, args, commit=False, execute_many=False):
    db_wrapper = SharedVariables.database
    c = db_wrapper.get_cursor()
    if execute_many:
        c.executemany(query, args)
    else:
        data = c.execute(query, args)

    if commit:
        db_wrapper.get_db().commit()
        return True
    return data
