# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
# |																|
# |             Copyright 2023 - 2023, Amulya Paritosh			|
# |																|
# |  This file is part of Component Library Plugin for FreeCAD.	|
# |																|
# |               This file was created as a part of				|
# |              Google Summer Of Code Program - 2023			|
# |																|
# --------------------------------------------------------------

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import TYPE_CHECKING, Any, Callable, Dict, List

from .data_types import DTypes

if TYPE_CHECKING:
    from .datadef import SerialisedDataType


class DataFactory:
    """
    DataFactory class acts as a factory for creating and serializing data objects.

    Attributes
    ----------
    _registry : Dict[DTypes, SerialisedDataType]
        A dictionary that maps dtype to the corresponding data object class.

    Examples
    --------
    factory.create(dtype=DTypes.METADATA, name="Component")
    factory.serialize()
    factory.load_many(data_list=[data1, data2], dtype=DTypes.FILE)
    """

    _registry: Dict[DTypes, SerialisedDataType] = {}

    def __init__(self) -> None:
        """
        Initializes the object.

        Raises
        ------
        NotImplementedError
            This method is not implemented.
        """
        raise NotImplementedError

    @classmethod
    def __init_subclass__(cls, /, dtype: DTypes, **kwargs) -> None:
        """
        Registers a subclass in the _registry dictionary based on the dtype provided.

        Parameters
        ----------
        cls : type
            The subclass.
        dtype : DTypes
            The dtype associated with the subclass.

        Returns
        -------
        None

        Examples
        --------
        class Subclass(BaseClass):
            pass

        Subclass.__init_subclass__(dtype=DTypes.MY_TYPE)
        """

        super().__init_subclass__(**kwargs)
        cls._registry[dtype] = cls

    @classmethod
    def create(cls, dtype: DTypes, **kwargs: Dict[str, Any]) -> SerialisedDataType:
        """
        Creates a data object of the specified dtype with the provided keyword arguments.

        Parameters
        ----------
        cls : type
            The class.
        dtype : DTypes
            The dtype associated with the data object.
        **kwargs : Dict[str, Any]
            Additional keyword arguments for initializing the data object.

        Returns
        -------
        SerialisedDataType
            The created data object.

        Examples
        --------
        factory = DataFactory()
        factory.create(dtype=DTypes.METADATA, name="Component")
        """

        subclass: SerialisedDataType = cls._registry[dtype]
        return subclass(**kwargs)

    def __is_field(self, attr) -> bool:
        """
        Check if the attribute should be considered as a field for serialization.

        Parameters
        ----------
        attr : Any
            The attribute to be checked.

        Returns
        -------
        bool
            True if the attribute should be considered as a field for serialization, False otherwise.
        """

        return not any(
            (
                attr.startswith("_"),  # Exclude private attributes (starting with '_').
                isinstance(getattr(self, attr), Callable),  # Exclude callable attributes (methods).
            )
        )

    def serialize(self):
        """
        Serialize the data object into a dictionary.

        If the object is not a dataclass, it serializes by including only non-private, non-method attributes.

        Returns
        -------
        dict
            The serialized data object.

        """

        if not is_dataclass(self):
            return {attr: getattr(self, attr) for attr in dir(self) if self.__is_field(attr)}
            # Serialize non-dataclass objects by including only non-private, non-method attributes.

        return asdict(self)

    @staticmethod
    def load_many(data_list: list, dtype: DTypes) -> List[SerialisedDataType]:
        """
        Create and load multiple data objects from a list of dictionaries.

        Parameters
        ----------
        data_list : list
            A list of dictionaries containing data for creating the objects.
        dtype : DTypes
            The type of data object to create.

        Returns
        -------
        List[SerialisedDataType]
            A list of loaded data objects.
        """

        return [DataFactory.create(dtype=dtype, **data) for data in data_list]
