from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:STATe \n
		Snippet: driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.state.set(state = False) \n
		Activates the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) . Note: Manual operation on the connected
		oscilloscope, or remote operation other than by the R&S FSW, is not possible while the B2000/B5000 option is active. For
		details on prerequisites and restrictions see 'Basics on the 2 GHz Bandwidth Extension (R&S FSW-B2000 Option) '. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:STATe \n
		Snippet: value: bool = driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.state.get() \n
		Activates the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) . Note: Manual operation on the connected
		oscilloscope, or remote operation other than by the R&S FSW, is not possible while the B2000/B5000 option is active. For
		details on prerequisites and restrictions see 'Basics on the 2 GHz Bandwidth Extension (R&S FSW-B2000 Option) '. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:STATe?')
		return Conversions.str_to_bool(response)
