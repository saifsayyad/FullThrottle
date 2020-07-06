from django.db import models
import sys, inspect

CLASSES = dict()


class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    class Meta:
        unique_together = (("user", "start_time", "end_time"),)


def init_classes():
    global CLASSES
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            CLASSES[name] = obj


init_classes()
