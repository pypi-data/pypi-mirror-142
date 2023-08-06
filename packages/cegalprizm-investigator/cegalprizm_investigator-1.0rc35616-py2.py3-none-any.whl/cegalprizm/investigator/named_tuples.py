# Copyright 2022 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""This file contains the definition of various named tuples used by Investigator
"""

from typing import List, NamedTuple


class InvestigationInfoTuple(NamedTuple):
    """This is a named tuple that defines the basic information to identify an investigation
    """
    id: str
    name: str

class ContinuousPropertyTuple(NamedTuple):
    """This is a named tuple that defines a continuous property
    """
    name: str
    unit_symbol: str

class DiscretePropertyTuple(NamedTuple):
    """This is a named tuple that defines a discrete property
    """
    name: str
    tags: List[str]

class ContinuousDimensionInfoTuple(NamedTuple):
    """This is a named tuple that defines the additional information that can be specified for a continuous dimension
    """
    property_name: str = None
    unit_symbol: str = None
    is_logarithmic: bool = False
    min: float = None
    max: float = None

class DiscreteTagInfoTuple(NamedTuple):
    """This is a named tuple that defines a discrete tag
    """
    index: int
    id: str
    name: str
