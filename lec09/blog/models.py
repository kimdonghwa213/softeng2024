from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) #제목 넣는 칸 최대 30글자
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):        #제목 설정하는거
        return f'[{self.pk}]{self.title}'