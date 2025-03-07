"""Contains the model used to represent a schema's changelog."""

from __future__ import annotations

from typing import Iterator, List, Optional

from pydantic import BaseModel, RootModel

from fmu.dataio.types import VersionStr


class FieldChanges(BaseModel):
    """Contains a list of changes relevant to a particular field in the schema."""

    field: str
    """The field within the schema being changed, i.e. `data.standard_result`."""

    changes: List[str]
    """A list of changes that occurred to this field.

    These changes will be rendered as bullet points. In most cases there is just one
    change."""


class ChangeLogEntry(BaseModel):
    """Contains all changes related to a particular schema version number."""

    version: VersionStr
    """The version of the schema."""

    description: Optional[str] = None
    """An optional description of the overall schema changes."""

    field_changes: List[FieldChanges]
    """A list of fields that changed and descriptions capturing those changes."""


class ChangeLog(RootModel[List[ChangeLogEntry]]):
    """Represents the changelog for all versions of a schema."""

    def __iter__(self) -> Iterator[ChangeLogEntry]:  # type: ignore
        return iter(self.root)
