from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.frequency.center.step.auto.set(state = False) \n
		Defines the step width of the center frequency. \n
			:param state: ON | 1 Links the step width to the current standard (currently 1 MHz for all standards) OFF | 0 Sets the step width as defined using the FREQ:CENT:STEP command (see [SENSe:]FREQuency:CENTer:STEP) .
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.frequency.center.step.auto.get() \n
		Defines the step width of the center frequency. \n
			:return: state: ON | 1 Links the step width to the current standard (currently 1 MHz for all standards) OFF | 0 Sets the step width as defined using the FREQ:CENT:STEP command (see [SENSe:]FREQuency:CENTer:STEP) ."""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP:AUTO?')
		return Conversions.str_to_bool(response)
