# Generated by Django 5.0.3 on 2024-03-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0003_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=185)),
                ('price', models.IntegerField(max_length=55)),
            ],
        ),
    ]
