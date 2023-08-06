from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedState:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState \n
		Snippet: value: str = driver.applications.k6Pulse.system.communicate.rdevice.oscilloscope.ledState.get() \n
		Returns the state of the LAN connection to the oscilloscope for the optional 2 GHz / 5 GHz bandwidth extension (R&S
		FSW-B2000/B5000) . For details see 'Alignment'. \n
			:return: led_state: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState?')
		return trim_str_response(response)
