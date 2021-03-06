# Generated by Django 2.1.7 on 2019-03-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('thumbnail', models.ImageField(upload_to='game_thumbnails/')),
                ('game_files', models.FileField(upload_to='games/')),
                ('release_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
