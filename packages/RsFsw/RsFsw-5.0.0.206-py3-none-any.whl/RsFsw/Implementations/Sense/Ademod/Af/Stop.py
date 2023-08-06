from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:ADEMod:AF:STOP \n
		Snippet: driver.sense.ademod.af.stop.set(frequency = 1.0) \n
		This command sets the stop frequency for AF spectrum result display. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:ADEMod:AF:STOP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:AF:STOP \n
		Snippet: value: float = driver.sense.ademod.af.stop.get() \n
		This command sets the stop frequency for AF spectrum result display. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:AF:STOP?')
		return Conversions.str_to_float(response)
