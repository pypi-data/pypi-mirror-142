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

	def set(self, state: bool, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:GAP<gap>[:AUTO] \n
		Snippet: driver.sense.power.achannel.filterPy.state.gap.auto.set(state = False, gapChannel = repcap.GapChannel.Default) \n
		This command turns the weighting filter for the specified gap (CACLR) channel in all sub block gaps on and off. \n
			:param state: ON | OFF | 1 | 0
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.bool_to_str(state)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:STATe:GAP{gapChannel_cmd_val}:AUTO {param}')
