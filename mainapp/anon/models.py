from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название вопроса")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    text = models.TextField(verbose_name='Текст')
    time = models.DateTimeField(default=timezone.now,verbose_name="дата публикации")
    auth = models.ForeignKey(User, related_name="profile_post",on_delete=models.CASCADE,verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Article(models.Model):
    text_article = models.TextField(verbose_name='Текст')
    time_article = models.DateTimeField(default=timezone.now,verbose_name="дата публикации")
    auth_article = models.TextField(max_length=255, verbose_name="Вопрос")
    post_article = models.ForeignKey(Post, related_name="article",on_delete=models.CASCADE,verbose_name='Автор')
    likes_article = models.ManyToManyField(User, blank=True, related_name='like')
    def __str__(self):
        return self.text_article
    class Meta:
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменты'



