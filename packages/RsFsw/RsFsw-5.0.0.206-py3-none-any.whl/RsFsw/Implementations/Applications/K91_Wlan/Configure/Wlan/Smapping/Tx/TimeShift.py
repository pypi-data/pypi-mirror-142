from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeShift:
	"""TimeShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timeShift", core, parent)

	def set(self, time_shift: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch>:TIMeshift \n
		Snippet: driver.applications.k91Wlan.configure.wlan.smapping.tx.timeShift.set(time_shift = 1.0, channel = repcap.Channel.Default) \n
		This remote control command specifies the timeshift for a specific antenna. \n
			:param time_shift: Time shift (in s) for specification of user defined CSD (cyclic delay diversity) for the Spatial Mapping. Range: -32 ns to 32 ns , Unit: S
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
		"""
		param = Conversions.decimal_value_to_str(time_shift)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val}:TIMeshift {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch>:TIMeshift \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.smapping.tx.timeShift.get(channel = repcap.Channel.Default) \n
		This remote control command specifies the timeshift for a specific antenna. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
			:return: time_shift: Time shift (in s) for specification of user defined CSD (cyclic delay diversity) for the Spatial Mapping. Range: -32 ns to 32 ns , Unit: S"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val}:TIMeshift?')
		return Conversions.str_to_float(response)
