from django.db.models import Q
from .models import Board, Column, Task
from .serializer import BoardDataSerializer, BoardSerializer,  ColumnSerializer, MemberSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, CreateAPIView



class BoardMemberAPi(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemberSerializer
    
    def perform_create(self, serializer):
        return serializer.save(inviter_id=self.request.user.id)




class GetDataAPi(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDataSerializer
    
    
    def get_queryset(self):
        params = self.request.query_params
        board_id = self.kwargs[self.lookup_field]
        if not board_id:
            return None
        queryset = super().get_queryset().filter(id=board_id, user_id=self.request.user).first()                            
        if not queryset:
            return None
        return queryset.board_columns.all()
        
    
    
class GetBoardDataAPi(ListAPIView):
    
    queryset = Board.objects.all()
    serializer_class = BoardDataSerializer
    pagination_class = None
    
    
    def get_queryset(self):
        params = self.request.query_params
        board_id = params.get("board_id")
        print(board_id)
        if not board_id:
            return None
        queryset = super().get_queryset().filter(id=board_id, user_id=self.request.user.id).first()
        print(queryset)
        if not queryset:
            return None
        return queryset.board_columns.all()
        
    
    



class BoardCreateAPi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return super().get_queryset().filter(
            Q(user_id=self.request.user.id) | Q(board_member__user_id=self.request.user.id)  )    
        
        
class BoardUpdateAPi(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated, )
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    
    
class BoardColumnUpdate(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    permission_classes = (IsAuthenticated, )
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
 
 
class TaskCreateAPi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer  
    
    
    
    
class TaskUpdatedAPi(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer  
    
    
    
    

    
            
        


#  Send message Gmail kod



