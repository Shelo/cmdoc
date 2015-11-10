from django.db import models
from django.contrib.auth.models import User

import section.models


class Document(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='document_owner')
    users = models.ManyToManyField(User)
    serial = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def users_count(self):
        return len(self.users.all()) + 1

    def has_user(self, user):
        return self.owner == user or user in self.users.all()

    def save(self, *args, **kwargs):
        is_new = bool(self.pk is None)
        self.serial += 1
        super(Document, self).save(*args, **kwargs)

        if is_new:
            print 1
            # notification for new document created.
            notification = ChangeNotification(
                document=self,
                modifier=self.owner,
                message=self.description)
            notification.save()

    def parsed_content(self):
        """
        Parse the content of every section in the document.

        :return: all sections parsed with the tokens.
        """
        sections = self.section_set.all()
        tokens = self.token_set.all()

        parsed_sections = []
        for sec in sections:
            sec.parse_content(tokens)
            parsed_sections.append(sec)

        return parsed_sections


class ChangeNotification(models.Model):
    document = models.ForeignKey(Document)
    section = models.ForeignKey('section.Section', null=True)
    modify_time = models.DateTimeField(auto_now_add=True)
    modifier = models.ForeignKey(User)
    message = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-modify_time']


class Message(models.Model):
    document = models.ForeignKey(Document)
    author = models.ForeignKey(User)
    content = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']
