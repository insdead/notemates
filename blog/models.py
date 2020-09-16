from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    #users = [str(user) for user in User.objects.all()]
    field_choices=(('A','A'),
                   ('B','B'))
    Заголовок = models.CharField(max_length=100)
    Описание = models.TextField()
    field=models.CharField(max_length=100, choices=field_choices, default='general')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Урок=models.CharField(max_length=100)
    likes=models.ManyToManyField(User, related_name="blog_posts")
    image = models.ImageField(upload_to='posts', blank=True)
    image2 = models.ImageField(upload_to='posts', blank=True)
    image3 = models.ImageField(upload_to='posts', blank=True)
    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.Заголовок

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.Заголовок