from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, display_pps: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PRATe[:VALue] \n
		Snippet: driver.applications.k70Vsa.display.window.prate.value.set(display_pps = 1.0, window = repcap.Window.Default) \n
		This command determines the number of points to be displayed per symbol if manual mode is selected (see method RsFsw.
		Applications.K70_Vsa.Display.Window.Prate.Auto.set) . This command is not available for result displays based on the
		capture buffer; in this case, the displayed points per symbol are defined by the sample rate ([SENSe:]DDEMod:PRATe
		command) . \n
			:param display_pps: 1, 2, 4, 8,16 or 32 1 only the symbol time instants are displayed 2, 4, 8, 16, 32 more points are displayed than symbols
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(display_pps)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PRATe:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:PRATe[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.display.window.prate.value.get(window = repcap.Window.Default) \n
		This command determines the number of points to be displayed per symbol if manual mode is selected (see method RsFsw.
		Applications.K70_Vsa.Display.Window.Prate.Auto.set) . This command is not available for result displays based on the
		capture buffer; in this case, the displayed points per symbol are defined by the sample rate ([SENSe:]DDEMod:PRATe
		command) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: display_pps: 1, 2, 4, 8,16 or 32 1 only the symbol time instants are displayed 2, 4, 8, 16, 32 more points are displayed than symbols"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PRATe:VALue?')
		return Conversions.str_to_float(response)
