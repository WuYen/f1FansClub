# Generated by Django 4.0.6 on 2022-07-31 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('rank', models.CharField(max_length=100)),
                ('pole', models.CharField(max_length=100)),
                ('champ', models.CharField(max_length=100)),
                ('point', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]