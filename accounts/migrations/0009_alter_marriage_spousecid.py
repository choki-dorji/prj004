# Generated by Django 4.1 on 2022-11-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_marriage_spousecid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marriage',
            name='Spousecid',
            field=models.IntegerField(),
        ),
    ]
