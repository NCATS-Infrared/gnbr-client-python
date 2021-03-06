# coding: utf-8

"""
    GNBR Knowledge Beacon API

    This is the GNBR Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: srensi@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExactMatchResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'has_exact_matches': 'list[str]',
        'id': 'str',
        'within_domain': 'bool'
    }

    attribute_map = {
        'has_exact_matches': 'has_exact_matches',
        'id': 'id',
        'within_domain': 'within_domain'
    }

    def __init__(self, has_exact_matches=None, id=None, within_domain=None):  # noqa: E501
        """ExactMatchResponse - a model defined in Swagger"""  # noqa: E501

        self._has_exact_matches = None
        self._id = None
        self._within_domain = None
        self.discriminator = None

        if has_exact_matches is not None:
            self.has_exact_matches = has_exact_matches
        if id is not None:
            self.id = id
        if within_domain is not None:
            self.within_domain = within_domain

    @property
    def has_exact_matches(self):
        """Gets the has_exact_matches of this ExactMatchResponse.  # noqa: E501

        List of [CURIE](https://www.w3.org/TR/curie/) identifiers of a exactly matching concepts.   # noqa: E501

        :return: The has_exact_matches of this ExactMatchResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_exact_matches

    @has_exact_matches.setter
    def has_exact_matches(self, has_exact_matches):
        """Sets the has_exact_matches of this ExactMatchResponse.

        List of [CURIE](https://www.w3.org/TR/curie/) identifiers of a exactly matching concepts.   # noqa: E501

        :param has_exact_matches: The has_exact_matches of this ExactMatchResponse.  # noqa: E501
        :type: list[str]
        """

        self._has_exact_matches = has_exact_matches

    @property
    def id(self):
        """Gets the id of this ExactMatchResponse.  # noqa: E501

        A given [CURIE](https://www.w3.org/TR/curie/) identifier.   # noqa: E501

        :return: The id of this ExactMatchResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExactMatchResponse.

        A given [CURIE](https://www.w3.org/TR/curie/) identifier.   # noqa: E501

        :param id: The id of this ExactMatchResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def within_domain(self):
        """Gets the within_domain of this ExactMatchResponse.  # noqa: E501

        True if the knowledge source is aware of this identifier, and has the capacity to return the identified concept. Otherwise, false.   # noqa: E501

        :return: The within_domain of this ExactMatchResponse.  # noqa: E501
        :rtype: bool
        """
        return self._within_domain

    @within_domain.setter
    def within_domain(self, within_domain):
        """Sets the within_domain of this ExactMatchResponse.

        True if the knowledge source is aware of this identifier, and has the capacity to return the identified concept. Otherwise, false.   # noqa: E501

        :param within_domain: The within_domain of this ExactMatchResponse.  # noqa: E501
        :type: bool
        """

        self._within_domain = within_domain

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExactMatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
