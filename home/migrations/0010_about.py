# Generated by Django 4.0.6 on 2022-07-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_contact_hos_con_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_hos_img', models.ImageField(upload_to='about')),
                ('abt_hos_description', models.TextField(null=True)),
            ],
        ),
    ]
