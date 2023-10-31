<<<<<<< HEAD
from django.contrib import admin

from .models import  Board, Column, Task, BoardMember


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "description")
    
    
    
@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "board", "title")
    
    
    
@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "column")   
    
    
    
@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "board", "inviter", "token", "code", "is_activ")
    
    
    
=======
from django.contrib import admin

from .models import  Board, Column, Task, BoardMember


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "description")
    
    
    
@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "board", "title")
    
    
    
@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "column")   
    
    
    
@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "board", "inviter", "token", "code", "is_activ")
    
    
    
>>>>>>> d51e158 (..)
