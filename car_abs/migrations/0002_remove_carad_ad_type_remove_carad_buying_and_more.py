# Generated by Django 5.0.1 on 2024-02-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_abs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carad',
            name='ad_type',
        ),
        migrations.RemoveField(
            model_name='carad',
            name='buying',
        ),
        migrations.AddField(
            model_name='carad',
            name='additional_options',
            field=models.CharField(blank=True, choices=[('power_windows', 'Полный электропакет'), ('alarm', 'Сигнализация'), ('remote_start', 'Автозавод')], max_length=50, verbose_name='Опции'),
        ),
        migrations.AddField(
            model_name='carad',
            name='color',
            field=models.CharField(default=1, max_length=50, verbose_name='Цвет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad',
            name='condition',
            field=models.CharField(choices=[('good', 'Хорошее'), ('excellent', 'Идеальное'), ('damaged', 'Аварийное / Не на ходу'), ('new', 'Новое')], default=1, max_length=20, verbose_name='Состояние'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad',
            name='contact_region',
            field=models.CharField(blank=True, max_length=50, verbose_name='Регион контакта'),
        ),
        migrations.AddField(
            model_name='carad',
            name='external_options',
            field=models.TextField(blank=True, verbose_name='Внешний вид'),
        ),
        migrations.AddField(
            model_name='carad',
            name='interior_options',
            field=models.TextField(blank=True, verbose_name='Салон'),
        ),
        migrations.AddField(
            model_name='carad',
            name='media_options',
            field=models.CharField(blank=True, choices=[('CD', 'CD'), ('DVD', 'DVD'), ('MP3', 'MP3'), ('USB', 'USB'), ('subwoofer', 'Сабвуфер')], max_length=50, verbose_name='Медиа'),
        ),
        migrations.AddField(
            model_name='carad',
            name='mileage',
            field=models.PositiveIntegerField(default=1, verbose_name='Пробег'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='carad',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='carad',
            name='safety_options',
            field=models.CharField(blank=True, choices=[('ABS', 'Антиблокировочная система (ABS)'), ('TCS', 'Антипробуксовочная система'), ('ESC', 'Система курсовой устойчивости'), ('airbags', 'Подушки безопасности'), ('parktronik', 'Парктроник'), ('rear_camera', 'Камера заднего вида')], max_length=50, verbose_name='Безопасность'),
        ),
        migrations.AddField(
            model_name='carad',
            name='wheel_drive',
            field=models.CharField(blank=True, max_length=50, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='body_type',
            field=models.CharField(max_length=50, verbose_name='Тип кузова'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='car_type',
            field=models.CharField(choices=[('Продажа', 'Продажа'), ('Покупка', 'Покупка')], max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='drive',
            field=models.CharField(max_length=50, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='engine',
            field=models.CharField(max_length=50, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='generation',
            field=models.CharField(max_length=50, verbose_name='Поколение'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='make_and_model',
            field=models.CharField(max_length=255, verbose_name='Марка и модель'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='modification',
            field=models.CharField(max_length=50, verbose_name='Модификация'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='steering_wheel',
            field=models.CharField(max_length=20, verbose_name='Руль'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='transmission',
            field=models.CharField(max_length=50, verbose_name='Коробка передач'),
        ),
        migrations.AlterField(
            model_name='carad',
            name='year',
            field=models.PositiveIntegerField(verbose_name='Год выпуска'),
        ),
    ]
