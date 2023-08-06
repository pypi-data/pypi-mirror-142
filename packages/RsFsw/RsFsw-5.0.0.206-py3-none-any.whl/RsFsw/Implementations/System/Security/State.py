from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:SECurity[:STATe] \n
		Snippet: driver.system.security.state.set(state = False) \n
		Activates or queries secure user mode. Note: Before you activate secure user mode, store any instrument settings that are
		required beyond the current session, such as predefined instrument settings, transducer files, or self-alignment data.
		Note: Initially after installation of the R&S FSW-K33 option, secure user mode must be enabled manually once before
		remote control is possible. This is necessary to prompt for a change of passwords. For details on the secure user mode
		see 'Protecting data using the secure user mode'. \n
			:param state: ON | OFF | 0 | 1 ON | 1 The R&S FSW automatically reboots and starts in secure user mode. In secure user mode, no data is written to the instrument's internal solid-state drive. Data that the R&S FSW normally stores on the solid-state drive is redirected to SDRAM. OFF | 0 The R&S FSW is set to normal instrument mode. Data is stored to the internal solid-state drive. Note: this parameter is for query only. Secure user mode cannot be deactivated via remote operation.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:SECurity:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:SECurity[:STATe] \n
		Snippet: value: bool = driver.system.security.state.get() \n
		Activates or queries secure user mode. Note: Before you activate secure user mode, store any instrument settings that are
		required beyond the current session, such as predefined instrument settings, transducer files, or self-alignment data.
		Note: Initially after installation of the R&S FSW-K33 option, secure user mode must be enabled manually once before
		remote control is possible. This is necessary to prompt for a change of passwords. For details on the secure user mode
		see 'Protecting data using the secure user mode'. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 The R&S FSW automatically reboots and starts in secure user mode. In secure user mode, no data is written to the instrument's internal solid-state drive. Data that the R&S FSW normally stores on the solid-state drive is redirected to SDRAM. OFF | 0 The R&S FSW is set to normal instrument mode. Data is stored to the internal solid-state drive. Note: this parameter is for query only. Secure user mode cannot be deactivated via remote operation."""
		response = self._core.io.query_str(f'SYSTem:SECurity:STATe?')
		return Conversions.str_to_bool(response)
