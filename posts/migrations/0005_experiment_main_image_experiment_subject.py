# Generated by Django 4.1 on 2022-09-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_experiment_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='main_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='experiment',
            name='subject',
            field=models.CharField(choices=[('P', 'Physics'), ('C', 'Chemistry'), ('B', 'Biology'), ('GS', 'Gneral Science')], max_length=2, null=True),
        ),
    ]