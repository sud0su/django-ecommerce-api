"""
USE:
    photo = models.ImageField(
        _(u'Rating photo'), upload_to=path_and_rename('ratings/pictures'),
        blank=True)
"""

import os
from uuid import uuid4

def path_and_rename(path):
    """
        get the filename of a uploaded image and change it to models PK or a random if model is not saved
    """
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper