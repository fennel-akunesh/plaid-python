"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.385.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.ach_class import ACHClass
    from plaid.model.recurring_transfer import RecurringTransfer
    from plaid.model.transfer_network import TransferNetwork
    from plaid.model.transfer_recurring_schedule import TransferRecurringSchedule
    from plaid.model.transfer_recurring_status import TransferRecurringStatus
    from plaid.model.transfer_type import TransferType
    from plaid.model.transfer_user_in_response import TransferUserInResponse
    globals()['ACHClass'] = ACHClass
    globals()['RecurringTransfer'] = RecurringTransfer
    globals()['TransferNetwork'] = TransferNetwork
    globals()['TransferRecurringSchedule'] = TransferRecurringSchedule
    globals()['TransferRecurringStatus'] = TransferRecurringStatus
    globals()['TransferType'] = TransferType
    globals()['TransferUserInResponse'] = TransferUserInResponse


class RecurringTransferNullable(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'recurring_transfer_id': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'next_origination_date': (date,),  # noqa: E501
            'type': (TransferType,),  # noqa: E501
            'amount': (str,),  # noqa: E501
            'status': (TransferRecurringStatus,),  # noqa: E501
            'network': (TransferNetwork,),  # noqa: E501
            'origination_account_id': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'funding_account_id': (str,),  # noqa: E501
            'iso_currency_code': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'transfer_ids': ([str],),  # noqa: E501
            'user': (TransferUserInResponse,),  # noqa: E501
            'schedule': (TransferRecurringSchedule,),  # noqa: E501
            'test_clock_id': (str, none_type,),  # noqa: E501
            'ach_class': (ACHClass,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'recurring_transfer_id': 'recurring_transfer_id',  # noqa: E501
        'created': 'created',  # noqa: E501
        'next_origination_date': 'next_origination_date',  # noqa: E501
        'type': 'type',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'status': 'status',  # noqa: E501
        'network': 'network',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'funding_account_id': 'funding_account_id',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'description': 'description',  # noqa: E501
        'transfer_ids': 'transfer_ids',  # noqa: E501
        'user': 'user',  # noqa: E501
        'schedule': 'schedule',  # noqa: E501
        'test_clock_id': 'test_clock_id',  # noqa: E501
        'ach_class': 'ach_class',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """RecurringTransferNullable - a model defined in OpenAPI

        Keyword Args:
            recurring_transfer_id (str): Plaid’s unique identifier for a recurring transfer.
            created (datetime): The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
            next_origination_date (date): A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment.
            type (TransferType):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").
            status (TransferRecurringStatus):
            network (TransferNetwork):
            origination_account_id (str): Plaid’s unique identifier for the origination account that was used for this transfer.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            funding_account_id (str): The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited.
            iso_currency_code (str): The currency of the transfer amount, e.g. \"USD\"
            description (str): The description of the recurring transfer.
            transfer_ids ([str]):
            user (TransferUserInResponse):
            schedule (TransferRecurringSchedule):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock.. [optional]  # noqa: E501
            ach_class (ACHClass): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """RecurringTransferNullable - a model defined in OpenAPI

        Keyword Args:
            recurring_transfer_id (str): Plaid’s unique identifier for a recurring transfer.
            created (datetime): The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
            next_origination_date (date): A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment.
            type (TransferType):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").
            status (TransferRecurringStatus):
            network (TransferNetwork):
            origination_account_id (str): Plaid’s unique identifier for the origination account that was used for this transfer.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            funding_account_id (str): The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited.
            iso_currency_code (str): The currency of the transfer amount, e.g. \"USD\"
            description (str): The description of the recurring transfer.
            transfer_ids ([str]):
            user (TransferUserInResponse):
            schedule (TransferRecurringSchedule):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock.. [optional]  # noqa: E501
            ach_class (ACHClass): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              RecurringTransfer,
          ],
          'oneOf': [
          ],
        }
