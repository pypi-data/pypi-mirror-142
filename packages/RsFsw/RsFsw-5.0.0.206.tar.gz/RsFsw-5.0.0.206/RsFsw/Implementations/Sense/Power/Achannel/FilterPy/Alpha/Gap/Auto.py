from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, alpha: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:GAP<gap>[:AUTO] \n
		Snippet: driver.sense.power.achannel.filterPy.alpha.gap.auto.set(alpha = 1.0, gapChannel = repcap.GapChannel.Default) \n
		This command defines the roll-off factor for the specified gap (CACLR) channel's weighting filter in all sub block gaps. \n
			:param alpha: Roll-off factor Range: 0 to 1
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.decimal_value_to_str(alpha)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:GAP{gapChannel_cmd_val}:AUTO {param}')
