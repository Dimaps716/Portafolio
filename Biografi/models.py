from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descricion")
    imag = models.ImageField(verbose_name="Imagen", upload_to="Biografi")
    skills= models.CharField(max_length=30, verbose_name="Heramientas")
    icon = models.ImageField(verbose_name="iconos" )
    icon1 = models.ImageField(null=True, blank=True, verbose_name="iconos 1" )
    icon2 = models.ImageField(null =True, blank=True, verbose_name="iconos 2" )
    icon3 = models.ImageField(null =True, blank=True, verbose_name="iconos 3" )
    icon4 = models.ImageField(null =True, blank=True, verbose_name="iconos 4" )
    icon5 = models.ImageField( null =True, blank=True, verbose_name="iconosb5" )
    icon6= models.ImageField( null =True, blank=True, verbose_name="iconos 6" )
    icon7 = models.ImageField( null =True, blank=True, verbose_name="iconos 7" )
    icon8 = models.ImageField( null =True, blank=True, verbose_name="iconos 8" )


    class Meta:
        verbose_name = "Biografia"

    def __str__(self):
        return self.name