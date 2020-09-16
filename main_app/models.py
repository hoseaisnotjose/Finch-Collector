from django.db import models

# Create your models here.
class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name,
        self.breed = breed,
        self.description = description,
        self.age = age
        
finches = [
    Finch('Kiwi', 'Firetail', 'Aussie', '2'),
    Finch('Pikachu', 'Bramling', 'Euro', '3'),
    Finch('Skittles', 'Gold', 'bling', '1')
]
