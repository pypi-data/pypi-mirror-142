from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	def set(self, scale: float, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:CONFig:SCALe \n
		Snippet: driver.applications.k149Uwb.sense.window.display.config.scale.set(scale = 1.0, window = repcap.Window.Default) \n
		Sets the X scale for the histogram trace results. \n
			:param scale: numeric value Unit: s
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(scale)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:CONFig:SCALe {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:CONFig:SCALe \n
		Snippet: value: float = driver.applications.k149Uwb.sense.window.display.config.scale.get(window = repcap.Window.Default) \n
		Sets the X scale for the histogram trace results. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: scale: numeric value Unit: s"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:CONFig:SCALe?')
		return Conversions.str_to_float(response)
