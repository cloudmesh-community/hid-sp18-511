import connexion
import six

from swagger_server import util
from swagger_server import filter_util

def filter_regex(criteria):  # noqa: E501
    """filter

    Returns filtered data based on criteria # noqa: E501

    :param criteria: The filter criteria
    :type criteria: str

    :rtype: None
    """
    return filter_util.filter_regex(criteria)
    
