from django.db import models

# Create your models here.

class PassPhrase(models.Model):
    phrase = models.TextField(max_length=200,blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-date_created",)
    def __str__(self) -> str:
        return f"Key: {str(self.date_created)}"