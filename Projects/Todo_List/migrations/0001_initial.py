# Generated by Django 4.2.7 on 2024-01-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Task', models.TextField(max_length=300)),
                ('Date', models.DateField(null=True)),
                ('Time', models.TimeField(null=True)),
                ('Bgcolor', models.CharField(max_length=20, null=False)),
            ],
        ),
    ]
