from django.db.models.fields import DateTimeField
from Noting.settings import TIME_ZONE
from django.db import models
from django.contrib.auth.models import User

class NotingModel(models.Model):
	noteID = models.IntegerField(primary_key=True)
	title = models.TextField(null=True)
	description = models.TextField(blank=True, null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def __str__(self):
		ret = str(self.noteID) + "} " + str(self.author.username) + ": " + str(self.title)
		return str(ret)