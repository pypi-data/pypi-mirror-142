from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: [SENSe]:SRATe \n
		Snippet: driver.applications.k149Uwb.sense.symbolRate.set(sample_rate = 1.0) \n
		Returns the sample rate set up for current measurement settings. \n
			:param sample_rate: numeric value
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'SENSe:SRATe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SRATe \n
		Snippet: value: float = driver.applications.k149Uwb.sense.symbolRate.get() \n
		Returns the sample rate set up for current measurement settings. \n
			:return: sample_rate: numeric value"""
		response = self._core.io.query_str(f'SENSe:SRATe?')
		return Conversions.str_to_float(response)
