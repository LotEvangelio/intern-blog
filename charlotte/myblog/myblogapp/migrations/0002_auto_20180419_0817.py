# Generated by Django 2.0.4 on 2018-04-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='Post', to='myblogapp.Tag'),
        ),
    ]
