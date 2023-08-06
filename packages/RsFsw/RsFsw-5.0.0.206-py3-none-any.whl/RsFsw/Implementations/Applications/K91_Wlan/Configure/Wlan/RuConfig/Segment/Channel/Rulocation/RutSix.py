from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RutSix:
	"""RutSix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rutSix", core, parent)

	def set(self, index: float, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:RUTSix \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.rutSix.set(index = 1.0, segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default) \n
		No command help available \n
			:param index: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
		"""
		param = Conversions.decimal_value_to_str(index)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:RUTSix {param}')

	def get(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default) -> float:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:RUTSix \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.rutSix.get(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:return: index: No help available"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:RUTSix?')
		return Conversions.str_to_float(response)
