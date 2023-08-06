from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsts:
	"""Nsts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsts", core, parent)

	def set(self, no_streams: float, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:NSTS \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.nsts.set(no_streams = 1.0, segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		For MIMO measurements only: Number of space-time streams (NSTS) for each user \n
			:param no_streams: Number of space-time streams (NSTS) for each user Range: 1 to 8
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(no_streams)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:NSTS {param}')

	def get(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default) -> float:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:NSTS \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.nsts.get(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		For MIMO measurements only: Number of space-time streams (NSTS) for each user \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
			:return: no_streams: Number of space-time streams (NSTS) for each user Range: 1 to 8"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:NSTS?')
		return Conversions.str_to_float(response)
