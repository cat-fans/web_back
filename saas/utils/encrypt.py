import uuid
from hashlib import md5 as md

from django.conf import settings


def md5(string):
    """ MD5加密 """
    hash_object = md(settings.SECRET_KEY.encode('utf-8'))
    hash_object.update(string.encode('utf-8'))
    return hash_object.hexdigest()


def uid(string):
    data = "{}-{}".format(str(uuid.uuid4()), string)
    return md5(data)
