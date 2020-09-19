from django.db import models
# importing reverse function
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# define toy
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

# Create your models here.
class  Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # M:M relationship
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    # redirecting the newly created Finch to Finch Details
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # we will set the default value for meal to be 'B' (for breakfast)
        default=MEALS[0][0]
        )
    
    # create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # the below ensures current date is displayed at the top by default
    class Meta:
        ordering = ['-date']

