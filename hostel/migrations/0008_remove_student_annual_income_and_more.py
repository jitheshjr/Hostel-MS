# Generated by Django 5.0.6 on 2024-06-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_attendancedate_month_attendancedate_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='annual_income',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_occupation',
        ),
        migrations.RemoveField(
            model_name='trash',
            name='annual_income',
        ),
        migrations.RemoveField(
            model_name='trash',
            name='parent_occupation',
        ),
        migrations.AddField(
            model_name='messbill',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1000000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendancedate',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10),
        ),
    ]
