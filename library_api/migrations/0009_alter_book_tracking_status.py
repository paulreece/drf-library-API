# Generated by Django 4.0.3 on 2022-04-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0008_alter_note_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_tracking',
            name='status',
            field=models.CharField(choices=[('WTR', 'Want To Read'), ('R', 'Reading'), ('RD', 'Read/Done')], max_length=200),
        ),
    ]
