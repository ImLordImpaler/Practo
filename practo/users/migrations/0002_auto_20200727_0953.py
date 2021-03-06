# Generated by Django 3.0.5 on 2020-07-27 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='salutation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Salutation'),
        ),
    ]
