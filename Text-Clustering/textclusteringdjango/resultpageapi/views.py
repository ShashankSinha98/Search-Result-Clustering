from rest_framework.response import Response
from rest_framework.decorators import api_view
from .readBackendResult import readResult

@api_view(['GET'])
def list_view(request):
    res_list = readResult()
#     my_list = [
# 	{
# 		"label": "Label 1",
# 		"size": 3,
# 		"documents" : [
# 			{
# 				"rank": 1,
# 				"doc_id": 123,
# 				"name": "doc1.txt",
# 				"content": "This is doc 1"
# 			}, 
# 			{
# 				"rank": 2,
# 				"doc_id": 234,
# 				"name": "doc2.txt",
# 				"content": "This is doc 2"
# 			}, 
# 			{
# 				"rank": 3,
# 				"doc_id": 345,
# 				"name": "doc3.txt",
# 				"content": "This is doc 3"		
# 			}
# 		]
# 	},
	
# 	{
# 		"label": "Label 2",
# 		"size": 2,
# 		"documents" : [
# 			{
# 				"rank": 1,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 4"
# 			}, 
# 			{
# 				"rank": 2,
# 				"doc_id": 567,
# 				"name": "doc5.txt",
# 				"content": "This is doc 5"
# 			}
# 		]		
# 	},
#     {
# 		"label": "Label 3",
# 		"size": 5,
# 		"documents" : [
# 			{
# 				"rank": 1,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 4"
# 			}, 
# 			{
# 				"rank": 2,
# 				"doc_id": 567,
# 				"name": "doc5.txt",
# 				"content": "This is doc 5"
# 			},
#             {
# 				"rank": 3,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 6"
# 			},
#             {
# 				"rank": 4,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 7"
# 			},
#             {
# 				"rank": 5,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 8"
# 			}
# 		]		
# 	},
# 	{
# 		"label": "Label 4",
# 		"size": 4,
# 		"documents" : [
# 			{
# 				"rank": 1,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 4"
# 			}, 
# 			{
# 				"rank": 2,
# 				"doc_id": 567,
# 				"name": "doc5.txt",
# 				"content": "This is doc 5"
# 			},
#             {
# 				"rank": 3,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 6"
# 			},
#             {
# 				"rank": 4,
# 				"doc_id": 456,
# 				"name": "doc4.txt",
# 				"content": "This is doc 7"
# 			}
# 		]		
# 	}
# ]
    return Response({'my_list': res_list})