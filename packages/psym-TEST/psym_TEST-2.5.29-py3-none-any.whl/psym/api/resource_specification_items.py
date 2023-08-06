#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.




from psym.client import SymphonyClient
from psym.common.data_class import PropertyDefinition, ResourceSpecificationItems, resourceSpecification, resourceSpecificationRelationship
from psym.exceptions import EntityNotFoundError
from psym.graphql.fragment.property_type import PropertyTypeFragment
from psym._utils import get_graphql_property_type_inputs
from psym.common.data_class import PropertyDefinition, PropertyValue
from psym.common.data_enum import Entity
from psym.common.data_format import (format_to_property_type_inputs,)
from ..graphql.mutation.add_resource_specification_items import addResourceSpecificationItems
from ..graphql.input.add_resource_specification_items_input import AddResourceSpecificationItemsInput
from ..graphql.mutation.edit_resource_specification_items import editResourceSpecificationtems
from ..graphql.input.edit_resource_specification_items_input import EditResourceSpecificationItemsInput
from ..graphql.query.resource_specification_items import resourceSpecificationItems
from ..graphql.mutation.remove_resource_specification_items import removeResourceSpecificationItems
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional





def add_resource_specification_items(
    client: SymphonyClient,
    resourceSpecificationRelationship: Optional[str]= None,
    resourceSpecification: Optional[str]= None,
) -> ResourceSpecificationItems:

    resource_specification_items_input = AddResourceSpecificationItemsInput(
        resourceSpecificationRelationship=resourceSpecificationRelationship,
        resourceSpecification=resourceSpecification
        )
    result = addResourceSpecificationItems.execute(client, input=resource_specification_items_input)
    return ResourceSpecificationItems(
        id=result.id,
        resourceSpecificationRelationship=result.resourceSpecificationRelationship,
        resourceSpecification=result.resourceSpecification
        )

def get_resource_specification_items_items(client: SymphonyClient) -> Iterator[ResourceSpecificationItems]:
    resource_specification_items = resourceSpecificationItems.execute(client, first=PAGINATION_STEP)
    edges = resource_specification_items.edges if resource_specification_items else []
    while resource_specification_items is not None and resource_specification_items.pageInfo.hasNextPage:
        resource_specification_items = resourceSpecificationItems.execute(
            client, after=resource_specification_items.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if resource_specification_items is not None:
            edges.extend(resource_specification_items.edges)

    for edge in edges:
        node = edge.node
        if node is not None:
            yield ResourceSpecificationItems(
                id=node.id,
                resourceSpecification=node.resourceSpecification,
                resourceSpecificationRelationship=node.resourceSpecificationRelationship

            )

def get_resource_specification_items_by_id(client: SymphonyClient, id: str) -> ResourceSpecificationItems:
    resource_specification_items_id = get_resource_specification_items_items(client=client)
    for resource_specification_items_ in resource_specification_items_id:
        if resource_specification_items_.id == id:
            return resource_specification_items_
    raise EntityNotFoundError(entity=Entity.ResourceSpecificationItems, entity_id=id)

def edit_resource_specification_items(
    client: SymphonyClient,
    resourceSpecificationItems_id: str,
    resourceSpecificationRelationship: Optional[str]= None,
    resourceSpecification: Optional[str]= None,
) -> ResourceSpecificationItems: 
    resource_specification_items_ = get_resource_specification_items_by_id(client=client, id=resourceSpecificationItems_id)
    resourceSpecificationRelationship = resource_specification_items_.resourceSpecificationRelationship if resourceSpecificationRelationship is None else resourceSpecificationRelationship
    resourceSpecification = resource_specification_items_.resourceSpecification if resourceSpecification is None else resourceSpecification
    resource_specification_items_input = EditResourceSpecificationItemsInput(
            id= resourceSpecificationItems_id,
            resourceSpecificationRelationship= resourceSpecificationRelationship,
            resourceSpecification= resourceSpecification

    )
    result = editResourceSpecificationtems.execute(client, resource_specification_items_input)
    return ResourceSpecificationItems(
        id=result.id,
        resourceSpecificationRelationship=result.resourceSpecificationRelationship,
        resourceSpecification=result.resourceSpecificationRelationship
    )

def delete_resource_specification_items(client: SymphonyClient, id: str) -> None:
    removeResourceSpecificationItems.execute(client, id=id)
