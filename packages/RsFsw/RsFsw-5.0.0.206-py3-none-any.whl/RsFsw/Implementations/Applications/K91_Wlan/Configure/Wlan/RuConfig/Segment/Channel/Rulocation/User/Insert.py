from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:INSert \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.insert.set(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		For HE Multi-User Downlink PPDUs that support MIMO only: Adds another user (station) for the selected resource unit (RU)
		to the configuration table. A maximum of 8 users can be assigned to a single resource unit in MIMO mode. This function is
		only available for RU sizes of at least 106 subcarriers. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:INSert')

	def set_with_opc(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default, opc_timeout_ms: int = -1) -> None:
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:INSert \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.insert.set_with_opc(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		For HE Multi-User Downlink PPDUs that support MIMO only: Adds another user (station) for the selected resource unit (RU)
		to the configuration table. A maximum of 8 users can be assigned to a single resource unit in MIMO mode. This function is
		only available for RU sizes of at least 106 subcarriers. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:INSert', opc_timeout_ms)
