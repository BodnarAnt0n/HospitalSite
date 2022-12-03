from django.db import models
from django.contrib.auth.models import User


class EmployeePosition(models.Model):

    """ Модель должности пользователя """

    title = models.CharField(verbose_name='Должность', max_length=250)

    def __str__(self):
        return f'{self.title}'


class HospitalDepartment(models.Model):

    """ Модель отделений больницы """

    title = models.CharField(verbose_name='Наименование отделения', max_length=250)

    def __str__(self):
        return f'Отделение: {self.title}'


class HospitalRoom(models.Model):

    """ Модель больничной палаты """

    department = models.ForeignKey(
        HospitalDepartment, on_delete=models.RESTRICT,
        related_name='room', related_query_name='room', verbose_name='Отделение'
    )
    number = models.CharField(verbose_name='Номер палаты', max_length=10)

    def __str__(self):
        return f'Палата № {self.number}'


class Employee(models.Model):

    """ Расширенная модель пользователя """

    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    date_birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    # Отделение сотрудника
    departments = models.ForeignKey(
        HospitalDepartment, on_delete=models.RESTRICT,
        related_name='employee', related_query_name='employee',
        verbose_name='Отделение', blank=True, null=True
    )

    # Больничные палаты сотрудника
    hospital_room = models.ManyToManyField(HospitalRoom)

    # Должность сотрудника
    position = models.ForeignKey(
        EmployeePosition, on_delete=models.RESTRICT,
        related_name='employee', related_query_name='employee',
        verbose_name='Должность', blank=True, null=True
    )

    def __str__(self):
        return f'Сотрудник: {self.user}'


class EmployeeBiography(models.Model):

    """ Биография сотрудника """

    employee = models.OneToOneField(Employee, on_delete=models.RESTRICT)
    biography = models.TextField(verbose_name='Биография')
    is_true = models.BooleanField(verbose_name='Флаг подтверждения', default=False)


class EmployeeEducation(models.Model):

    """ Модель образования сотрудника """

    employee = models.ForeignKey(
        Employee, on_delete=models.RESTRICT,
        related_name='education', related_query_name='education',
    )
    place_of_study = models.CharField(verbose_name='Место учебы', max_length=250)
    year_of_the_beginning = models.DateField(verbose_name='Год начала обучения')
    year_of_completion = models.DateField(verbose_name='Год завершения обучения')
    is_true = models.BooleanField(verbose_name='Флаг подтверждения', default=False)


class EmployeeWorkExperience(models.Model):

    """ Модель рабочего стажа сотрудника """

    employee = models.ForeignKey(
        Employee, on_delete=models.RESTRICT,
        related_name='work', related_query_name='work',
    )
    place_of_work = models.CharField(verbose_name='Место работы', max_length=250)
    year_of_the_beginning = models.DateField(verbose_name='Год начала работы')
    year_of_completion = models.DateField(verbose_name='Год завершения работы')
    is_true = models.BooleanField(verbose_name='Флаг подтверждения', default=False)


class EmployeeAchievement(models.Model):

    """ Модель достижений и научных работ сотрудника """

    employee = models.ForeignKey(
        Employee, on_delete=models.RESTRICT,
        related_name='achievement', related_query_name='achievement',
    )
    description = models.CharField(verbose_name='Описание достижения', max_length=500)
    is_true = models.BooleanField(verbose_name='Флаг подтверждения', default=False)
