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



class PaymentInitiationPaymentStatus(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'INPUT_NEEDED': "PAYMENT_STATUS_INPUT_NEEDED",
            'PROCESSING': "PAYMENT_STATUS_PROCESSING",
            'INITIATED': "PAYMENT_STATUS_INITIATED",
            'COMPLETED': "PAYMENT_STATUS_COMPLETED",
            'INSUFFICIENT_FUNDS': "PAYMENT_STATUS_INSUFFICIENT_FUNDS",
            'FAILED': "PAYMENT_STATUS_FAILED",
            'BLOCKED': "PAYMENT_STATUS_BLOCKED",
            'UNKNOWN': "PAYMENT_STATUS_UNKNOWN",
            'EXECUTED': "PAYMENT_STATUS_EXECUTED",
            'SETTLED': "PAYMENT_STATUS_SETTLED",
            'AUTHORISING': "PAYMENT_STATUS_AUTHORISING",
            'CANCELLED': "PAYMENT_STATUS_CANCELLED",
            'ESTABLISHED': "PAYMENT_STATUS_ESTABLISHED",
            'REJECTED': "PAYMENT_STATUS_REJECTED",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """PaymentInitiationPaymentStatus - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): The status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.  `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.  `PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.  `PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.  `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).  `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.  Deprecated: These statuses will be removed in a future release.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.., must be one of ["PAYMENT_STATUS_INPUT_NEEDED", "PAYMENT_STATUS_PROCESSING", "PAYMENT_STATUS_INITIATED", "PAYMENT_STATUS_COMPLETED", "PAYMENT_STATUS_INSUFFICIENT_FUNDS", "PAYMENT_STATUS_FAILED", "PAYMENT_STATUS_BLOCKED", "PAYMENT_STATUS_UNKNOWN", "PAYMENT_STATUS_EXECUTED", "PAYMENT_STATUS_SETTLED", "PAYMENT_STATUS_AUTHORISING", "PAYMENT_STATUS_CANCELLED", "PAYMENT_STATUS_ESTABLISHED", "PAYMENT_STATUS_REJECTED", ]  # noqa: E501

        Keyword Args:
            value (str): The status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.  `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.  `PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.  `PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.  `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).  `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.  Deprecated: These statuses will be removed in a future release.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.., must be one of ["PAYMENT_STATUS_INPUT_NEEDED", "PAYMENT_STATUS_PROCESSING", "PAYMENT_STATUS_INITIATED", "PAYMENT_STATUS_COMPLETED", "PAYMENT_STATUS_INSUFFICIENT_FUNDS", "PAYMENT_STATUS_FAILED", "PAYMENT_STATUS_BLOCKED", "PAYMENT_STATUS_UNKNOWN", "PAYMENT_STATUS_EXECUTED", "PAYMENT_STATUS_SETTLED", "PAYMENT_STATUS_AUTHORISING", "PAYMENT_STATUS_CANCELLED", "PAYMENT_STATUS_ESTABLISHED", "PAYMENT_STATUS_REJECTED", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """PaymentInitiationPaymentStatus - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): The status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.  `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.  `PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.  `PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.  `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).  `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.  Deprecated: These statuses will be removed in a future release.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.., must be one of ["PAYMENT_STATUS_INPUT_NEEDED", "PAYMENT_STATUS_PROCESSING", "PAYMENT_STATUS_INITIATED", "PAYMENT_STATUS_COMPLETED", "PAYMENT_STATUS_INSUFFICIENT_FUNDS", "PAYMENT_STATUS_FAILED", "PAYMENT_STATUS_BLOCKED", "PAYMENT_STATUS_UNKNOWN", "PAYMENT_STATUS_EXECUTED", "PAYMENT_STATUS_SETTLED", "PAYMENT_STATUS_AUTHORISING", "PAYMENT_STATUS_CANCELLED", "PAYMENT_STATUS_ESTABLISHED", "PAYMENT_STATUS_REJECTED", ]  # noqa: E501

        Keyword Args:
            value (str): The status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.  `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.  `PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.  `PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.  `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).  `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.  Deprecated: These statuses will be removed in a future release.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.., must be one of ["PAYMENT_STATUS_INPUT_NEEDED", "PAYMENT_STATUS_PROCESSING", "PAYMENT_STATUS_INITIATED", "PAYMENT_STATUS_COMPLETED", "PAYMENT_STATUS_INSUFFICIENT_FUNDS", "PAYMENT_STATUS_FAILED", "PAYMENT_STATUS_BLOCKED", "PAYMENT_STATUS_UNKNOWN", "PAYMENT_STATUS_EXECUTED", "PAYMENT_STATUS_SETTLED", "PAYMENT_STATUS_AUTHORISING", "PAYMENT_STATUS_CANCELLED", "PAYMENT_STATUS_ESTABLISHED", "PAYMENT_STATUS_REJECTED", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
