import copy
import logging

from fastutils import cipherutils
from fastutils import strutils

from django.db import models
from django.conf import settings
from django.utils.datastructures import OrderedSet


logger = logging.getLogger(__name__)


class SafeFieldMixinBase(object):

    def __init__(self, *args, used_ciphers=None, cipher=None, cipher_class=None, cipher_kwargs=None, result_encoder=None, force_text=None, password=None, **kwargs):
        self.used_ciphers = used_ciphers or []
        if cipher:
            self.cipher = cipher
        else:
            password = password or settings.SECRET_KEY
            cipher_class = cipher_class or cipherutils.MysqlAesCipher
            cipher_kwargs = cipher_kwargs and copy.deepcopy(cipher_kwargs) or {}
            if result_encoder:
                cipher_kwargs["result_encoder"] = result_encoder
            else:
                if cipher_class.default_result_encoder is None:
                    cipher_kwargs["result_encoder"] = cipherutils.HexlifyEncoder()
            if force_text is None:
                cipher_kwargs["force_text"] = True
            else:
                cipher_kwargs["force_text"] = force_text
            self.cipher = cipher_class(password=password, **cipher_kwargs)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        for cipher in [self.cipher] + self.used_ciphers:
            try:
                value = cipher.decrypt(value)
                return value
            except Exception:
                logger.warn("Warn: {0} has old cipher encrypted data.".format(self))
        logger.error("Error: SafeCharField.from_db_value decrypt failed: value={}".format(value))
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.cipher.encrypt(value)
        return strutils.force_text(value)

    def get_lookup(self, lookup_name):
        base_lookup = super().get_lookup(lookup_name)
        return type(base_lookup.__name__, (base_lookup,), {"get_db_prep_lookup": self.get_db_prep_lookup})

    def get_db_prep_lookup(self, value, connection):
        if callable(value):
            value = value()
        if isinstance(value, OrderedSet):
            value2 = OrderedSet()
            for item in value:
                value2.add(self.cipher.encrypt(item))
            value = value2
        else:
            value = [self.cipher.encrypt(value)]
        result = ('%s', value)
        return result

class SafeStringFieldMixin(SafeFieldMixinBase):
    pass

class SafeCharField(SafeStringFieldMixin, models.CharField):
    pass

class SafeTextField(SafeStringFieldMixin, models.TextField):
    pass

class SafeEmailField(SafeStringFieldMixin, models.EmailField):
    pass

class SafeURLField(SafeStringFieldMixin, models.URLField):
    pass

class SafeGenericIPAddressField(SafeStringFieldMixin, models.GenericIPAddressField):

    def __init__(self, *args, max_length=None, **kwargs):
        max_length = max_length or 128
        super().__init__(*args, max_length=max_length, **kwargs)
        self.max_length = max_length

    def get_internal_type(self):
        return "CharField"


class SafeIntegerField(SafeFieldMixinBase, models.IntegerField):

    def __init__(self, *args, cipher_class=None, result_encoder=None, force_text=None, **kwargs):
        cipher_class = cipher_class or cipherutils.IvCipher
        result_encoder = result_encoder or cipherutils.RawDataEncoder()
        super().__init__(*args, cipher_class=cipher_class, result_encoder=result_encoder, force_text=False, **kwargs)

class SafeNumbericFieldMixinBase(SafeFieldMixinBase):

    def __init__(self, *args, result_encoder=None, **kwargs):
        result_encoder = result_encoder or cipherutils.RawDataEncoder()
        super().__init__(*args, result_encoder=result_encoder, **kwargs)

    def force_numberic(self, value):
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        if isinstance(value, str):
            if "." in value:
                return float(value)
            else:
                return int(value)
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.force_numberic(value)
        result = super().get_db_prep_value(value, connection, prepared)
        return result

class SafeBigIntegerField(SafeNumbericFieldMixinBase, models.CharField):

    def __init__(self, *args, max_length=None, cipher_class=None, cipher_kwargs=None, force_text=None, **kwargs):
        max_length = max_length or 128
        cipher_class = cipher_class or cipherutils.IvfCipher
        cipher_kwargs = cipher_kwargs and copy.deepcopy(cipher_kwargs) or {}
        cipher_kwargs["float_digits"] = 0
        super().__init__(*args, max_length=max_length, cipher_class=cipher_class, cipher_kwargs=cipher_kwargs, force_text=False, **kwargs)

class SafeFloatField(SafeNumbericFieldMixinBase, models.CharField):

    def __init__(self, *args, max_length=None, cipher_class=None, force_text=None, **kwargs):
        max_length = max_length or 128
        cipher_class = cipher_class or cipherutils.IvfCipher
        super().__init__(*args, max_length=max_length, cipher_class=cipher_class, force_text=False, **kwargs)
