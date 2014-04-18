from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
import sys

register=template.Library()
import re

@register.filter
@stringfilter
def highlight(text, filter):
    filter="|".join(filter.split())
    pattern=re.compile(r"(?P<filter>%s)" % filter, re.IGNORECASE)
    return mark_safe(re.sub(pattern, r"<b><span class='highlight'>\g<filter></span></b>", text))

register.filter('highlight', highlight)
