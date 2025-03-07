"""Contains the changelog for fmu_results.json."""

from fmu.dataio._models._changelog_base import ChangeLog, ChangeLogEntry, FieldChanges

CHANGELOG = ChangeLog(
    [
        ChangeLogEntry(
            version="0.9.0",
            description="This is the first new version of the schema 🎉",
            field_changes=[
                FieldChanges(
                    field="data.product",
                    changes=["This field has been renamed to `data.standard_result`"],
                )
            ],
        ),
        ChangeLogEntry(
            version="0.8.0",
            description="This is the initial schema.",
            field_changes=[],
        ),
    ]
)
