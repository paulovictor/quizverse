# Generated migration for adding discount_percentage field to Product model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_add_badge_translations'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.IntegerField(default=0, help_text='Desconto em porcentagem (0-100). Use 0 para sem desconto.', verbose_name='Porcentagem de Desconto'),
        ),
    ]

