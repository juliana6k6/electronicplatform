from django.db import models


# Create your models here.
class PlatformUnit:
    """ Модель, описывающая объект сети """
    TYPE_CHOICES = (
        ("завод", "завод"),
        ("розница", "розничная сеть"),
        ("ИП", "индивидуальный предприниматель"),
    )
    LEVEL_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
    )

    name = models.CharField(max_length=300, verbose_name='Название объекта сети', help_text="Укажите название")
    type = models.CharField(choices=TYPE_CHOICES, default="завод", verbose_name='Тип звена сети',
                            help_text="Укажите тип звена сети", )
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name='Уровень в иерархии поставок',
                                help_text="Укажите уровень в иерархии поставок")

    email = models.EmailField(unique=True, verbose_name='email',  blank=True, null=True,
                              help_text="Укажите электронную почту")
    country = models.CharField(max_length=100, verbose_name='Страна',  blank=True, null=True,
                               help_text="Укажите страну",)
    city = models.CharField(max_length=100, verbose_name='Город',  blank=True, null=True, help_text="Укажите город")
    street = models.CharField(max_length=100, verbose_name='Улица',  blank=True, null=True, help_text="Укажите улицу")
    house_number = models.CharField(max_length=15, verbose_name='Номер дома',  blank=True, null=True,
                                    help_text="Укажите номер дома")

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Cсылка на поставщика',
                                 blank=True, null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                               verbose_name='Задолженность перед поставщиком', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name} - {self.type}'

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'


class Product(models.Model):
    """ Модель, описывающая продукт """
    name = models.CharField(max_length=150, verbose_name='название', help_text="Укажите название")
    model = models.CharField(max_length=150, verbose_name='модель', blank=True, null=True, help_text="Укажите модель")
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', blank=True, null=True,
                                    help_text="Укажите дату выхода продукта на рынок")
    network_unit = models.ForeignKey("PlatformUnit", on_delete=models.CASCADE, verbose_name='Объект сети')

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
