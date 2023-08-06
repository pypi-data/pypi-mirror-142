#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.




from psym.client import SymphonyClient
from psym.common.data_class import resourceType
from psym.common.data_enum import Entity
from psym.exceptions import EntityNotFoundError


from ..graphql.mutation.add_resource_type import addResourceType
from ..graphql.input.add_resource_type_input import AddResourceTypeInput
from ..graphql.mutation.edit_resource_type import editResourceType
from ..graphql.input.edit_resource_type_input import EditResourceTypeInput
from ..graphql.query.resource_types import resourceTypes
from ..graphql.mutation.remove_resource_type import removeResourceType
from psym.graphql.enum.resource_type_class_kind import ResourceTypeClassKind
from psym.graphql.enum.resource_type_base_type_kind import ResourceTypeBaseTypeKind
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional





def add_resource_type(
    client: SymphonyClient,
    name: str,
    resourceTypeClass: ResourceTypeClassKind, 
    resourceTypeBaseType: ResourceTypeBaseTypeKind
) -> resourceType:
    """This function adds Resource Type.

    :param name: Resource Type name
    :type name: str
    :param name: resourceTypeClass Type resourceTypeClass
    :type name: ResourceTypeClassKind
    :param name: ResourceTypeClassKind Type ResourceTypeClassKind
    :type name: ResourceTypeClassKind

    
    :return: resourceType object
    :rtype: :class:`~psym.common.data_class.resourceType`

    **Example 1**

    .. code-block:: python

        new_resource_typees = client.add_resource_type(name="new_resource_type")

    **Example 2**

    .. code-block:: python

        new_resource_type = client.add_resource_type(
            name="resource_type",

        )
    """
    resource_type_input = AddResourceTypeInput(
        name=name, 
        resourceTypeBaseType=resourceTypeBaseType,
        resourceTypeClass=resourceTypeClass)

    result = addResourceType.execute(client, input=resource_type_input)

    return resourceType(
        name=result.name, 
        id=result.id, 
        resourceTypeClass=result.resourceTypeClass, 
        resourceTypeBaseType=result.resourceTypeBaseType)

def get_resource_type_by_id(client: SymphonyClient, id: str) -> resourceType:
    resource_type_by_id = get_resource_types(client=client)
    for resource_type_ in resource_type_by_id:
        if resource_type_.id == id:
            return resource_type_
    raise EntityNotFoundError(entity=Entity.resourceType, entity_id=id)
    
def edit_resource_type(
    client: SymphonyClient,
    resourceType_id: str,
    new_name: Optional[str] = None,
    resourceTypeClass: Optional[ResourceTypeClassKind] = None,
    resourceTypeBaseType: Optional[ResourceTypeBaseTypeKind] = None,
) -> resourceType:
    """This function edits Resource Type.

    :param resource_type: Resource Type entity
    :type name: str
    :param new_name: Resource Type name
    :type name: str

    :return: none object
    :rtype: :class:`~psym.common.data_class.resourceType`

    **Example 1**

    .. code-block:: python

        resource_type_edited = client.edit_resource_type(resource_type=resourceType ,new_name="new_resource_type")

    **Example 2**

    .. code-block:: python

        new_resource_type = client.edit_resource_type(
            resource_type=resourceType,
            new_name="resource_type",

        )
    """
    resource_type_ = get_resource_type_by_id(client=client, id=resourceType_id)
    resourceTypeClass = resource_type_.resourceTypeClass if resourceTypeClass is None else resourceTypeClass
    resourceTypeBaseType = resource_type_.resourceTypeBaseType if resourceTypeBaseType is None else resourceTypeBaseType
    new_name=resource_type_.name if new_name is None else new_name
    
    resource_type_input = EditResourceTypeInput(
        id=resourceType_id,
        name=new_name,
        resourceTypeBaseType=resourceTypeBaseType,
        resourceTypeClass=resourceTypeClass



    )
    result = editResourceType.execute(client, resource_type_input)
    return resourceType(
        id=result.id,
        name=result.name,
        resourceTypeClass=result.resourceTypeClass,
        resourceTypeBaseType=result.resourceTypeBaseType

    )



def get_resource_types(client: SymphonyClient) -> Iterator[resourceType]:
    """ this funtion Get ResourceTypes


    :return: resourceType object
    :rtype: Iterator[ :class:`~psym.common.data_class.resourceType` ]

    **Example**

    .. code-block:: python

        resource_typees = client.get_resource_type_clases()
        for resource_type in resource_type_clases:
            print(resource_type.name)
    """
    resource_types = resourceTypes.execute(client, first=PAGINATION_STEP)
    edges = resource_types.edges if resource_types else []
    while resource_types is not None and resource_types.pageInfo.hasNextPage:
        resource_types = resourceTypes.execute(
            client, after=resource_types.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if resource_types is not None:
            edges.extend(resource_types.edges)

    for edge in edges:
        node = edge.node
        if node is not None:
            yield resourceType(
                id=node.id,
                name=node.name,
                resourceTypeClass=node.resourceTypeClass,
                resourceTypeBaseType=node.resourceTypeBaseType
            )


def delete_resource_type(client: SymphonyClient, id: str) -> None:
    """This function delete Resource Type.

    :param name: Resource Type name
    :type name: :class:`~psym.common.data_class.resourceType`
    :rtype: None

    **Example**

    .. code-block:: python

        client.delete_resource_type(resourceType.id)
    """
    removeResourceType.execute(client, id=id)



