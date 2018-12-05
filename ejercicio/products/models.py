from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default="prueba")
    product_number = models.IntegerField(default=1)
    stock = models.IntegerField(default=5)
    price = models.FloatField(default=2.00)

    def __str__(self):
        return self.name

class User(models.Model): 
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.id

class favourites(models.Model):
    id = models.AutoField(primary_key=True)