"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.514.1
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
    from plaid.model.transfer_authorization_device import TransferAuthorizationDevice
    from plaid.model.transfer_authorization_idempotency_key import TransferAuthorizationIdempotencyKey
    from plaid.model.transfer_authorization_user_in_request import TransferAuthorizationUserInRequest
    from plaid.model.transfer_network import TransferNetwork
    from plaid.model.transfer_type import TransferType
    from plaid.model.transfer_wire_details import TransferWireDetails
    globals()['ACHClass'] = ACHClass
    globals()['TransferAuthorizationDevice'] = TransferAuthorizationDevice
    globals()['TransferAuthorizationIdempotencyKey'] = TransferAuthorizationIdempotencyKey
    globals()['TransferAuthorizationUserInRequest'] = TransferAuthorizationUserInRequest
    globals()['TransferNetwork'] = TransferNetwork
    globals()['TransferType'] = TransferType
    globals()['TransferWireDetails'] = TransferWireDetails


class TransferAuthorizationCreateRequest(ModelNormal):
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
            'access_token': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'type': (TransferType,),  # noqa: E501
            'network': (TransferNetwork,),  # noqa: E501
            'amount': (str,),  # noqa: E501
            'user': (TransferAuthorizationUserInRequest,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'funding_account_id': (str, none_type,),  # noqa: E501
            'payment_profile_token': (str,),  # noqa: E501
            'ach_class': (ACHClass,),  # noqa: E501
            'wire_details': (TransferWireDetails,),  # noqa: E501
            'device': (TransferAuthorizationDevice,),  # noqa: E501
            'origination_account_id': (str,),  # noqa: E501
            'iso_currency_code': (str,),  # noqa: E501
            'idempotency_key': (TransferAuthorizationIdempotencyKey,),  # noqa: E501
            'user_present': (bool, none_type,),  # noqa: E501
            'with_guarantee': (bool, none_type,),  # noqa: E501
            'beacon_session_id': (str, none_type,),  # noqa: E501
            'originator_client_id': (str, none_type,),  # noqa: E501
            'credit_funds_source': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'test_clock_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'access_token': 'access_token',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'network': 'network',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'user': 'user',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'funding_account_id': 'funding_account_id',  # noqa: E501
        'payment_profile_token': 'payment_profile_token',  # noqa: E501
        'ach_class': 'ach_class',  # noqa: E501
        'wire_details': 'wire_details',  # noqa: E501
        'device': 'device',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'user_present': 'user_present',  # noqa: E501
        'with_guarantee': 'with_guarantee',  # noqa: E501
        'beacon_session_id': 'beacon_session_id',  # noqa: E501
        'originator_client_id': 'originator_client_id',  # noqa: E501
        'credit_funds_source': 'credit_funds_source',  # noqa: E501
        'test_clock_id': 'test_clock_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, access_token, account_id, type, network, amount, user, *args, **kwargs):  # noqa: E501
        """TransferAuthorizationCreateRequest - a model defined in OpenAPI

        Args:
            access_token (str): The Plaid `access_token` for the account that will be debited or credited.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            type (TransferType):
            network (TransferNetwork):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.
            user (TransferAuthorizationUserInRequest):

        Keyword Args:
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
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            funding_account_id (str, none_type): Specify the account used to fund the transfer. Should be specified if using legacy funding methods only. If using Plaid Ledger, leave this field blank. Customers can find a list of `funding_account_id`s in the Accounts page of your Plaid Dashboard, under the \"Account ID\" column. If this field is left blank and you are using legacy funding methods, this will default to the default `funding_account_id` specified during onboarding. Otherwise, Plaid Ledger will be used.. [optional]  # noqa: E501
            payment_profile_token (str): The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using `access_token`.. [optional]  # noqa: E501
            ach_class (ACHClass): [optional]  # noqa: E501
            wire_details (TransferWireDetails): [optional]  # noqa: E501
            device (TransferAuthorizationDevice): [optional]  # noqa: E501
            origination_account_id (str): Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.. [optional]  # noqa: E501
            iso_currency_code (str): The currency of the transfer amount. The default value is \"USD\".. [optional]  # noqa: E501
            idempotency_key (TransferAuthorizationIdempotencyKey): [optional]  # noqa: E501
            user_present (bool, none_type): If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`. This field is not currently used and is present to support planned future functionality.. [optional]  # noqa: E501
            with_guarantee (bool, none_type): If set to `false`, Plaid will not offer a `guarantee_decision` for this request (Guarantee customers only).. [optional] if omitted the server will use the default value of True  # noqa: E501
            beacon_session_id (str, none_type): The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage.. [optional]  # noqa: E501
            originator_client_id (str, none_type): The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a [Platform customer](https://plaid.com/docs/transfer/application/#originators-vs-platforms).. [optional]  # noqa: E501
            credit_funds_source (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `authorization` is created at the `virtual_time` on the provided test clock.. [optional]  # noqa: E501
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

        self.access_token = access_token
        self.account_id = account_id
        self.type = type
        self.network = network
        self.amount = amount
        self.user = user
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, access_token, account_id, type, network, amount, user, *args, **kwargs):  # noqa: E501
        """TransferAuthorizationCreateRequest - a model defined in OpenAPI

        Args:
            access_token (str): The Plaid `access_token` for the account that will be debited or credited.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            type (TransferType):
            network (TransferNetwork):
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.
            user (TransferAuthorizationUserInRequest):

        Keyword Args:
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
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            funding_account_id (str, none_type): Specify the account used to fund the transfer. Should be specified if using legacy funding methods only. If using Plaid Ledger, leave this field blank. Customers can find a list of `funding_account_id`s in the Accounts page of your Plaid Dashboard, under the \"Account ID\" column. If this field is left blank and you are using legacy funding methods, this will default to the default `funding_account_id` specified during onboarding. Otherwise, Plaid Ledger will be used.. [optional]  # noqa: E501
            payment_profile_token (str): The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using `access_token`.. [optional]  # noqa: E501
            ach_class (ACHClass): [optional]  # noqa: E501
            wire_details (TransferWireDetails): [optional]  # noqa: E501
            device (TransferAuthorizationDevice): [optional]  # noqa: E501
            origination_account_id (str): Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.. [optional]  # noqa: E501
            iso_currency_code (str): The currency of the transfer amount. The default value is \"USD\".. [optional]  # noqa: E501
            idempotency_key (TransferAuthorizationIdempotencyKey): [optional]  # noqa: E501
            user_present (bool, none_type): If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`. This field is not currently used and is present to support planned future functionality.. [optional]  # noqa: E501
            with_guarantee (bool, none_type): If set to `false`, Plaid will not offer a `guarantee_decision` for this request (Guarantee customers only).. [optional] if omitted the server will use the default value of True  # noqa: E501
            beacon_session_id (str, none_type): The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage.. [optional]  # noqa: E501
            originator_client_id (str, none_type): The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a [Platform customer](https://plaid.com/docs/transfer/application/#originators-vs-platforms).. [optional]  # noqa: E501
            credit_funds_source (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `authorization` is created at the `virtual_time` on the provided test clock.. [optional]  # noqa: E501
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

        self.access_token = access_token
        self.account_id = account_id
        self.type = type
        self.network = network
        self.amount = amount
        self.user = user
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
