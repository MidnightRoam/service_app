# Generated by Django 3.2.16 on 2023-02-07 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_subscription_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='comment',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]
