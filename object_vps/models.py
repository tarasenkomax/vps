import uuid

from django.db import models


class VPS(models.Model):
    """ Модель VPS """
    STATUS_LIST = (
        ('started', 'Запущен'),
        ('blocked', 'Заблокирован'),
        ('stopped', 'Остановлен')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Идентификатор')
    cpu = models.PositiveIntegerField(verbose_name='Количество ядер')
    ram = models.CharField(max_length=20, verbose_name='Объем RAM')
    hdd = models.CharField(max_length=20, verbose_name='Объем HDD')
    status = models.PositiveIntegerField(choices=STATUS_LIST, default='stopped', verbose_name='Статус сервера')

    def __str__(self):
        return f'{self.id}: {self.status}'

    class Meta:
        verbose_name_plural = 'VPS'
        verbose_name = 'VPS'
