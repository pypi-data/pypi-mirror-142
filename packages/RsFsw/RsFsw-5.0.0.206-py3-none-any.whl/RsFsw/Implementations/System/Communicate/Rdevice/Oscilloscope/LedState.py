from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedState:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	def set(self, color: enums.ControlState) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState \n
		Snippet: driver.system.communicate.rdevice.oscilloscope.ledState.set(color = enums.ControlState.ERRor) \n
		Returns the state of the LAN connection to the oscilloscope for the optional 2 GHz / 5 GHz bandwidth extension (R&S
		FSW-B2000/B5000) . For details see 'Alignment'. \n
			:param color: OFF | SUCCessful | ERRor SUCCessful Connection to the instrument has been established successfully. OFF No instrument configured. ERRor Connection to the instrument could not be established. Check the connection between the R&S FSW and the oscilloscope, and make sure the IP address of the oscilloscope has been defined (see method RsFsw.Applications.K6_Pulse.System.Communicate.Rdevice.Oscilloscope.Tcpip.set) .
		"""
		param = Conversions.enum_scalar_to_str(color, enums.ControlState)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ControlState:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState \n
		Snippet: value: enums.ControlState = driver.system.communicate.rdevice.oscilloscope.ledState.get() \n
		Returns the state of the LAN connection to the oscilloscope for the optional 2 GHz / 5 GHz bandwidth extension (R&S
		FSW-B2000/B5000) . For details see 'Alignment'. \n
			:return: color: OFF | SUCCessful | ERRor SUCCessful Connection to the instrument has been established successfully. OFF No instrument configured. ERRor Connection to the instrument could not be established. Check the connection between the R&S FSW and the oscilloscope, and make sure the IP address of the oscilloscope has been defined (see method RsFsw.Applications.K6_Pulse.System.Communicate.Rdevice.Oscilloscope.Tcpip.set) ."""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.ControlState)
