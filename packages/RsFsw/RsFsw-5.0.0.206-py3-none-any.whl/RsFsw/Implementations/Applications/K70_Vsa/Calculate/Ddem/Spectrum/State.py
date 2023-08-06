from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DDEM:SPECtrum[:STATe] \n
		Snippet: driver.applications.k70Vsa.calculate.ddem.spectrum.state.set(state = False, window = repcap.Window.Default) \n
		This command switches the result type transformation to spectrum mode. Spectral evaluation is available for the following
		result types:
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- MAGNitude
			- PHASe/UPHase
			- FREQuency
			- Real/Imag (RIMAG)
		The result types are defined using the method RsFsw.Calculate.FormatPy.set command (see method RsFsw.Calculate.FormatPy.
		set) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DDEM:SPECtrum:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:DDEM:SPECtrum[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.ddem.spectrum.state.get(window = repcap.Window.Default) \n
		This command switches the result type transformation to spectrum mode. Spectral evaluation is available for the following
		result types:
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- MAGNitude
			- PHASe/UPHase
			- FREQuency
			- Real/Imag (RIMAG)
		The result types are defined using the method RsFsw.Calculate.FormatPy.set command (see method RsFsw.Calculate.FormatPy.
		set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DDEM:SPECtrum:STATe?')
		return Conversions.str_to_bool(response)
