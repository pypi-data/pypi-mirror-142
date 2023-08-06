from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BreakPy:
	"""BreakPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("breakPy", core, parent)

	def set(self, state: bool, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BREak \n
		Snippet: driver.sense.listPy.range.breakPy.set(state = False, rangePy = repcap.RangePy.Default) \n
		This command controls the sweep for all ranges. The sweep list cannot be configured using remote commands during an
		on-going sweep operation. \n
			:param state: ON | 1 The R&S FSW stops after measuring one range, and the status bit number 10 in the STAT:OPER register is set. (See 'STATus:OPERation register'.) To continue with the next range, use method RsFsw.Applications.K17_Mcgd.Initiate.ConMeas.set. OFF | 0 The R&S FSW sweeps all ranges in one go.
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BREak {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BREak \n
		Snippet: value: bool = driver.sense.listPy.range.breakPy.get(rangePy = repcap.RangePy.Default) \n
		This command controls the sweep for all ranges. The sweep list cannot be configured using remote commands during an
		on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | 1 The R&S FSW stops after measuring one range, and the status bit number 10 in the STAT:OPER register is set. (See 'STATus:OPERation register'.) To continue with the next range, use method RsFsw.Applications.K17_Mcgd.Initiate.ConMeas.set. OFF | 0 The R&S FSW sweeps all ranges in one go."""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BREak?')
		return Conversions.str_to_bool(response)
