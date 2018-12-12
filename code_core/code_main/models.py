from django.db import models

class Cipher(models.Models):
    to = models.CharField(max_length= 100)
    message = models.TextField()
    direction = models.CharField()
    translaction = models.IntegerField()
    result = models.TextField()

    class Meta:
        db_table = 'code_main'


    def __str__(self):
        return self.to