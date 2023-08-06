from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Used_Disk_Space: int: numeric value in bytes Amount of storage space required by all transducers files in the C:/Program Files (x86) /Rohde-Schwarz/FSW/version/trd directory (= sum of all individual FileSize values)
			- Free_Disk_Space: int: numeric value in bytes Amount of free storage space on the R&S FSW
			- File_Size: List[int]: numeric value in bytes Size of a single transducer file
			- Filename: List[str]: string Name of a single transducer file"""
		__meta_args_list = [
			ArgStruct.scalar_int('Used_Disk_Space'),
			ArgStruct.scalar_int('Free_Disk_Space'),
			ArgStruct('File_Size', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Filename', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Used_Disk_Space: int = None
			self.Free_Disk_Space: int = None
			self.File_Size: List[int] = None
			self.Filename: List[str] = None

	def get(self) -> GetStruct:
		"""SCPI: [SENSe]:CORRection:TRANsducer:CATalog \n
		Snippet: value: GetStruct = driver.sense.correction.transducer.catalog.get() \n
		This command queries all transducer factors stored on the R&S FSW. After general data for the transducer storage
		directory, data for the individual files is listed. The result is a comma-separated list of values with the following
		syntax: <UsedMem>,<FreeMem>,<FileSize>,<FileName>[,<FileSize>,<FileName>] For details see 'Basics on transducer factors'. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:TRANsducer:CATalog?', self.__class__.GetStruct())
