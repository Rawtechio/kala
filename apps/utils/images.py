# -*- coding: utf-8 -*-

from datetime import date


def logo_upload_path(instance, filename):
    """
    Logos are uploaded according to date and associated org/place
    """

    today = date.today()

    return "logos/{y}/{m}/{d}/{slug}-{pk}/{filename}".format(
        y=today.year,
        m=today.month,
        d=today.day,
        slug=instance.slug,
        pk=instance.pk,
        filename=filename
    )
