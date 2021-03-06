"""
Definition of the
:class:`~django_dicom.models.values.signed_short.SignedShort` model.
"""


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_dicom.models.values.data_element_value import DataElementValue

#: Minimal *SignedShort* value.
MIN_VALUE = -(2 ** 15)
#: Maximal *SignedShort* value.
MAX_VALUE = 2 ** 15 - 1


class SignedShort(DataElementValue):
    """
    A :class:`~django.db.models.Model` representing a single *SignedShort*
    data element value.
    """

    #: Overrides
    #: :attr:`~django_dicom.models.values.data_element_value.DataElementValue.value`
    #: to assign a :class:`~django.db.models.IntegerField`.
    value = models.IntegerField(
        validators=[
            MaxValueValidator(MAX_VALUE),
            MinValueValidator(MIN_VALUE),
        ],
        blank=True,
        null=True,
    )

    #: Overrides
    #: :attr:`~django_dicom.models.values.data_element_value.DataElementValue.raw`
    #: to assign a :class:`~django.db.models.IntegerField`.
    raw = models.IntegerField(
        validators=[
            MaxValueValidator(MAX_VALUE),
            MinValueValidator(MIN_VALUE),
        ],
        blank=True,
        null=True,
    )


# flake8: noqa: E501
