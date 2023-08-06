from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Packet:
	"""Packet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("packet", core, parent)

	def set(self, packet: float, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:PACKet \n
		Snippet: driver.applications.k149Uwb.sense.window.display.rwConfig.packet.set(packet = 1.0, window = repcap.Window.Default) \n
		Sets the packet for this window and for any other windows this window is linked to. \n
			:param packet: numeric value
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(packet)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:PACKet {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:PACKet \n
		Snippet: value: float = driver.applications.k149Uwb.sense.window.display.rwConfig.packet.get(window = repcap.Window.Default) \n
		Sets the packet for this window and for any other windows this window is linked to. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: packet: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:PACKet?')
		return Conversions.str_to_float(response)
