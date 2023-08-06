from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, average_mode: enums.AverageModeC) -> None:
		"""SCPI: [SENSe]:AVERage:TYPE \n
		Snippet: driver.applications.k17Mcgd.sense.average.typePy.set(average_mode = enums.AverageModeC.LINear) \n
		This command selects the trace averaging mode. \n
			:param average_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(average_mode, enums.AverageModeC)
		self._core.io.write(f'SENSe:AVERage:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AverageModeC:
		"""SCPI: [SENSe]:AVERage:TYPE \n
		Snippet: value: enums.AverageModeC = driver.applications.k17Mcgd.sense.average.typePy.get() \n
		This command selects the trace averaging mode. \n
			:return: average_mode: No help available"""
		response = self._core.io.query_str(f'SENSe:AVERage:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AverageModeC)
