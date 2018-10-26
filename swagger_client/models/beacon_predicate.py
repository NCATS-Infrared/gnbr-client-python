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


class BeaconPredicate(object):
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
        'id': 'str',
        'uri': 'str',
        'edge_label': 'str',
        'relation': 'str',
        'local_id': 'str',
        'local_uri': 'str',
        'local_relation': 'str',
        'description': 'str',
        'frequency': 'int'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'edge_label': 'edge_label',
        'relation': 'relation',
        'local_id': 'local_id',
        'local_uri': 'local_uri',
        'local_relation': 'local_relation',
        'description': 'description',
        'frequency': 'frequency'
    }

    def __init__(self, id=None, uri=None, edge_label=None, relation=None, local_id=None, local_uri=None, local_relation=None, description=None, frequency=None):  # noqa: E501
        """BeaconPredicate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._uri = None
        self._edge_label = None
        self._relation = None
        self._local_id = None
        self._local_uri = None
        self._local_relation = None
        self._description = None
        self._frequency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if edge_label is not None:
            self.edge_label = edge_label
        if relation is not None:
            self.relation = relation
        if local_id is not None:
            self.local_id = local_id
        if local_uri is not None:
            self.local_uri = local_uri
        if local_relation is not None:
            self.local_relation = local_relation
        if description is not None:
            self.description = description
        if frequency is not None:
            self.frequency = frequency

    @property
    def id(self):
        """Gets the id of this BeaconPredicate.  # noqa: E501

        CURIE-encoded identifier of predicate relation   # noqa: E501

        :return: The id of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BeaconPredicate.

        CURIE-encoded identifier of predicate relation   # noqa: E501

        :param id: The id of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this BeaconPredicate.  # noqa: E501

        The predicate URI which should generally resolves to the  full semantic description of the predicate relation  # noqa: E501

        :return: The uri of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this BeaconPredicate.

        The predicate URI which should generally resolves to the  full semantic description of the predicate relation  # noqa: E501

        :param uri: The uri of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def edge_label(self):
        """Gets the edge_label of this BeaconPredicate.  # noqa: E501

        A predicate edge label which must be taken from the minimal predicate ('slot') list of the [Biolink Model](https://biolink.github.io/biolink-model).   # noqa: E501

        :return: The edge_label of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._edge_label

    @edge_label.setter
    def edge_label(self, edge_label):
        """Sets the edge_label of this BeaconPredicate.

        A predicate edge label which must be taken from the minimal predicate ('slot') list of the [Biolink Model](https://biolink.github.io/biolink-model).   # noqa: E501

        :param edge_label: The edge_label of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._edge_label = edge_label

    @property
    def relation(self):
        """Gets the relation of this BeaconPredicate.  # noqa: E501

        The predicate relation, with the preferred format being a CURIE where one exists, but strings/labels acceptable. This relation  may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity  (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)   # noqa: E501

        :return: The relation of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this BeaconPredicate.

        The predicate relation, with the preferred format being a CURIE where one exists, but strings/labels acceptable. This relation  may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity  (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)   # noqa: E501

        :param relation: The relation of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._relation = relation

    @property
    def local_id(self):
        """Gets the local_id of this BeaconPredicate.  # noqa: E501

        CURIE-encoded identifier of the locally defined predicate relation. Such terms should be formally documented as mappings in the [Biolink Model](https://biolink.github.io/biolink-model)   # noqa: E501

        :return: The local_id of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this BeaconPredicate.

        CURIE-encoded identifier of the locally defined predicate relation. Such terms should be formally documented as mappings in the [Biolink Model](https://biolink.github.io/biolink-model)   # noqa: E501

        :param local_id: The local_id of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._local_id = local_id

    @property
    def local_uri(self):
        """Gets the local_uri of this BeaconPredicate.  # noqa: E501

        The predicate URI which should generally resolves  to the local predicate relation  # noqa: E501

        :return: The local_uri of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._local_uri

    @local_uri.setter
    def local_uri(self, local_uri):
        """Sets the local_uri of this BeaconPredicate.

        The predicate URI which should generally resolves  to the local predicate relation  # noqa: E501

        :param local_uri: The local_uri of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._local_uri = local_uri

    @property
    def local_relation(self):
        """Gets the local_relation of this BeaconPredicate.  # noqa: E501

        human readable name of the locally defined predicate relation   # noqa: E501

        :return: The local_relation of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._local_relation

    @local_relation.setter
    def local_relation(self, local_relation):
        """Sets the local_relation of this BeaconPredicate.

        human readable name of the locally defined predicate relation   # noqa: E501

        :param local_relation: The local_relation of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._local_relation = local_relation

    @property
    def description(self):
        """Gets the description of this BeaconPredicate.  # noqa: E501

        human readable definition of predicate relation  provided by this beacon   # noqa: E501

        :return: The description of this BeaconPredicate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BeaconPredicate.

        human readable definition of predicate relation  provided by this beacon   # noqa: E501

        :param description: The description of this BeaconPredicate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def frequency(self):
        """Gets the frequency of this BeaconPredicate.  # noqa: E501

        the number of statement entries using the specified predicate in the given beacon knowledge base  # noqa: E501

        :return: The frequency of this BeaconPredicate.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this BeaconPredicate.

        the number of statement entries using the specified predicate in the given beacon knowledge base  # noqa: E501

        :param frequency: The frequency of this BeaconPredicate.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

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
        if not isinstance(other, BeaconPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
