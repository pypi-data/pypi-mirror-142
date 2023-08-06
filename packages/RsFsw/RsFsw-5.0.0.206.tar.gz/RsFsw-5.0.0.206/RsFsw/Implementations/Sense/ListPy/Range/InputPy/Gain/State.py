from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN:STATe \n
		Snippet: driver.sense.listPy.range.inputPy.gain.state.set(state = False, rangePy = repcap.RangePy.Default) \n
		This command turns the preamplifier for a spurious emission measurement range on and off. The gain level is defined by
		[SENSe:]LIST:RANGe<ri>:INPut:GAIN[:VALue]. The sweep list cannot be configured using remote commands during an on-going
		sweep operation. \n
			:param state: ON | OFF | 1 | 0
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN:STATe \n
		Snippet: value: bool = driver.sense.listPy.range.inputPy.gain.state.get(rangePy = repcap.RangePy.Default) \n
		This command turns the preamplifier for a spurious emission measurement range on and off. The gain level is defined by
		[SENSe:]LIST:RANGe<ri>:INPut:GAIN[:VALue]. The sweep list cannot be configured using remote commands during an on-going
		sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | OFF | 1 | 0"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe?')
		return Conversions.str_to_bool(response)
