from django.db import models
from backend_functions.universal_values import *


# backend database (already filed.)
class CLASS_COURSES_MAPPING(models.Model):
    # format "class:section:offeringyear"
    unique_id = models.CharField(
        max_length=CLS_COURSE_MAPPING_UNIQUE_ID_LENGTH)
    # an array represented as string, where, each element is a course_id which is nothing but courseapp.AVALIABLE_COURSES course_id.
    course_id_array = models.CharField(max_length=COURSE_ID_ARRAY_MAX_LENGTH)

    def __str__(self) -> str:
        return self.unique_id

    class Meta:
        ordering = ['unique_id']


"""unique_id = "06AS2020"
course_id = "MA06AS2020 SC06AS2020 SS06AS2020 HI06AS20202 EN06AS2020"
"""


class AVAILABLE_COURSES(models.Model):
    # format, "sc-cl-cs-ofyr" subject_code:class:section:offeringyear
    course_id = models.CharField(max_length=COURSE_ID_LENGTH)
    course_instructor = models.OneToOneField(
        "loginapp.TEACHER_CODE_MAPPING", on_delete=models.CASCADE)
    course_name = models.CharField(max_length=COURSE_NAME_LENGTH)
    # Needs to be updated whenever new lecture added # Backend handlingI
    lecture_series_number = models.IntegerField(default=0)
    test_series_number = models.IntegerField(default=0)  # Same.
    forum_series_number = models.IntegerField(default=0)  # Same.

    def __str__(self):
        return self.course_id

    class Meta:
        ordering = ['course_id']
