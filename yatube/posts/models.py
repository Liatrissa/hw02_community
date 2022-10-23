from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Модель для хранения сообществ"""
    title = models.CharField(max_length=200)
    """Название группы"""
    slug = models.SlugField(unique=True)
    """Уникальный адрес группы"""
    description = models.TextField()
    """Описание сообществ"""
    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для хранения постов"""
    text = models.TextField()
    """Текст поста"""
    pub_date = models.DateTimeField(auto_now_add=True)
    """Дата публикации поста"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    """Автор поста"""
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )
    """Название сообщества"""