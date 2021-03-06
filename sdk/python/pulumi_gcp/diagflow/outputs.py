# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'EntityTypeEntity',
    'IntentFollowupIntentInfo',
]

@pulumi.output_type
class EntityTypeEntity(dict):
    def __init__(__self__, *,
                 synonyms: Sequence[str],
                 value: str):
        """
        :param Sequence[str] synonyms: A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
               could be green onions.
               For KIND_LIST entity types:
               * This collection must contain exactly one synonym equal to value.
        :param str value: The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
               could be scallions.
               For KIND_MAP entity types:
               * A reference value to be used in place of synonyms.
               For KIND_LIST entity types:
               * A string that can contain references to other entity types (with or without aliases).
        """
        pulumi.set(__self__, "synonyms", synonyms)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def synonyms(self) -> Sequence[str]:
        """
        A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
        could be green onions.
        For KIND_LIST entity types:
        * This collection must contain exactly one synonym equal to value.
        """
        return pulumi.get(self, "synonyms")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
        could be scallions.
        For KIND_MAP entity types:
        * A reference value to be used in place of synonyms.
        For KIND_LIST entity types:
        * A string that can contain references to other entity types (with or without aliases).
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IntentFollowupIntentInfo(dict):
    def __init__(__self__, *,
                 followup_intent_name: Optional[str] = None,
                 parent_followup_intent_name: Optional[str] = None):
        """
        :param str parent_followup_intent_name: The unique identifier of the parent intent in the chain of followup intents.
               Format: projects/<Project ID>/agent/intents/<Intent ID>.
        """
        if followup_intent_name is not None:
            pulumi.set(__self__, "followup_intent_name", followup_intent_name)
        if parent_followup_intent_name is not None:
            pulumi.set(__self__, "parent_followup_intent_name", parent_followup_intent_name)

    @property
    @pulumi.getter(name="followupIntentName")
    def followup_intent_name(self) -> Optional[str]:
        return pulumi.get(self, "followup_intent_name")

    @property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> Optional[str]:
        """
        The unique identifier of the parent intent in the chain of followup intents.
        Format: projects/<Project ID>/agent/intents/<Intent ID>.
        """
        return pulumi.get(self, "parent_followup_intent_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


