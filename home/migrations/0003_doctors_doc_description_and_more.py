# Generated by Django 4.0.6 on 2022-07-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='doc_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='dept_description',
            field=models.TextField(null=True),
        ),
    ]
