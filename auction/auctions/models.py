# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from users.models import User

class Auction(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True)  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='FinishDate')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerId', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auction'


class Lot(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    auctionid = models.ForeignKey(Auction, models.DO_NOTHING, db_column='AuctionId')  # Field name made lowercase.
    startprice = models.DecimalField(db_column='StartPrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    reserveprice = models.DecimalField(db_column='ReservePrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    currentprice = models.DecimalField(db_column='CurrentPrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    winnerid = models.CharField(db_column='WinnerId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    exhibitiondate = models.DateTimeField(db_column='ExhibitionDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lot'


class Category(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=255)

    class Meta:
        managed = True
        db_table = 'category'


class Bid(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=2)
    placementdate = models.DateTimeField(db_column='PlacementDate')
    lotid = models.ForeignKey(Lot, models.DO_NOTHING, db_column='LotId')
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserId')

    class Meta:
        managed = True
        db_table = 'bid'

