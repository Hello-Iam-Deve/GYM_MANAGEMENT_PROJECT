# Generated by Django 5.0.3 on 2024-03-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0010_chest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
