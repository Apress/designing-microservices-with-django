from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    slack_channel = models.CharField(max_length=128)


class Owner(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    email = models.EmailField()


class Service(models.Model):
    name = models.CharField(max_length=128)
    owners = models.ManyToManyField(Team)
    repository = models.URLField()
    healthcheck_url = models.URLField()
    swagger_file_location = models.URLField()
    asyncapi_file_location = models.URLField()
