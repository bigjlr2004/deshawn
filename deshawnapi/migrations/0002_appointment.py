# Generated by Django 4.1.3 on 2024-10-03 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deshawnapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='deshawnapi.walker')),
            ],
        ),
    ]
