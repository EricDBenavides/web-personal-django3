from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Title")
    description = models.TextField(verbose_name = "Description")
    image = models.ImageField(verbose_name = "Image", upload_to= "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Created")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Edited")
    url = models.URLField(null=True,blank=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ['-created'] 

    def __str__(self):
        return f'{self.title}'