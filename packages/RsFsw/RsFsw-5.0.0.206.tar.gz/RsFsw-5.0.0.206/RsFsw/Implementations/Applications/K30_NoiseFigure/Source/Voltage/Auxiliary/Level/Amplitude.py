from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amplitude:
	"""Amplitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amplitude", core, parent)

	def set(self, voltage: float) -> None:
		"""SCPI: SOURce:VOLTage:AUX:LEVel:AMPLitude \n
		Snippet: driver.applications.k30NoiseFigure.source.voltage.auxiliary.level.amplitude.set(voltage = 1.0) \n
		No command help available \n
			:param voltage: No help available
		"""
		param = Conversions.decimal_value_to_str(voltage)
		self._core.io.write(f'SOURce:VOLTage:AUX:LEVel:AMPLitude {param}')

	def get(self) -> float:
		"""SCPI: SOURce:VOLTage:AUX:LEVel:AMPLitude \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.voltage.auxiliary.level.amplitude.get() \n
		No command help available \n
			:return: voltage: No help available"""
		response = self._core.io.query_str(f'SOURce:VOLTage:AUX:LEVel:AMPLitude?')
		return Conversions.str_to_float(response)
