from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()

class Publisher(models.Model):
    STATUS_CHOICE = [
        (True, 'active'),
        (False, 'not_active')
    ]
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    sold_books = models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(choices=STATUS_CHOICE, default=False)

    def __str__(self):
        return f'{self.id}.  {self.name}, ({self.city}, {self.country}'

class Author(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField()
    biography = models.TextField()
    phone_number = models.CharField(max_length=16, blank=True)      #Чекнуть, что такое bldnk=True
    personal_page = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    university = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}.  {self.name}'

class Book(models.Model):
    STATUS_CHOISES= [
        ('D', 'Draft'),
        ('R', 'Review'),
        ('P', 'published')
    ]                                   #Константа, отвечающая за варианты статуса
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default='D')        #Выбор статуса 'choices=' - варианты

    def __str__(self):
        return self.title