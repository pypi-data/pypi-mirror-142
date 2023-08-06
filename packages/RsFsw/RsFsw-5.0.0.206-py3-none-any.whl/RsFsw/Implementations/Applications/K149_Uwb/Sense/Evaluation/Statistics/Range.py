from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, staticstics_range: enums.StaticsticsRange) -> None:
		"""SCPI: [SENSe]:EVALuation:STATistics:RANGe \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.statistics.range.set(staticstics_range = enums.StaticsticsRange.CAPTure) \n
		Sets the type of range used for evaluating packets. \n
			:param staticstics_range: CAPTure | COUNt
		"""
		param = Conversions.enum_scalar_to_str(staticstics_range, enums.StaticsticsRange)
		self._core.io.write(f'SENSe:EVALuation:STATistics:RANGe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StaticsticsRange:
		"""SCPI: [SENSe]:EVALuation:STATistics:RANGe \n
		Snippet: value: enums.StaticsticsRange = driver.applications.k149Uwb.sense.evaluation.statistics.range.get() \n
		Sets the type of range used for evaluating packets. \n
			:return: staticstics_range: CAPTure | COUNt"""
		response = self._core.io.query_str(f'SENSe:EVALuation:STATistics:RANGe?')
		return Conversions.str_to_scalar_enum(response, enums.StaticsticsRange)
