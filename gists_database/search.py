from .models import Gist

def search_gists(db_connection, **kwargs):
    query = 'SELECT * FROM gists'
    
    result = []
    params = {}
    
    for name, value in kwargs.items():
        if name == 'created_at':
            git_name = name
            query += ' WHERE datetime({}) = datetime(:date) AND'.format(git_name)
            params.update({'date' : value})
        else:
            git_name = name
            query += ' WHERE {} = :value AND'.format(git_name)
            params.update({'value' : value})
    
    query = query.rstrip(' AND')
    print(params)
    cursor = db_connection.execute(query, params)
        
    for gist in cursor:
        result.append(Gist(gist))
    
    return result
