from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ru26Index:
	"""Ru26Index commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ru26Index", core, parent)

	def set(self, index: float, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:RU26index \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.ru26Index.set(index = 1.0, segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default) \n
		Sets or queries the index of the resource unit based on 26-subcarrier units. \n
			:param index: integer Range: 1 to 143
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
		"""
		param = Conversions.decimal_value_to_str(index)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:RU26index {param}')

	def get(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default) -> float:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:RU26index \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.ru26Index.get(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default) \n
		Sets or queries the index of the resource unit based on 26-subcarrier units. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:return: index: integer Range: 1 to 143"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:RU26index?')
		return Conversions.str_to_float(response)
