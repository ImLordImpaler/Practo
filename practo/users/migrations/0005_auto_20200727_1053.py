# Generated by Django 3.0.5 on 2020-07-27 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200727_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='category',
            field=models.CharField(choices=[('Dental', 'Dental'), ('Neuro', 'Neuro'), ('Child', 'Child'), ('Bone', 'Bone'), ('General', 'General'), ('Heart', 'Heart'), ('Eyes', 'Eyes'), ('Gyno', 'Gyno')], max_length=100, null=True),
        ),
    ]
