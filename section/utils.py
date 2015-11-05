from django.shortcuts import get_object_or_404

from section import models


def release_section(section_id):
    section = get_object_or_404(models.Section, id=section_id)

    section.editing = None
    section.save_no_notification()
