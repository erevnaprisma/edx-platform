# pylint: disable=abstract-method
"""
Progress Tab Serializers
"""

from rest_framework import serializers
from lms.djangoapps.course_home_api.outline.v1.serializers import CourseBlockSerializer


class ProgressTabSerializer(serializers.Serializer):
    """
    Serializer
    """
    course_blocks = CourseBlockSerializer()
    enrollment_mode = serializers.CharField()
