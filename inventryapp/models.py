from django.db import models


# Create your models here.

class Phone(models.Model):
    phone = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.IntegerField()
    model = models.CharField(max_length=200)
    feature = models.CharField(max_length=200)
    camera = models.CharField(max_length=200)
    def getPhone(self):
        return self.phone

    def __str__(self):
        return "Phone={0},Color={1},Price={2},Model={3},Feature={4},camera={5}".format(self.phone, self.color,
                                                                                       self.price, self.model,
                                                                                       self.feature, self.camera)

    class Meta:
        db_table = "phone"
