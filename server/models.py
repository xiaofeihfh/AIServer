from datetime import timedelta
from django.utils import timezone

from django.db import models


# Create your models here.
def calculate_expiration_date(days=10):
    return timezone.now() + timedelta(days=days)


class License(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, auto_created=True)
    machine_code = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_permission = models.IntegerField(default=0)  # 0 试用期  1会员

    def save(self, *args, **kwargs):
        if not self.expiration_date:
            # 设置默认的过期时间，例如当前时间加30天
            self.expiration_date = timezone.now() + timedelta(days=10)
        super(License, self).save(*args, **kwargs)

    def remaining_time(self):
        now = timezone.now()
        delta = self.expiration_date - now
        days, seconds = delta.days, delta.seconds
        hours = seconds // 3600
        return f"剩余{days}天{hours}小时"
