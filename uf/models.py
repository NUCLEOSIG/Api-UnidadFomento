from django.db import models



class UnidaddeFomento(models.Model):
    fecha = models.DateField(primary_key=True, unique=True, null=False, blank=False, verbose_name='Fecha')
    valor = models.CharField(max_length=50, verbose_name='Valor Diario')
    
    
    def __str__(self):
        return str(self.fecha)

    class Meta:
        verbose_name = 'Unidad de Fomento'
        verbose_name_plural = 'Unidad de Fomento'
        ordering = ['fecha']