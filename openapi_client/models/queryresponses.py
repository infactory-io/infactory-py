# coding: utf-8

"""
    Find the knowledge in your data

    <h2><img src='/logo.svg' alt='Infactory' height='50'></h2><p><ul><li><a href='/er.svg'>Entity-Relationship Diagram</a></li><li><a href='/er.md'>Documentation</a></li></ul></p>

    The version of the OpenAPI document: 0.5.0
    Contact: support@infactory.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Queryresponses(BaseModel):
    """
    Represents a queryresponses record
    """ # noqa: E501
    id: StrictStr
    object: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    queryprogram_id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    queryprograms: Optional[Queryprograms] = None
    __properties: ClassVar[List[str]] = ["id", "object", "text", "queryprogram_id", "created_at", "updated_at", "queryprograms"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Queryresponses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of queryprograms
        if self.queryprograms:
            _dict['queryprograms'] = self.queryprograms.to_dict()
        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if queryprogram_id (nullable) is None
        # and model_fields_set contains the field
        if self.queryprogram_id is None and "queryprogram_id" in self.model_fields_set:
            _dict['queryprogram_id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if queryprograms (nullable) is None
        # and model_fields_set contains the field
        if self.queryprograms is None and "queryprograms" in self.model_fields_set:
            _dict['queryprograms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Queryresponses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "text": obj.get("text"),
            "queryprogram_id": obj.get("queryprogram_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "queryprograms": Queryprograms.from_dict(obj["queryprograms"]) if obj.get("queryprograms") is not None else None
        })
        return _obj

from openapi_client.models.queryprograms import Queryprograms
# TODO: Rewrite to not use raise_errors
Queryresponses.model_rebuild(raise_errors=False)

