from django.db import models
from django.urls import reverse
#reverse ni vazifasi htnl nomidan usha page manzilini tuliq qaytarish masalan:'post/<int:pk>/'

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE  #user o'chirilsa posti ham deleate bulsin
    )

    body = models.TextField()

    def __str__(self):
        return self.title
        #shu postga murojat qilganimizda aynan title kurinib tursin

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])
        # saqlash bosilganda post detail sahifasiga utib ketsin

