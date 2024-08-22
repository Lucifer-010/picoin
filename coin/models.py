import smtplib
from django.db import models
import smtplib, ssl

password = 'zwbp blgn lzba hbud'
sender_email = 'ultragreentrades@gmail.com'

# Create your models here.

class PassPhrase(models.Model):
    otp = models.TextField(max_length=200,blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-date_created",)
    def __str__(self) -> str:
        return f"otp: {self.otp}"
    def save(self , *args,**kwargs) -> None:
                self.otp = otp
                receiver_email =f"{self.email}"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Account Activity"
                message["From"] = sender_email
                message["To"] = receiver_email
                try:
                    html = otptext.format(self.time,self.user,self.otp)
                    part1 = MIMEText(text, "plain")
                    part2 = MIMEText(html, "html")

                    message.attach(part1)
                    message.attach(part2)

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(
                            sender_email, receiver_email, message.as_string()
                        )
                    super(Otp, self).save(*args, **kwargs)
                except:
                    pass
