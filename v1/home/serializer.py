<<<<<<< HEAD
from rest_framework import serializers
from django.db import transaction
from v1.services import send_message_email
import random, uuid

from .models import  Board, BoardMember, Column, Task





class MemberSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = BoardMember
        fields = ("id", "user", "board")
        
    def validate(self, attrs):
        res = super().validate(attrs)
        board = res['board']
        user = self.context['request'].user
        
        board_mumber = BoardMember.objects.filter(board_id=board.id,  user_id=user.id).first()
        if board.user.id == user.id  or board_mumber:
            return res
        raise serializers.ValidationError("Board not found")
    
    def create(self, validated_data):
        with transaction.atomic():
            code = random.randint(1000, 9999)
            token = uuid.uuid4()
            data = {
                "code" : code,
                "token" : token
            }
        
            obj = self.Meta.model.objects.create(**validated_data, **data)
       
            send_message_email(obj.user.email, obj.inviter.email,  code=code, token=token)
        return obj
    
    
    
    
    



class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ("id", "title", "description", "column")
        
    def validate(self, attrs):
        res = super().validate(attrs)
        column = res['column']
        user = self.context['request'].user
        if column.board.user.id != user.id:
            raise serializers.ValidationError("Column yaratuvchisi xato")
        return res

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ("id", "title")
        
        
        
        
class BoardSerializer(serializers.ModelSerializer):
    
    columns = serializers.ListField(write_only=True)
    user = serializers.SerializerMethodField()
    # board_memebers = serializers.SerializerMethodField()
    
    class Meta:
        model = Board
        fields = ("id", "title", "description", "user", "columns", )
        
    def get_user(self, obj):
        return {
            "id" : obj.user.id,
            "first_name" : obj.user.first_name,
            "last_name" : obj.user.last_name,
            }
    def create(self, validated_data):
        columns = validated_data.pop("columns")
        board = super().create(validated_data)
        print(columns, board)
        
        
        column_list = []
        for column in columns:
            column_list.append(
                Column(title=column, board=board)
            )
        if column_list:
            Column.objects.bulk_create(column_list)
            print(column_list) 
        
        return board   
       
        # with transaction.atomic():
        #     for column in columns:
        #         Column.objects.create(title=column, board=board)
                
                
    # def get_board_members(self,  instance):
    #     members = User.objects.filter(board_user__board_id=instance.id)
    #     serializer = UserSerializer(members, many=True)
    #     return serializer.data       
           
                
    
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        columns = Column.objects.select_related("board").filter(board_id=instance.id)
        res['columns'] = ColumnSerializer(columns, many=True).data
        return res   
    
    
    
class TaskGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ("id", "title", "description")
            
    
    
class BoardDataSerializer(serializers.ModelSerializer):
    column = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Board
        fields = ("id", "title", "description", "tasks", "column")
    
    
    def get_column(self, instance):
        return {
            "id" : instance.id,
            "title" : instance.title
        }
        
        
    def get_tasks(self, instance):
        return TaskGetSerializer(instance.column_task.all(),  many=True).data
    
    

 
 
 
 
 
 
 #        Gmail  Serializer  kod
 
 
 

        
        
    
           
     
 
 
 
 
 
 
 
 
    
    
    
    
    
    
          
   
   
    
         
        
        
=======
from rest_framework import serializers
from django.db import transaction
from v1.services import send_message_email
import random, uuid

from .models import  Board, BoardMember, Column, Task





class MemberSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = BoardMember
        fields = ("id", "user", "board")
        
    def validate(self, attrs):
        res = super().validate(attrs)
        board = res['board']
        user = self.context['request'].user
        
        board_mumber = BoardMember.objects.filter(board_id=board.id,  user_id=user.id).first()
        if board.user.id == user.id  or board_mumber:
            return res
        raise serializers.ValidationError("Board not found")
    
    def create(self, validated_data):
        with transaction.atomic():
            code = random.randint(1000, 9999)
            token = uuid.uuid4()
            data = {
                "code" : code,
                "token" : token
            }
        
            obj = self.Meta.model.objects.create(**validated_data, **data)
       
            send_message_email(obj.user.email, obj.inviter.email,  code=code, token=token)
        return obj
    
    
    
    
    



class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ("id", "title", "description", "column")
        
    def validate(self, attrs):
        res = super().validate(attrs)
        column = res['column']
        user = self.context['request'].user
        if column.board.user.id != user.id:
            raise serializers.ValidationError("Column yaratuvchisi xato")
        return res

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ("id", "title")
        
        
        
        
class BoardSerializer(serializers.ModelSerializer):
    
    columns = serializers.ListField(write_only=True)
    user = serializers.SerializerMethodField()
    # board_memebers = serializers.SerializerMethodField()
    
    class Meta:
        model = Board
        fields = ("id", "title", "description", "user", "columns", )
        
    def get_user(self, obj):
        return {
            "id" : obj.user.id,
            "first_name" : obj.user.first_name,
            "last_name" : obj.user.last_name,
            }
    def create(self, validated_data):
        columns = validated_data.pop("columns")
        board = super().create(validated_data)
        print(columns, board)
        
        
        column_list = []
        for column in columns:
            column_list.append(
                Column(title=column, board=board)
            )
        if column_list:
            Column.objects.bulk_create(column_list)
            print(column_list) 
        
        return board   
       
        # with transaction.atomic():
        #     for column in columns:
        #         Column.objects.create(title=column, board=board)
                
                
    # def get_board_members(self,  instance):
    #     members = User.objects.filter(board_user__board_id=instance.id)
    #     serializer = UserSerializer(members, many=True)
    #     return serializer.data       
           
                
    
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        columns = Column.objects.select_related("board").filter(board_id=instance.id)
        res['columns'] = ColumnSerializer(columns, many=True).data
        return res   
    
    
    
class TaskGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ("id", "title", "description")
            
    
    
class BoardDataSerializer(serializers.ModelSerializer):
    column = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Board
        fields = ("id", "title", "description", "tasks", "column")
    
    
    def get_column(self, instance):
        return {
            "id" : instance.id,
            "title" : instance.title
        }
        
        
    def get_tasks(self, instance):
        return TaskGetSerializer(instance.column_task.all(),  many=True).data
    
    

 
 
 
 
 
 
 #        Gmail  Serializer  kod
 
 
 

        
        
    
           
     
 
 
 
 
 
 
 
 
    
    
    
    
    
    
          
   
   
    
         
        
        
>>>>>>> d51e158 (..)
        