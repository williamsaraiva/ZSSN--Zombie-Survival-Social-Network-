from django.db import models


# Create your models here.

class survivor_control(models.Model):
    status_title = models.CharField(max_length=50)
    last_location = models.CharField(max_length=50)
    status_message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    survivor = models.ForeignKey('survivor')

    def __str__(self):
        return "%s" % self.status_title


class survivor(models.Model):
    survivor_name = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.survivor_name


class infected(models.Model):
    status = models.BooleanField(default=True)
    survivor_infected = models.ForeignKey(survivor,related_name='infected_reports', on_delete=models.CASCADE)
    postby = models.ForeignKey(survivor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.survivor_infected


class inventory(models.Model):
    survivor = models.OneToOneField('survivor')
    item_water = models.IntegerField()
    item_food = models.IntegerField()
    item_medication = models.IntegerField()
    item_ammunition = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.survivor_infected