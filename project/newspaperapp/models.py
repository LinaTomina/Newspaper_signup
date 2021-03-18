from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Author(models.Model):
    user = models.OnetoOneField(User, on_delete = models.CASCADE)
    author_rating = models.IntegerField(default = 0, verbose_name = 'Рейтинг автора')

    def update_rating(self):
        self.author_rating = (Post.post_rating * 3) + Comment.user.comment_rating + Comment.post.comment_rating
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique = True, verbose_name = 'Наименование категории')
    
class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = 'Автор')
    post_news_choice = models.BooleanField(default = False, verbose_name = 'Новость')
    post_article_choice = models.BooleanField(default=False, verbose_name = 'Статья')
    post_datetime = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата публикации')
    post_category = models.ManyToManyField(Category, through = 'PostCategory')
    post_theme = models.CharField(max_length = 30, verbose_name = 'Название')
    post_text = models.TextField(verbose_name = 'Текст')
    post_rating = models.IntegerField(default = 0, verbose_name = 'Рейтинг публикации')
    

    def like(self):
        self.post_rating = + 1
        self.save()

    def dislike(self):
        self.post_rating = - 1
        self.save()

    def preview(self):
        return self.post_text[0-123] + '...'
    
class PostCategory(models.Model):
    post = models.ForeignKey(Category, on_delete = models.CASCADE)
    category = models.ForeignKey(Post, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.comment_rating = + 1
        self.save()

    def dislike(self):
        self.comment_rating = - 1
        self.save()