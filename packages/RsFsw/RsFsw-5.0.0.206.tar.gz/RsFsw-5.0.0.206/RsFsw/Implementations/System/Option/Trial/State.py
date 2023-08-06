from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:OPTion:TRIal[:STATe] \n
		Snippet: driver.system.option.trial.state.set(state = False) \n
		Determines availability of trial option T0. It is pre-installed at the factory on request. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off. The query result indicates the trial license is not available (not installed, expired) . ON | 1 If enabled, you can use additional applications for a limited period of time (90 days from factory installation) . They are accessible from the common 'Mode' dialog box (see 'Selecting the operating mode and applications') . If the trial license is not available (not installed, expired) the command returns an error (E_OPTION_NA) .
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:OPTion:TRIal:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:OPTion:TRIal[:STATe] \n
		Snippet: value: bool = driver.system.option.trial.state.get() \n
		Determines availability of trial option T0. It is pre-installed at the factory on request. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off. The query result indicates the trial license is not available (not installed, expired) . ON | 1 If enabled, you can use additional applications for a limited period of time (90 days from factory installation) . They are accessible from the common 'Mode' dialog box (see 'Selecting the operating mode and applications') . If the trial license is not available (not installed, expired) the command returns an error (E_OPTION_NA) ."""
		response = self._core.io.query_str(f'SYSTem:OPTion:TRIal:STATe?')
		return Conversions.str_to_bool(response)
