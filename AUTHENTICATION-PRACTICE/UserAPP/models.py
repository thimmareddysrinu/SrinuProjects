from django.db import models

# Create your models here.
class SendOtp(models.Model):
    phoneNumber = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    def is_expired(self):
        from datetime import timedelta
        from django.utils import timezone
        return self.created_at < timezone.now() - timedelta(minutes=5)
    

    def __str__(self):
        return f"OTP for {self.phoneNumber}: {self.otp}"
