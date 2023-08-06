from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.TouchscreenState) -> None:
		"""SCPI: DISPlay:TOUChscreen[:STATe] \n
		Snippet: driver.display.touchscreen.state.set(state = enums.TouchscreenState.FRAMe) \n
		This command controls the touch screen functionality. \n
			:param state: ON | FRAMe | OFF ON | 1 Touch screen is active for entire screen OFF | 0 Touch screen is inactivate for entire screen FRAMe Touch screen is inactivate for the diagram area of the screen, but active for softkeys, toolbars and menus.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.TouchscreenState)
		self._core.io.write(f'DISPlay:TOUChscreen:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TouchscreenState:
		"""SCPI: DISPlay:TOUChscreen[:STATe] \n
		Snippet: value: enums.TouchscreenState = driver.display.touchscreen.state.get() \n
		This command controls the touch screen functionality. \n
			:return: state: ON | FRAMe | OFF ON | 1 Touch screen is active for entire screen OFF | 0 Touch screen is inactivate for entire screen FRAMe Touch screen is inactivate for the diagram area of the screen, but active for softkeys, toolbars and menus."""
		response = self._core.io.query_str(f'DISPlay:TOUChscreen:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.TouchscreenState)
