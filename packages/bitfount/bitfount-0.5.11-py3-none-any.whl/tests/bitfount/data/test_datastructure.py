"""Tests datastructure.py."""
from typing import Any, Dict, List

import pytest
from pytest_asyncio import fixture

from bitfount.data.datastructure import DEFAULT_IMAGE_TRANSFORMATIONS, DataStructure
from bitfount.data.exceptions import DataStructureError
from bitfount.runners.config_schemas import (
    DataStructureAssignConfig,
    DataStructureSelectConfig,
    DataStructureTransformConfig,
)
from bitfount.transformations.batch_operations import ImageTransformation
from tests.utils.helper import TABLE_NAME, unit_test


@unit_test
class TestDataStructure:
    """Tests DataStructure class."""

    @fixture
    def query(self) -> str:
        """Query fixture."""
        return "SELECT * from TABLE"

    def test_transformed_columns_added_to_datastructure(self) -> None:
        """Tests that the transformed columns are added to our datastructure."""
        dataset: List[Dict[str, Dict[str, Any]]] = [
            {"convert_to": {"type": "string", "col": "TARGET"}},
            {"normalise": {"col": ["A", "B"], "keep_original": "A"}},
        ]
        batch = [{"image": {"arg": "col_1", "output": True}}]
        datastructure = DataStructure(
            target="TARGET",
            dataset_transforms=dataset,
            batch_transforms=batch,
            selected_cols=["A", "B", "C", "image"],
            table=TABLE_NAME,
        )
        assert set(datastructure.ignore_cols) == set(["B"])
        assert set(datastructure.selected_cols) == set(
            ["A", "A_normalise", "B_normalise", "C", "image"]
        )

    def test_create_datastructure_from_config(self) -> None:
        """Tests that the datastructure gets the right args fom configs."""
        select = DataStructureSelectConfig(
            include=["TARGET", "weights", "Col1", "image"]
        )
        assign = DataStructureAssignConfig(
            target="TARGET",
            loss_weights_col="weights",
            ignore_classes_col="ignore_classes",
        )
        transform = DataStructureTransformConfig(
            dataset=[{"convert_to": {"type": "string", "col": "TARGET"}}],
            batch=[{"crop": {"col": ["image"], "keep_original": "image"}}],
        )
        ds = DataStructure.create_datastructure(
            select=select,
            transform=transform,
            assign=assign,
            table=TABLE_NAME,
        )
        assert ds.target == "TARGET"
        assert ds.ignore_cols == []
        assert set(ds.selected_cols) == set(["TARGET", "weights", "Col1", "image"])
        assert ds.loss_weights_col == "weights"
        assert ds.ignore_classes_col == "ignore_classes"
        assert ds.batch_transforms == [
            {"crop": {"col": ["image"], "keep_original": "image"}}
        ]
        assert ds.dataset_transforms == [
            {"convert_to": {"type": "string", "col": "TARGET"}}
        ]

    def test_create_datastructure_select_config_raises_error(self) -> None:
        """Tests that the providing both include and exclude cols raises error."""
        select = DataStructureSelectConfig(
            include=["TARGET", "weights", "multihead_col", "Col1"],
            exclude=["Col2", "Col3"],
        )
        transform = DataStructureTransformConfig()
        assign = DataStructureAssignConfig(target="TARGET")
        with pytest.raises(DataStructureError):
            DataStructure.create_datastructure(
                select=select,
                transform=transform,
                assign=assign,
                table=TABLE_NAME,
            )

    def test_get_batch_transformations(self) -> None:
        """Tests `get_batch_transformations` method."""
        batch = [
            {
                "image": {
                    "step": "train",
                    "output": True,
                    "arg": "col1",
                    "transformations": ["RandomBrightnessContrast"],
                }
            }
        ]
        ds = DataStructure(
            target="TARGET",
            batch_transforms=batch,
            selected_cols=["A", "B", "C", "image"],
            table=TABLE_NAME,
        )
        tfms = ds.get_batch_transformations()
        assert tfms is not None
        assert len(tfms) == 1
        assert isinstance(tfms[0], ImageTransformation)

    def test_default_image_transformations(self) -> None:
        """Tests `get_batch_transformations` method."""
        ds = DataStructure(
            target="TARGET",
            selected_cols=["A", "B", "C", "image"],
            image_cols=["image"],
            table=TABLE_NAME,
        )
        assert ds.batch_transforms is not None
        assert ds.batch_transforms == [
            {
                "Image": {
                    "arg": "image",
                    "output": True,
                    "transformations": DEFAULT_IMAGE_TRANSFORMATIONS,
                    "step": "train",
                }
            },
            {
                "Image": {
                    "arg": "image",
                    "output": True,
                    "transformations": DEFAULT_IMAGE_TRANSFORMATIONS,
                    "step": "validation",
                }
            },
        ]

    def test_empty_batch_transformations(self) -> None:
        """Tests that batch transformations can be an empty list.

        Tests that if an empty list is explicitly provided and there are no image
        transformations, then the batch transformations stay empty.
        """
        ds = DataStructure(
            target="TARGET",
            selected_cols=["A", "B", "C", "image"],
            batch_transforms=[],
            table=TABLE_NAME,
        )
        assert ds.batch_transforms == []
        assert ds.get_batch_transformations() == []

    def test_get_table_name_with_single_table_datastructure(self) -> None:
        """Tests that the table name is returned correctly."""
        ds = DataStructure(
            target="TARGET",
            table=TABLE_NAME,
        )
        assert ds.get_table_name() == TABLE_NAME

    def test_get_table_name_with_multi_pod_datastructure(self) -> None:
        """Tests that the table name is returned correctly."""
        ds = DataStructure(
            target="TARGET",
            table={"pod1": "pod1_table", "pod2": "pod2_table"},
        )
        assert ds.get_table_name("pod1") == "pod1_table"

    def test_get_table_name_with_multi_pod_datastructure_raises_value_error(
        self,
    ) -> None:
        """Tests that the `get_table_name` method raises a ValueError."""
        ds = DataStructure(
            target="TARGET",
            table={"pod1": "pod1_table", "pod2": "pod2_table"},
        )
        with pytest.raises(
            ValueError, match="No pod identifier provided for multi-pod datastructure."
        ):
            ds.get_table_name()

    def test_get_pod_identifiers_with_single_table_datastructure(self) -> None:
        """Tests that `get_pod_identifiers` returns None if there are no pods."""
        ds = DataStructure(
            target="TARGET",
            table=TABLE_NAME,
        )
        assert ds.get_pod_identifiers() is None

    def test_get_pod_identifiers_with_multi_pod_datastructure(self) -> None:
        """Tests that `get_pod_identifiers` returns the correct identifiers."""
        ds = DataStructure(
            target="TARGET",
            table={"pod1": "pod1_table", "pod2": "pod2_table"},
        )
        assert ds.get_pod_identifiers() == ["pod1", "pod2"]

    def test_error_raised_for_incompatible_parameters(self) -> None:
        """Tests error is raised when incompatible parameters are given."""
        selected_cols = ["a", "b"]
        ignore_cols = ["c", "d"]
        with pytest.raises(DataStructureError):
            DataStructure(
                target="TARGET",
                table=TABLE_NAME,
                selected_cols=selected_cols,
                ignore_cols=ignore_cols,
            )
