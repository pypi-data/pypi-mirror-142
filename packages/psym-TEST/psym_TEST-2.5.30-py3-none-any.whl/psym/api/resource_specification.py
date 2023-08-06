#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.




from psym.client import SymphonyClient
from psym.common.data_class import PropertyDefinition, resourceSpecification
from psym.graphql.fragment.property_type import PropertyTypeFragment
from psym._utils import get_graphql_property_type_inputs
from psym.common.data_class import PropertyDefinition, PropertyValue
from psym.common.data_enum import Entity
from psym.common.data_format import (format_to_property_type_inputs,)
from ..graphql.mutation.add_resource_specification import addResourceSpecification
from ..graphql.input.add_resource_specification_input import AddResourceSpecificationInput
from ..graphql.mutation.edit_resource_specification import editResourceSpecification
from ..graphql.input.edit_resource_specification_input import EditResourceSpecificationInput
from ..graphql.query.resource_specifications import resourceSpecifications
from ..graphql.mutation.remove_resource_specification import removeResourceSpecification
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional





def add_resource_specification(
    client: SymphonyClient, 
    name: str, 
    resourceType: Optional[str]= None,
    propertyTypes: List[PropertyDefinition] = None,

) -> resourceSpecification:
    """This function adds Resource Specification.

    :param name: Resource Specification name
    :specification name: str

    :return: resourceSpecification object
    :rspecification: :class:`~psym.common.data_class.resourceSpecification`

    **Example 1**

    .. code-block:: python

        new_resource_specificationes = client.add_resource_specification(name="new_resource_specification")

    **Example 2**

    .. code-block:: python

        new_resource_specification = client.add_resource_specification(
            name="resource_specification",

        )
    """
    property_type_inputs = []
    if propertyTypes is not None:
        property_type_inputs = format_to_property_type_inputs(data=propertyTypes)
    result = addResourceSpecification.execute(
        client,
        AddResourceSpecificationInput(
            name=name, 
            resourceType=resourceType,
            propertyTypes=property_type_inputs
        ),
    )
    return resourceSpecification(
    name=result.name, 
    id=result.id, 
    resourceType=result.resourceType,
    propertyTypes=result.propertyTypes)


def edit_resource_specification(
    client: SymphonyClient,
    resourceSpecification: resourceSpecification,
    new_name: Optional[str] = None,
    resourceType: Optional[str]= None,
    propertyTypes: List[PropertyDefinition] = None,
) -> None:
    """This function edits Resource Specification.

    :param resource_specification: Resource Specification entity
    :specification name: str
    :param new_name: Resource Specification name
    :specification name: str

    :return: none object
    :rspecification: :class:`~psym.common.data_class.resourceSpecification`

    **Example 1**

    .. code-block:: python

        resource_specification_edited = client.edit_resource_specification(resource_specification=resourceSpecification ,new_name="new_resource_specification")

    **Example 2**

    .. code-block:: python

        new_resource_specification = client.edit_resource_specification(
            resource_specification=resourceSpecification,
            new_name="resource_specification",

        )
    """
    params: Dict[str, Any] = {}
    if new_name is not None:
        params.update({"_name_": new_name})
    if new_name is not None:
        editResourceSpecification.execute(client, input=EditResourceSpecificationInput(
        id=resourceSpecification.id, 
        name=new_name,
        propertyTypes=propertyTypes,
        resourceType=resourceType
        ))


def get_resource_specifications(client: SymphonyClient) -> Iterator[resourceSpecification]:
    """ this funtion Get ResourceSpecifications


    :return: resourceSpecification object
    :rspecification: Iterator[ :class:`~psym.common.data_class.resourceSpecification` ]

    **Example**

    .. code-block:: python

        resource_specificationes = client.get_resource_specification_clases()
        for resource_specification in resource_specification_clases:
            print(resource_specification.name)
    """
    resource_specifications = resourceSpecifications.execute(client, first=PAGINATION_STEP)
    edges = resource_specifications.edges if resource_specifications else []
    while resource_specifications is not None and resource_specifications.pageInfo.hasNextPage:
        resource_specifications = resourceSpecifications.execute(
            client, after=resource_specifications.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if resource_specifications is not None:
            edges.extend(resource_specifications.edges)

    for edge in edges:
        node = edge.node
        if node is not None:
            yield resourceSpecification(
                id=node.id,
                name=node.name,
                resourceType=node.resourceType,
                propertyTypes=node.propertyTypes

            )


def delete_resource_specification(client: SymphonyClient, id: str) -> None:
    """This function delete Resource Specification.

    :param name: Resource Specification name
    :specification name: :class:`~psym.common.data_class.resourceSpecification`
    :rspecification: None

    **Example**

    .. code-block:: python

        client.delete_resource_specification(resourceSpecification.id)
    """
    removeResourceSpecification.execute(client, id=id)