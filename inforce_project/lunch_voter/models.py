from django.db import models


class User(models.Model):
    role = models.CharField(max_length=255)  # employee, admin, manager(for particular restaurant)

    class Meta:
        db_table = 'lunch_voter_schema."User"'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='User_pkey')
        ]

    def __str__(self):
        return self.role


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='restaurants')

    class Meta:
        db_table = 'lunch_voter_schema."Restaurant"'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='Restaurant_pkey')
        ]

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu = models.CharField(max_length=10000)
    date_created = models.DateField()
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')

    class Meta:
        db_table = 'lunch_voter_schema."Menu"'
        constraints = [
            models.UniqueConstraint(fields=['id'], name='Menu_pkey')
        ]

    def __str__(self):
        return self.menu
