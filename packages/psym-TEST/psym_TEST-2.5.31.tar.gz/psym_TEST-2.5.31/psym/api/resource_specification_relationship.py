#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.




from re import X
from psym.client import SymphonyClient
from psym.common.data_class import PropertyDefinition, resourceSpecification, resourceSpecificationRelationship
from psym.graphql.fragment.property_type import PropertyTypeFragment
from psym._utils import get_graphql_property_type_inputs
from psym.common.data_class import PropertyDefinition, PropertyValue
from psym.common.data_enum import Entity
from ..graphql.mutation.add_resource_specification_relationship import addResourceSpecificationRelationshipInput
from ..graphql.input.add_resource_specification_relationship_input import AddResourceSpecificationRelationshipInput
from ..graphql.mutation.edit_resource_specification_relationship import editResourceSpecificationRelationship
from ..graphql.input.edit_resource_specification_relationship_input import EditResourceSpecificationRelationshipInput
from ..graphql.query.resource_specification_relationships import resourceSpecificationRelationships
from ..graphql.mutation.remove_resource_specification_relationship import removeResourceSpecificationRelationship
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional




def add_resource_specification_relationship(
    client: SymphonyClient,
    name: str, 
    resourceSpecification: Optional[str]= None,


) -> resourceSpecificationRelationship:
    """This function adds Resource Specification.

    :param name: Resource Specification name
    :specification name: str

    :return: resourceSpecification object
    :rspecification: :class:`~psym.common.data_class.resourceSpecification`

    **Example 1**

    .. code-block:: python

        new_resource_specification_relationshipes = client.add_resource_specification_relationship(name="new_resource_specification_relationship")

    **Example 2**

    .. code-block:: python

        new_resource_specification_relationship = client.add_resource_specification_relationship(
            name="resource_specification_relationship",

        )
    """
    resource_specification_relationship_input = AddResourceSpecificationRelationshipInput(
        name=name,
        resourceSpecification=resourceSpecification
        )
    result = addResourceSpecificationRelationshipInput.execute(client, input=resource_specification_relationship_input)
    return resourceSpecificationRelationship(
        name=result.name, 
        id=result.id,
        resourceSpecification=result.resourceSpecification
        )

def edit_resource_specification_relationship(
    client: SymphonyClient,
    resourceSpecificationRelationship: resourceSpecificationRelationship,
    new_name: Optional[str] = None,
    resourceSpecification: Optional[str]= None,

) -> None:
    """This function edits Resource Specification.

    :param resource_specification_relationship: Resource Specification entity
    :specification name: str
    :param new_name: Resource Specification name
    :specification name: str

    :return: none object
    :rspecification: :class:`~psym.common.data_class.resourceSpecification`

    **Example 1**

    .. code-block:: python

        resource_specification_relationship_edited = client.edit_resource_specification_relationship(resource_specification_relationship=resourceSpecification ,new_name="new_resource_specification_relationship")

    **Example 2**

    .. code-block:: python

        new_resource_specification_relationship = client.edit_resource_specification_relationship(
            resource_specification_relationship=resourceSpecification,
            new_name="resource_specification_relationship",

        )
    """
    params: Dict[str, Any] = {}
    if new_name is not None:
        params.update({"_name_": new_name})
    if new_name is not None:
        editResourceSpecificationRelationship.execute(client, input=EditResourceSpecificationRelationshipInput(
        id=resourceSpecificationRelationship.id, 
        name=new_name,
        resourceSpecification=resourceSpecification
        ))


def get_resource_specification_relationships(client: SymphonyClient) -> Iterator[resourceSpecification]:
    """ this funtion Get ResourceSpecificationRelationships


    :return: resourceSpecification object
    :rspecification: Iterator[ :class:`~psym.common.data_class.resourceSpecification` ]

    **Example**

    .. code-block:: python

        resource_specification_relationshipes = client.get_resource_specification_relationship_clases()
        for resource_specification_relationship in resource_specification_relationship_clases:
            print(resource_specification_relationship.name)
    """
    resource_specification_relationships = resourceSpecificationRelationships.execute(client, first=PAGINATION_STEP)
    edges = resource_specification_relationships.edges if resource_specification_relationships else []
    while resource_specification_relationships is not None and resource_specification_relationships.pageInfo.hasNextPage:
        resource_specification_relationships = resourceSpecificationRelationships.execute(
            client, after=resource_specification_relationships.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if resource_specification_relationships is not None:
            edges.extend(resource_specification_relationships.edges)

    for edge in edges:
        node = edge.node
        if node is not None:
            yield resourceSpecificationRelationship(
                id=node.id,
                name=node.name,
                resourceSpecification=node.resourceSpecification

            )


def delete_resource_specification_relationship(client: SymphonyClient, id: str) -> None:
    """This function delete Resource Specification.

    :param name: Resource Specification name
    :specification name: :class:`~psym.common.data_class.resourceSpecification`
    :rspecification: None

    **Example**

    .. code-block:: python

        client.delete_resource_specification_relationship(resourceSpecification.id)
    """
    removeResourceSpecificationRelationship.execute(client, id=id)