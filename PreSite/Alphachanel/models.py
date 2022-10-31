from django.db import models

class Advertisment(models.Model):
    title = models.CharField(max_length=1000, db_index=True)
    description = models.CharField(max_length=1000, default='', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='кол-во просмотров', default=0)
    status = models.ForeignKey('StatusAdv', default=None, null=True, on_delete=models.CASCADE, verbose_name='статус')

    def __str__(self):
        return self.title

    class Meta:                 #Этот класс для доп. задач по БД
        db_table = 'advertisement'          #Эта инструкция меняет название всей БД
        ordering = ['title']                #Эта инструкция сортирует по алфавиту

class Equipment(models.Model):
    title = models.CharField(max_length=1000)
    price = models.IntegerField()


class StatusAdv(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.name
