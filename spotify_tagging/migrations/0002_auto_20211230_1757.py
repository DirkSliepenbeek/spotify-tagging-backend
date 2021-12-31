# Generated by Django 2.2.4 on 2021-12-30 17:57

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_tagging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('album', models.CharField(max_length=250)),
                ('artists', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify_tagging.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='track',
            name='tags',
            field=models.ManyToManyField(to='spotify_tagging.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='spotify_tagging.Project'),
            preserve_default=False,
        ),
    ]
