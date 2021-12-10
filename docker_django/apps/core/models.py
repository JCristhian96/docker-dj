from django.db import models
 
 
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    photo = models.ImageField(max_length=200,upload_to="persons/",null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'