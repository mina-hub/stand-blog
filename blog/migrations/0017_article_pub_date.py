# Generated by Django 5.0.6 on 2024-07-08 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0016_alter_comment_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 8, 10, 22, 22, 576908, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]