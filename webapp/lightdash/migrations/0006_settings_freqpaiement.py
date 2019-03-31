# Generated by Django 2.1.5 on 2019-03-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightdash', '0005_linkydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='freqPaiement',
            field=models.CharField(choices=[('m', 'Mensuelle'), ('b', 'Bimestrielle')], default='m', max_length=6),
        ),
    ]
