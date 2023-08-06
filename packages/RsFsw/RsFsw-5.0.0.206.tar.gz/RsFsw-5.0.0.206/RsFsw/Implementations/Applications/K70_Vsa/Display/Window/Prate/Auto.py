from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, display_pps_mode: enums.AutoManualMode, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PRATe:AUTO \n
		Snippet: driver.applications.k70Vsa.display.window.prate.auto.set(display_pps_mode = enums.AutoManualMode.AUTO, window = repcap.Window.Default) \n
		Defines the number of display points that are displayed per symbol automatically, i.e. according to [SENSe:]DDEMod:PRATe.
		To define a different number of points per symbol for display, use the MANual parameter and the method RsFsw.Applications.
		K70_Vsa.Display.Window.Prate.Value.set command. \n
			:param display_pps_mode: AUTO | MANual
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(display_pps_mode, enums.AutoManualMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PRATe:AUTO {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AutoManualMode:
		"""SCPI: DISPlay[:WINDow<n>]:PRATe:AUTO \n
		Snippet: value: enums.AutoManualMode = driver.applications.k70Vsa.display.window.prate.auto.get(window = repcap.Window.Default) \n
		Defines the number of display points that are displayed per symbol automatically, i.e. according to [SENSe:]DDEMod:PRATe.
		To define a different number of points per symbol for display, use the MANual parameter and the method RsFsw.Applications.
		K70_Vsa.Display.Window.Prate.Value.set command. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: display_pps_mode: AUTO | MANual"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PRATe:AUTO?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
