# Generated by Django 4.1.2 on 2022-10-17 16:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('cpu', models.PositiveIntegerField(verbose_name='Количество ядер')),
                ('ram', models.CharField(max_length=20, verbose_name='Объем RAM')),
                ('hdd', models.CharField(max_length=20, verbose_name='Объем HDD')),
                ('status', models.PositiveIntegerField(choices=[('started', 'Запущен'), ('blocked', 'Заблокирован'), ('stopped', 'Остановлен')], default='stopped', verbose_name='Статус сервера')),
            ],
            options={
                'verbose_name': 'VPS',
                'verbose_name_plural': 'VPS',
            },
        ),
    ]
