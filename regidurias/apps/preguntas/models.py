from django.db import models
from django.utils import timezone
# Create your models here.

class Comentarios(models.Model):
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    asunto = models.CharField(max_length=200)
    comentario = models.TextField()
    resolve = models.TextField()
    slug = models.SlugField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.asunto

class ComentariosPost(models.Model):
    resolve = models.TextField()
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    post =  models.ForeignKey(Comentarios, on_delete=models.CASCADE, related_name="commented_posts", default="")
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'Comment by {}'.format(self.nombre)



class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
