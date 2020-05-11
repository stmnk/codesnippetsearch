# Generated by Django 3.0.5 on 2020-05-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2048)),
                ('repo', models.CharField(max_length=256)),
                ('file_path', models.CharField(max_length=2048)),
                ('identifier', models.CharField(max_length=2048)),
                ('language', models.CharField(max_length=32)),
                ('code', models.TextField()),
                ('code_hash', models.CharField(max_length=64)),
                ('embedded_row_index', models.IntegerField()),
            ],
        ),
        migrations.AddIndex(
            model_name='codedocument',
            index=models.Index(fields=['language', 'embedded_row_index'], name='code_search_languag_9d45ef_idx'),
        ),
        migrations.AddIndex(
            model_name='codedocument',
            index=models.Index(fields=['code_hash'], name='code_search_code_ha_732501_idx'),
        ),
    ]
