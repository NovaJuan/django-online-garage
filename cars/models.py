from django.db import models
from django.db.models import Avg


class Car(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='uploads/cars', default='default.jpg')
    pub_date = models.DateField('Published', auto_now_add=True)

    def __str__(self):
        return self.name

    def avg_rating(self):
        average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']

        if average == None:
            return 'No rate'

        return '%.1f' % average


class Review(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=1)
    pub_date = models.DateField('Created', auto_now_add=True)

    def __str__(self):
        return f'ID {self.id} | ({self.pub_date})'
