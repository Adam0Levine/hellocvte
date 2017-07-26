# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkuser',
            name='email',
            field=models.EmailField(verbose_name='邮箱', max_length=254, blank=True),
        ),
    ]
