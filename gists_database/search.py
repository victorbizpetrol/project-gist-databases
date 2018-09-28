from .models import Gist

# def search_gists(db_connection, **kwargs):
#     query = 'SELECT * FROM gists'
    
#     result = []
#     for name, value in kwargs.items():
#         if name == 'created_at':
#             query += ' WHERE datetime("{}") = datetime("{}") AND'.format(name, value)
#         else:
#             query += ' WHERE {} = "{}" AND'.format(name, value)
    
#     cursor = db_connection.execute(query.rstrip(' AND'))
        
#     for gist in cursor:
          #Takes query result and converts it to a Gist object using Gist in models.py
#         result.append(Gist(gist))
    
#     return result

# print(search_gists('db', github_id='4232a4', created_at='time'))

def search_gists(db_connection, **kwargs):
    query = 'SELECT * FROM gists'
    
    result = []
    params = {}
    for name, value in kwargs.items():
        if name == 'created_at':
            query += ' WHERE datetime(":date_name") = datetime(":date") AND'
            params.update({'date_name' : name})
            params.update({'date' : value})
        else:
            query += ' WHERE :name = ":value" AND'
            params.update({'name' : name}, {'value' : value})
        
    cursor = db_connection.execute(query.rstrip(' AND'), params)
        
    for gist in cursor:
        result.append(Gist(gist))
    
    return result