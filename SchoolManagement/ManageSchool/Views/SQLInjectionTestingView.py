# myapp/unsafe_views.py
from django.http import HttpResponse
from django.db import connection

def unsafe_school_view(request, school_id):
    with connection.cursor() as cursor:
        try:
            # Construct the query
            query = f"SELECT * FROM schooldatamodel WHERE id = '{school_id}';"
            print(f"Executing query: {query}")  # Debugging line
            cursor.execute(query)
            rows = cursor.fetchall()
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
    
    # Convert rows to a string representation
    response_data = '\n'.join([str(row) for row in rows])
    return HttpResponse(response_data, content_type='text/plain')
