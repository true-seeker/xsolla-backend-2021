from rest_framework.exceptions import APIException


class ProductTypeException(APIException):
    status_code = 400
    default_detail = 'product_type parameter must be int'
    default_code = 'wrong product_type'


class MinPriceException(APIException):
    status_code = 400
    default_detail = 'min_price parameter must be float'
    default_code = 'wrong min_price'


class MaxPriceException(APIException):
    status_code = 400
    default_detail = 'max_price parameter must be float'
    default_code = 'wrong max_price'
