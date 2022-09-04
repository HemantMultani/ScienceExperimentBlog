# Generated by Django 4.1 on 2022-09-03 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_experiment_main_image_experiment_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='precautions',
            field=models.TextField(default='follow general safety precautions'),
        ),
        migrations.CreateModel(
            name='MaterialsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('quantity', models.CharField(max_length=1000)),
                ('experiment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.experiment')),
            ],
        ),
    ]