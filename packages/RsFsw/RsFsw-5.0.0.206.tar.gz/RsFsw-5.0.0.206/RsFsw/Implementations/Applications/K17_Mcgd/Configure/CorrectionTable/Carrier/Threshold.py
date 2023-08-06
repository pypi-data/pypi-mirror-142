from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, index: int, carrier_threshold: float) -> None:
		"""SCPI: CONFigure:CTABle:CARRier:THReshold \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.carrier.threshold.set(index = 1, carrier_threshold = 1.0) \n
		Sets the threshold of a specific carrier of the carrier table. \n
			:param index: Carrier position
			:param carrier_threshold: numeric value Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('carrier_threshold', carrier_threshold, DataType.Float))
		self._core.io.write(f'CONFigure:CTABle:CARRier:THReshold {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThresholdStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: int: Carrier position
			- Carrier_Threshold: float: numeric value Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Index'),
			ArgStruct.scalar_float('Carrier_Threshold')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: int = None
			self.Carrier_Threshold: float = None

	def get(self) -> ThresholdStruct:
		"""SCPI: CONFigure:CTABle:CARRier:THReshold \n
		Snippet: value: ThresholdStruct = driver.applications.k17Mcgd.configure.correctionTable.carrier.threshold.get() \n
		Sets the threshold of a specific carrier of the carrier table. \n
			:return: structure: for return value, see the help for ThresholdStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:CTABle:CARRier:THReshold?', self.__class__.ThresholdStruct())
