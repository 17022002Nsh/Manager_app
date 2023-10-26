from django.db import models

 
class DefaultAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstract = True 
        
        
        
class Board(DefaultAbstract):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
  
     
    class Meta:
        verbose_name_plural = "1) Boards (Sarlovha_boshi)"
      
        
        
class Column(DefaultAbstract):
    title = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="board_columns")
    
    
    def __str__(self) -> str:
        return self.title
    
    
     
    class Meta:
        verbose_name_plural = "2)Column (Sahiga qatorlari) "
        
   
   
class Task(DefaultAbstract):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300,  blank=True, null=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="column_task")
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = "3) Tasks (Vazifalar)"
        
        

class BoardMember(DefaultAbstract):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="board_member")
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='board_user')
    inviter = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='board_inviter')
    token = models.CharField(max_length=200)
    code = models.IntegerField()
    is_activ = models.BooleanField(default=False)
    
    
   
    
    
    
    class Meta:
        verbose_name_plural = "4) Members (Chaqirilgan foydalanuvchilar)"
               
    
    
    
    
    


               
    


    
    

    
    
 