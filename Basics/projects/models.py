import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    #owner
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #feature_image
    demo_link = models.CharField(max_length=1000,null=True,blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag',blank=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('Up','up'),
        ('Down','down'),
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=50,choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name