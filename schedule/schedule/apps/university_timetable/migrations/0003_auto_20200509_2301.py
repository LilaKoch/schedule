# Generated by Django 3.0.3 on 2020-05-09 23:01

from django.db import migrations, models
import university_timetable.models


class Migration(migrations.Migration):

    dependencies = [
        ('university_timetable', '0002_auto_20200508_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='DayOfWeek',
            field=models.CharField(choices=[('ср', 'Среда'), ('вт', 'Вторник'), ('пят', 'Пятница'), ('вос', 'Воскресенье'), ('чет', 'Четверг'), ('суб', 'Суббота'), ('пон', 'Понедельник')], max_length=11),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='TypeOfWeek',
            field=models.CharField(choices=[('чн', 'четная'), ('нч', 'нечетная')], max_length=2),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='IntermediateCertificationForm',
            field=models.CharField(choices=[('з', 'зачет'), ('экз', 'экзамен'), ('зо', 'зачет с оценкой')], db_column='Форма промежуточной аттестации', default='', max_length=20, verbose_name='Форма промежуточной аттестации'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='Name',
            field=models.CharField(db_column='Название дисциплины', max_length=60, validators=[university_timetable.models.validate_string], verbose_name='Название дисциплины'),
        ),
        migrations.AlterField(
            model_name='groupininstitute',
            name='FormOfTraining',
            field=models.CharField(choices=[('оз', 'очно-заочная'), ('з', 'заочная'), ('о', 'очная')], db_column='Форма обучения', max_length=12),
        ),
        migrations.AlterField(
            model_name='groupininstitute',
            name='GroupName',
            field=models.CharField(max_length=15, validators=[university_timetable.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='groupininstitute',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Код группы'),
        ),
        migrations.AlterField(
            model_name='groupininstitute',
            name='Institute',
            field=models.CharField(db_column='Институт', max_length=60, validators=[university_timetable.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='groupininstitute',
            name='Specialty',
            field=models.CharField(db_column='Специальность', max_length=60, validators=[university_timetable.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='PhoneNumber',
            field=models.CharField(db_column='Номер телефона', max_length=11, unique=True, validators=[university_timetable.models.validate_phone]),
        ),
    ]
