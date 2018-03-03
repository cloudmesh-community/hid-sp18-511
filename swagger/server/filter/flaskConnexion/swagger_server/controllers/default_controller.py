import connexion
import six

from swagger_server import util
from swagger_server import filter_util

def filter(criteria):  # noqa: E501
    """filter

    Returns filtered data based on criteria # noqa: E501

    :param criteria: The filter criteria
    :type criteria: str

    :rtype: None
    """
    if criteria == "pos":
        return filter_util.filter_positive()
    elif criteria == "neg":
        return filter_util.filter_negative()
    else:
        return "provided criteria is not supported"
