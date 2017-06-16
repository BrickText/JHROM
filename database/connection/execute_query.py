from settings.SharedVariables import SharedVariables


def execute_query(query, args, commit=False):
    db_wrapper = SharedVariables.database
    c = db_wrapper.get_cursor()
    if commit:
        c.execute(query, args)
        db_wrapper.get_db().commit()
        return True
    else:
        return c.execute(query, args)
