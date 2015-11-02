from django.shortcuts import get_object_or_404
from cmdocapp import models


def sync_sec_cancel(section_id):
    section = get_object_or_404(models.Section, id=section_id)

    section.editing = None
    section.save_no_notification()
