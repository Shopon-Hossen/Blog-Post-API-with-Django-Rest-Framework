# Generated by Django 5.1.6 on 2025-02-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='tag.tag'),
        ),
    ]
