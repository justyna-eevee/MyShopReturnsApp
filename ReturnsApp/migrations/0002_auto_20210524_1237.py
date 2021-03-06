# Generated by Django 3.2.3 on 2021-05-24 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReturnsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='my_return',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ReturnsApp.return'),
        ),
        migrations.AddField(
            model_name='return',
            name='summarized',
            field=models.BooleanField(default=False),
        ),
    ]
