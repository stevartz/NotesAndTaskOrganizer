# Generated by Django 3.2.7 on 2021-10-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_name', models.CharField(default='', max_length=100)),
                ('for_class', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assignment',
            name='colorcode',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='for_class',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='class',
            name='course_abbr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='class',
            name='course_num',
            field=models.CharField(default='', max_length=100),
        ),
    ]
