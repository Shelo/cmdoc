from django.contrib.auth.models import User
from django.db import models

import edit.models

class Section(models.Model):
    document = models.ForeignKey('edit.Document')
    content = models.TextField()
    owner = models.ForeignKey(User, related_name='section_owner')
    position = models.IntegerField(default=0)

    # modification related fields.
    last_modified = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=256, blank=True)
    modifier = models.ForeignKey(User, null=True)

    editing = models.ForeignKey(User, null=True, blank=True, related_name='editing_user')

    class Meta:
        ordering = ['-document_id', 'position']

    def document_title(self):
        return self.document.title

    def short_content(self):
        return self.content if len(self.content) < 50 else self.content[:50]

    def __str__(self):
        return self.short_content()

    def save(self, *args, **kwargs):
        self.save_no_notification(*args, **kwargs)

        # when saving a section a change notification has to be registered.
        notification = edit.models.ChangeNotification(
            document=self.document,
            section=self,
            modifier=self.modifier,
            message=self.message
        )

        notification.save()

    def save_no_notification(self, *args, **kwargs):
        self.document.save()
        super(Section, self).save(*args, **kwargs)
