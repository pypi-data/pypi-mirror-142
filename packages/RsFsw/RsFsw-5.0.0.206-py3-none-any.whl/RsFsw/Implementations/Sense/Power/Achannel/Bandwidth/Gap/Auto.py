from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, bandwidth: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:GAP<gap>[:AUTO] \n
		Snippet: driver.sense.power.achannel.bandwidth.gap.auto.set(bandwidth = 1.0, gapChannel = repcap.GapChannel.Default) \n
		This command defines the bandwidth of the MSR gap (CACLR) channel in all sub block gaps. This command is for MSR signals
		only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For details on MSR signals see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param bandwidth: numeric value in Hz Unit: Hz
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:GAP{gapChannel_cmd_val}:AUTO {param}')
