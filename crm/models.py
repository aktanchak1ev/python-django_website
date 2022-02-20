from django.db import models

class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Status Name')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')


    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'



class ComentCrm(models.Model):
    comet_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Application')
    comet_text = models.TextField(verbose_name='Coment Text')
    comet_dt = models.DateTimeField(auto_now=True, verbose_name='Вate of creation')

    def __str__(self):
        return self.comet_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'