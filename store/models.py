from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class JSONField(models.TextField):

    def to_python(self, value):
        if value == "":
            return None
        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value
    

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    bookmarks = JSONField(null=True, blank=True,default={"total":0,"books":[]})
