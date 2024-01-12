from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuerySerializer
from .models import Query
from .getQueryandK import GetQueryAndClusterCount

from .KMeans import queryCluster

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def query_list(request):
    if request.method == 'GET':
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # Add query here
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Call TestFunction after saving data
            data = GetQueryAndClusterCount()
            if data != None:
                query = data["query"]
                cluster_count = data["k_value"]

                res = queryCluster(query=query, no_of_results=50, K=cluster_count, save_result=True)
                print(res)
            print("POST SUCCESS")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # Handle update logic
        pass

    elif request.method == 'DELETE':
        # Handle delete logic
        pass

# Add other views as needed
