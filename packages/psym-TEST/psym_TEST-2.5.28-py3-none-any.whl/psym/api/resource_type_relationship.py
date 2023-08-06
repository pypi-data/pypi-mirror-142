#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import enum
from psym.client import SymphonyClient
from psym.common.data_class import LocationType, resourceTypeRelationship
from psym.common.data_enum import Entity
from psym.exceptions import EntityNotFoundError
from psym.graphql.enum.resource_relationship_multiplicity_kind import ResourceRelationshipMultiplicityKind
from psym.graphql.enum.resource_relationship_type_kind import ResourceRelationshipTypeKind
from psym.graphql.enum.resource_relationship_types_kind import ResourceRelationshipTypesKind
from ..graphql.input.add_resource_type_relationship_input import AddResourceTypeRelationshipInput
from ..graphql.mutation.add_resource_type_relationship import addResourceTypeRelationship
from ..graphql.mutation.edit_resource_type_relationship import editResourceTypeRelationship
from ..graphql.input.edit_resource_type_relationship_input import EditResourceTypeRelationshipInput
from ..graphql.query.resource_type_relationships import resourceTypeRelationships
from ..graphql.mutation.remove_resource_type_relationship import removeResourceTypeRelationship
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional


def add_resource_type_relationship(
    client: SymphonyClient, 
    resourceRelationshipMultiplicity: ResourceRelationshipMultiplicityKind,
    resourceRelationshipType: ResourceRelationshipTypesKind,
    resourceTypeA: str,
    resourceTypeB: Optional[str] = None,
    locationType: Optional[str] = None,
) -> resourceTypeRelationship:
    resource_relationship_input = AddResourceTypeRelationshipInput(
        resourceRelationshipType= resourceRelationshipType,
        resourceRelationshipMultiplicity= resourceRelationshipMultiplicity,
        resourceTypeA= resourceTypeA,
        locationType= locationType,
        resourceTypeB= resourceTypeB,
    )
    result = addResourceTypeRelationship.execute(client, input=resource_relationship_input)
    return resourceTypeRelationship(
        id=result.id,
        resourceRelationshipMultiplicity=result.resourceRelationshipMultiplicity,
        resourceRelationshipType=result.resourceRelationshipType,
        resourceTypeA=result.resourceTypeA,
        resourceTypeB=result.resourceTypeB,
        LocationType=result.locationType 
    )
def edit_resource_type_relationship(
    client: SymphonyClient,
    resourceTypeRelationship_id: str,
    resourceTypeA: str,
    locationType: Optional[str],
    resourceTypeB: Optional[str],
    resourceRelationshipMultiplicity: ResourceRelationshipMultiplicityKind,
    resourceRelationshipType: ResourceRelationshipTypeKind,
) -> resourceTypeRelationship: 
    resource_type_relationship_ = get_resource_type_relationship_by_id(client=client, id=resourceTypeRelationship_id)
    resourceRelationshipMultiplicity = resource_type_relationship_.resourceRelationshipMultiplicity if resourceRelationshipMultiplicity is None else resourceRelationshipMultiplicity
    resourceRelationshipType = resource_type_relationship_.resourceRelationshipType if resourceRelationshipType is None else resourceRelationshipType
    resourceTypeA = resource_type_relationship_.resourceTypeA if resourceTypeA is None else resourceTypeA
    resourceTypeB = resource_type_relationship_.resourceTypeB if resourceTypeB is None else resourceTypeB
    locationType = resource_type_relationship_.LocationType if locationType is None else locationType
    resource_type_relationship_input = EditResourceTypeRelationshipInput(
        id=resourceTypeRelationship_id,
        resourceTypeA=resourceTypeA,
        locationType=resourceTypeB,
        resourceTypeB=locationType,
        resourceRelationshipMultiplicity=resourceRelationshipMultiplicity,
        resourceRelationshipType=resourceRelationshipType,
    )
    result = editResourceTypeRelationship.execute(client, resource_type_relationship_input)
    return resourceTypeRelationship(
        id=result.id,
        resourceRelationshipMultiplicity=result.resourceRelationshipMultiplicity,
        resourceRelationshipType=result.resourceRelationshipType,
        LocationType=result.locationType,
        resourceTypeA=result.resourceTypeA,
        resourceTypeB=result.resourceTypeB
    )

def get_resource_type_relationships(client: SymphonyClient) -> Iterator[resourceTypeRelationship]:
    resource_relationships = resourceTypeRelationships.execute(client, first=PAGINATION_STEP)
    edges = resource_relationships.edges if resource_relationships else []
    while resource_relationships is not None and resource_relationships.pageInfo.hasNextPage:
        resource_relationships = resourceTypeRelationships.execute(
            client, after=resource_relationships.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if resource_relationships is not None:
            edges.extend(resource_relationships.edges)

    for edge in edges:
        node = edge.node
        if node is not None:
            yield resourceTypeRelationship(
                id=node.id,
                resourceRelationshipMultiplicity=node.resourceRelationshipMultiplicity,
                resourceRelationshipType=node.resourceRelationshipType,
                resourceTypeA=node.resourceTypeA,
                resourceTypeB=node.resourceTypeB,
                LocationType=node.locationType
            )

def get_resource_type_relationship_by_id(client: SymphonyClient, id: str) -> resourceTypeRelationship:
    resource_type_relationship_id = get_resource_type_relationships(client=client)
    for resource_type_relationship_ in resource_type_relationship_id:
        if resource_type_relationship_.id == id:
            return resource_type_relationship_
    raise EntityNotFoundError(entity=Entity.resourceTypeRelationship, entity_id=id)


def delete_resource_type_relationship(client: SymphonyClient, id: str) -> None:
    """This function delete Resource Relationship Type.

    :param name: Resource Relationship Type name
    :type name: :class:`~psym.common.data_class.resourceRelationship`
    :rtype: None

    **Example**

    .. code-block:: python

        client.delete_resource_relationship(resourceRelationship.id)
    """
    removeResourceTypeRelationship.execute(client, id=id)