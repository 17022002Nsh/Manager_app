<<<<<<< HEAD
from django.urls import path

from .views import (
    BoardCreateAPi, 
    BoardUpdateAPi, 
    BoardColumnUpdate, 
    GetDataAPi, 
    TaskCreateAPi, 
    TaskUpdatedAPi,
    GetBoardDataAPi,
    BoardMemberAPi,
    Tasdiqlash_Verify
   
)

urlpatterns = [
    
    path('board/get_data/<int:pk>/', GetDataAPi.as_view()),
    path('create_board/', BoardCreateAPi.as_view()),
    path('updated_board/<int:pk>/', BoardUpdateAPi.as_view()),
    path('colum/update/<int:id>/', BoardColumnUpdate.as_view()),
    path('task/create/', TaskCreateAPi.as_view()),
    path('task/detail/<int:pk>/', TaskUpdatedAPi.as_view()),
    path('board_data/', GetBoardDataAPi.as_view()),
    path('board_member/', BoardMemberAPi.as_view()),
    path('tasdiqlash/', Tasdiqlash_Verify.as_view()),
    
]
=======
from django.urls import path

from .views import (
    BoardCreateAPi, 
    BoardUpdateAPi, 
    BoardColumnUpdate, 
    GetDataAPi, 
    TaskCreateAPi, 
    TaskUpdatedAPi,
    GetBoardDataAPi,
    BoardMemberAPi,
    Tasdiqlash_Verify
   
)

urlpatterns = [
    
    path('board/get_data/<int:pk>/', GetDataAPi.as_view()),
    path('create_board/', BoardCreateAPi.as_view()),
    path('updated_board/<int:pk>/', BoardUpdateAPi.as_view()),
    path('colum/update/<int:id>/', BoardColumnUpdate.as_view()),
    path('task/create/', TaskCreateAPi.as_view()),
    path('task/detail/<int:pk>/', TaskUpdatedAPi.as_view()),
    path('board_data/', GetBoardDataAPi.as_view()),
    path('board_member/', BoardMemberAPi.as_view()),
    path('tasdiqlash/', Tasdiqlash_Verify.as_view()),
    
]
>>>>>>> d51e158 (..)
