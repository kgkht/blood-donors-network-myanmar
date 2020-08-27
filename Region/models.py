from django.db import models

# Create your models here.
class Division(models.Model):
    Region_Division = [
            ('AYAR', "Ayeyarwady"),
            ('BAGO', "Bago Region"),
            ('CHIN', "Chin State"),
            ('KCIN', "Kachin State"),
            ('KYAH', "Kayah State"),
            ('KYIN', "Kayin State"),
            ('MGWY', "Magway Region"),
            ('MDLY', "Mandalay Region"),
            ('MONS', "Mon State"),
            ('RKIN', "Rakhine State"),
            ('SHAN', "Shan State"),
            ('SAGI', "Sagaing Region"),
            ('TNDY', "Taninthary Region"),
            ('YGON', "Yangon Region"),
            ]
    name = models.CharField("Region/Division",
                            max_length=4, 
                            choices=Region_Division,
                            default='AYAR')
    
    def __str__(self):
        return self.name






class Township(models.Model):
    division = models.ForeignKey('Division',on_delete=models.CASCADE)
    name = models.CharField("Township", max_length=30, help_text="Enter City/Township.")
    
    def __str__(self):
        return self.name
        



class Address(models.Model):
    address = models.TextField()
    city = models.ForeignKey('Township', on_delete=models.CASCADE)
    def __str__(self):
        return self.address