from django.db import models

class Passengers(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class DeparturePoint(models.Model):
    departure = models.CharField(max_length=3)

    def __str__(self):
        return self.departure

class ArrivalPoint(models.Model):
    arrival = models.CharField(max_length=3)

    def __str__(self):
        return self.arrival

class DepartureTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class ArrivalTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class Distance(models.Model):
    kilometers = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.kilometers)

class TransportId(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)

class TransportType(models.Model):
    TYPES = (
        ('plane', 'Plane'),
        ('car', 'Car'),
        ('train', 'Train'),
        ('subway', 'Subway'),
        ('motorbike', 'Motorbike'),
        ('boat', 'Boat'),
    )
    type = models.CharField(max_length=20, choices=TYPES)

    def __str__(self):
        return self.type