# Generated by Django 3.2.16 on 2023-02-08 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
    ]