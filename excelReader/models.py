# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Files(models.Model):
	xlsFile = models.FileField(upload_to = 'files/')

class FileContents(models.Model):
	row1 = models.TextField()
	row2 = models.TextField()
