# Generated by Django 3.1.3 on 2021-04-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0004_auto_20210309_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(default='', max_length=100)),
                ('aEmail', models.EmailField(default='', max_length=100)),
                ('apassword', models.CharField(default='', max_length=50)),
                ('acpassword', models.CharField(default='', max_length=50)),
                ('aphone', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='cpassword',
            field=models.CharField(default='', max_length=500),
        ),
    ]
