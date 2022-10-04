from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER=(
    (0, 'female'),
    (1, 'male'),
    )

class Data(models.Model):
    name= models.CharField(max_length= 100, null= True)
    age= models.PositiveIntegerField(validators=[MinValueValidator(13), MaxValueValidator(19)],null= True)
    height= models.PositiveIntegerField()
    sex= models.PositiveIntegerField(choices= GENDER, null= True)
    predictions= models.CharField(max_length=100, blank= True)
    date= models.DateTimeField(auto_now_add= True)

    def save(self, *args, **kwargs):
        Ml_model= joblib.load('ml_model/Ml_sport_model.joblib')
        self.predictions=Ml_model.predict([[self.age, self.height, self.sex]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering= ['-date']
    
    def __str__(self):
        return self.name

# Create your models here.
