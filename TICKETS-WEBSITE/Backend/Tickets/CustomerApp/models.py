from django.db import models

# Create your models here.
class otpModel(models.Model):
    phoneNumber = models.CharField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)


    def is_expired(self):
        # Check if the OTP is still valid (e.g., within 5 minutes)
        from django.utils import timezone
        return timezone.now() - self.created_at < timezone.timedelta(minutes=5)

    def __str__(self):
        return f"{self.phoneNumber} - {self.otp}"