import os


def get_profile_picture_path(instance, filename):
    return os.path.join('cv', instance.slug, filename)
