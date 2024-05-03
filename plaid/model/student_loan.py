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
    from plaid.model.pslf_status import PSLFStatus
    from plaid.model.servicer_address_data import ServicerAddressData
    from plaid.model.student_loan_status import StudentLoanStatus
    from plaid.model.student_repayment_plan import StudentRepaymentPlan
    globals()['PSLFStatus'] = PSLFStatus
    globals()['ServicerAddressData'] = ServicerAddressData
    globals()['StudentLoanStatus'] = StudentLoanStatus
    globals()['StudentRepaymentPlan'] = StudentRepaymentPlan


class StudentLoan(ModelNormal):
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
            'account_id': (str, none_type,),  # noqa: E501
            'account_number': (str, none_type,),  # noqa: E501
            'disbursement_dates': ([date], none_type,),  # noqa: E501
            'expected_payoff_date': (date, none_type,),  # noqa: E501
            'guarantor': (str, none_type,),  # noqa: E501
            'interest_rate_percentage': (float,),  # noqa: E501
            'is_overdue': (bool, none_type,),  # noqa: E501
            'last_payment_amount': (float, none_type,),  # noqa: E501
            'last_payment_date': (date, none_type,),  # noqa: E501
            'last_statement_issue_date': (date, none_type,),  # noqa: E501
            'loan_name': (str, none_type,),  # noqa: E501
            'loan_status': (StudentLoanStatus,),  # noqa: E501
            'minimum_payment_amount': (float, none_type,),  # noqa: E501
            'next_payment_due_date': (date, none_type,),  # noqa: E501
            'origination_date': (date, none_type,),  # noqa: E501
            'origination_principal_amount': (float, none_type,),  # noqa: E501
            'outstanding_interest_amount': (float, none_type,),  # noqa: E501
            'payment_reference_number': (str, none_type,),  # noqa: E501
            'pslf_status': (PSLFStatus,),  # noqa: E501
            'repayment_plan': (StudentRepaymentPlan,),  # noqa: E501
            'sequence_number': (str, none_type,),  # noqa: E501
            'servicer_address': (ServicerAddressData,),  # noqa: E501
            'ytd_interest_paid': (float, none_type,),  # noqa: E501
            'ytd_principal_paid': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_id': 'account_id',  # noqa: E501
        'account_number': 'account_number',  # noqa: E501
        'disbursement_dates': 'disbursement_dates',  # noqa: E501
        'expected_payoff_date': 'expected_payoff_date',  # noqa: E501
        'guarantor': 'guarantor',  # noqa: E501
        'interest_rate_percentage': 'interest_rate_percentage',  # noqa: E501
        'is_overdue': 'is_overdue',  # noqa: E501
        'last_payment_amount': 'last_payment_amount',  # noqa: E501
        'last_payment_date': 'last_payment_date',  # noqa: E501
        'last_statement_issue_date': 'last_statement_issue_date',  # noqa: E501
        'loan_name': 'loan_name',  # noqa: E501
        'loan_status': 'loan_status',  # noqa: E501
        'minimum_payment_amount': 'minimum_payment_amount',  # noqa: E501
        'next_payment_due_date': 'next_payment_due_date',  # noqa: E501
        'origination_date': 'origination_date',  # noqa: E501
        'origination_principal_amount': 'origination_principal_amount',  # noqa: E501
        'outstanding_interest_amount': 'outstanding_interest_amount',  # noqa: E501
        'payment_reference_number': 'payment_reference_number',  # noqa: E501
        'pslf_status': 'pslf_status',  # noqa: E501
        'repayment_plan': 'repayment_plan',  # noqa: E501
        'sequence_number': 'sequence_number',  # noqa: E501
        'servicer_address': 'servicer_address',  # noqa: E501
        'ytd_interest_paid': 'ytd_interest_paid',  # noqa: E501
        'ytd_principal_paid': 'ytd_principal_paid',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, account_id, account_number, disbursement_dates, expected_payoff_date, guarantor, interest_rate_percentage, is_overdue, last_payment_amount, last_payment_date, last_statement_issue_date, loan_name, loan_status, minimum_payment_amount, next_payment_due_date, origination_date, origination_principal_amount, outstanding_interest_amount, payment_reference_number, pslf_status, repayment_plan, sequence_number, servicer_address, ytd_interest_paid, ytd_principal_paid, *args, **kwargs):  # noqa: E501
        """StudentLoan - a model defined in OpenAPI

        Args:
            account_id (str, none_type): The ID of the account that this liability belongs to. Each account can only contain one liability.
            account_number (str, none_type): The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number).
            disbursement_dates ([date], none_type): The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            expected_payoff_date (date, none_type): The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            guarantor (str, none_type): The guarantor of the student loan.
            interest_rate_percentage (float): The interest rate on the loan as a percentage.
            is_overdue (bool, none_type): `true` if a payment is currently overdue. Availability for this field is limited.
            last_payment_amount (float, none_type): The amount of the last payment.
            last_payment_date (date, none_type): The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            last_statement_issue_date (date, none_type): The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            loan_name (str, none_type): The type of loan, e.g., \"Consolidation Loans\".
            loan_status (StudentLoanStatus):
            minimum_payment_amount (float, none_type): The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`). Firstmark (`ins_116295` ), EdFinancial Services (`ins_116304`),  and Navient (`ins_116248`) will display as $0 if there is an autopay program in effect.
            next_payment_due_date (date, none_type): The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            origination_date (date, none_type): The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). 
            origination_principal_amount (float, none_type): The original principal balance of the loan.
            outstanding_interest_amount (float, none_type): The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`.
            payment_reference_number (str, none_type): The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match `account_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different.
            pslf_status (PSLFStatus):
            repayment_plan (StudentRepaymentPlan):
            sequence_number (str, none_type): The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available.
            servicer_address (ServicerAddressData):
            ytd_interest_paid (float, none_type): The year to date (YTD) interest paid. Availability for this field is limited.
            ytd_principal_paid (float, none_type): The year to date (YTD) principal paid. Availability for this field is limited.

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

        self.account_id = account_id
        self.account_number = account_number
        self.disbursement_dates = disbursement_dates
        self.expected_payoff_date = expected_payoff_date
        self.guarantor = guarantor
        self.interest_rate_percentage = interest_rate_percentage
        self.is_overdue = is_overdue
        self.last_payment_amount = last_payment_amount
        self.last_payment_date = last_payment_date
        self.last_statement_issue_date = last_statement_issue_date
        self.loan_name = loan_name
        self.loan_status = loan_status
        self.minimum_payment_amount = minimum_payment_amount
        self.next_payment_due_date = next_payment_due_date
        self.origination_date = origination_date
        self.origination_principal_amount = origination_principal_amount
        self.outstanding_interest_amount = outstanding_interest_amount
        self.payment_reference_number = payment_reference_number
        self.pslf_status = pslf_status
        self.repayment_plan = repayment_plan
        self.sequence_number = sequence_number
        self.servicer_address = servicer_address
        self.ytd_interest_paid = ytd_interest_paid
        self.ytd_principal_paid = ytd_principal_paid
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
    def __init__(self, account_id, account_number, disbursement_dates, expected_payoff_date, guarantor, interest_rate_percentage, is_overdue, last_payment_amount, last_payment_date, last_statement_issue_date, loan_name, loan_status, minimum_payment_amount, next_payment_due_date, origination_date, origination_principal_amount, outstanding_interest_amount, payment_reference_number, pslf_status, repayment_plan, sequence_number, servicer_address, ytd_interest_paid, ytd_principal_paid, *args, **kwargs):  # noqa: E501
        """StudentLoan - a model defined in OpenAPI

        Args:
            account_id (str, none_type): The ID of the account that this liability belongs to. Each account can only contain one liability.
            account_number (str, none_type): The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number).
            disbursement_dates ([date], none_type): The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            expected_payoff_date (date, none_type): The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            guarantor (str, none_type): The guarantor of the student loan.
            interest_rate_percentage (float): The interest rate on the loan as a percentage.
            is_overdue (bool, none_type): `true` if a payment is currently overdue. Availability for this field is limited.
            last_payment_amount (float, none_type): The amount of the last payment.
            last_payment_date (date, none_type): The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            last_statement_issue_date (date, none_type): The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            loan_name (str, none_type): The type of loan, e.g., \"Consolidation Loans\".
            loan_status (StudentLoanStatus):
            minimum_payment_amount (float, none_type): The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`). Firstmark (`ins_116295` ), EdFinancial Services (`ins_116304`),  and Navient (`ins_116248`) will display as $0 if there is an autopay program in effect.
            next_payment_due_date (date, none_type): The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
            origination_date (date, none_type): The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). 
            origination_principal_amount (float, none_type): The original principal balance of the loan.
            outstanding_interest_amount (float, none_type): The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`.
            payment_reference_number (str, none_type): The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match `account_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different.
            pslf_status (PSLFStatus):
            repayment_plan (StudentRepaymentPlan):
            sequence_number (str, none_type): The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available.
            servicer_address (ServicerAddressData):
            ytd_interest_paid (float, none_type): The year to date (YTD) interest paid. Availability for this field is limited.
            ytd_principal_paid (float, none_type): The year to date (YTD) principal paid. Availability for this field is limited.

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

        self.account_id = account_id
        self.account_number = account_number
        self.disbursement_dates = disbursement_dates
        self.expected_payoff_date = expected_payoff_date
        self.guarantor = guarantor
        self.interest_rate_percentage = interest_rate_percentage
        self.is_overdue = is_overdue
        self.last_payment_amount = last_payment_amount
        self.last_payment_date = last_payment_date
        self.last_statement_issue_date = last_statement_issue_date
        self.loan_name = loan_name
        self.loan_status = loan_status
        self.minimum_payment_amount = minimum_payment_amount
        self.next_payment_due_date = next_payment_due_date
        self.origination_date = origination_date
        self.origination_principal_amount = origination_principal_amount
        self.outstanding_interest_amount = outstanding_interest_amount
        self.payment_reference_number = payment_reference_number
        self.pslf_status = pslf_status
        self.repayment_plan = repayment_plan
        self.sequence_number = sequence_number
        self.servicer_address = servicer_address
        self.ytd_interest_paid = ytd_interest_paid
        self.ytd_principal_paid = ytd_principal_paid
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
