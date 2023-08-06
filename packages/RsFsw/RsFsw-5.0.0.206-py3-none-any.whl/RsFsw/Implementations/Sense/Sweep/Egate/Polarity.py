from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Polarity:
	"""Polarity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polarity", core, parent)

	def set(self, polarity: enums.SlopeType) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:POLarity \n
		Snippet: driver.sense.sweep.egate.polarity.set(polarity = enums.SlopeType.NEGative) \n
		This command selects the polarity of an external gate signal. The setting applies both to the edge of an edge-triggered
		signal and the level of a level-triggered signal. \n
			:param polarity: POSitive | NEGative
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.SlopeType)
		self._core.io.write(f'SENSe:SWEep:EGATe:POLarity {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SlopeType:
		"""SCPI: [SENSe]:SWEep:EGATe:POLarity \n
		Snippet: value: enums.SlopeType = driver.sense.sweep.egate.polarity.get() \n
		This command selects the polarity of an external gate signal. The setting applies both to the edge of an edge-triggered
		signal and the level of a level-triggered signal. \n
			:return: polarity: POSitive | NEGative"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
