# Generated by Django 4.2.3 on 2023-07-14 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='division',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.department', verbose_name='Управление'),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.division', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='userdivisionaccess',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.division', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='userdivisionaccess',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='usersectoraccess',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.sector', verbose_name='Сектор'),
        ),
        migrations.AlterField(
            model_name='usersectoraccess',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
