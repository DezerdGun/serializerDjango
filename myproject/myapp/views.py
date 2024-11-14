from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from .utils import read_data,write_data

# @api_view(['GET'])
# def get_data(request):
#     file_path = os.path.join(os.path.dirname(__file__),'data.json')
    
#     with open(file_path, 'r') as json_file:
#         data = json.load(json_file)
#     return Response(data)    
        
class BookListView(APIView):
    def get(self, request):
        data = read_data()
        return Response(data)

    def post(self, request):
        data = read_data()
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            new_book = serializer.data
            new_book['id'] = max([book['id'] for book in data], default=0) + 1
            data.append(new_book)
            write_data(data)
            return Response(new_book, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailView(APIView):
    def get_object(self,book_id):
        data = read_data()
        for book in data:
            if book['id'] == book_id:
                return book
        return None    
    
    def get(self,request,book_id):
        book = self.get_object(book_id)
        if book is not None :
            return Response(book)
        return Response({"error","Oshibka s book_id"})   
    
    def delete(self,request,book_id):
        data = read_data()
        book = self.get_object(book_id)
        if book is None:
            return Response(book) 
        data = [b for b in data if b['id'] != book_id]
        write_data(data)
        return Response({"message","Id is deleted sucessfule"},status=status.HTTP_204_NO_CONTENT)
    
    
    def put(self,request,book_id):
        print(1)
        data = read_data()
        book = self.get_object(book_id)
        if book is None:
            return Response({"error":"Book is not defined"},
                            status=status.HTTP_404_NOT_FOUND)
        serialize = DataSerializer(data = request.data)
        if serialize.is_valid():
            update_book = serialize.data  
            update_book['id'] = book_id
            for i,b in enumerate(data):
                if b['id'] == book_id:
                    data[i] = update_book
            write_data(data)
            return Response(update_book)
        return Response(serialize.errors,
                        status=status.HTTP_400_BAD_REQUEST)         
    
    
    
    
