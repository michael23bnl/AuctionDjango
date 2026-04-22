from django.db import models


class User(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    firstname = models.CharField(db_column='FirstName', max_length=255)
    lastname = models.CharField(db_column='LastName', max_length=255)
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=18, decimal_places=2)
    email = models.CharField(db_column='Email', max_length=255)
    hashedpassword = models.CharField(db_column='HashedPassword', max_length=255)
    role = models.IntegerField(db_column='Role')
    isblocked = models.BooleanField(db_column='IsBlocked')

    class Meta:
        managed = True
        db_table = 'user'


