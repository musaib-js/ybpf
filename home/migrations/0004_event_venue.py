# Generated by Django 4.2.1 on 2023-06-05 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_eventimages_options_event_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='To Be Decided', max_length=250),
        ),
    ]
