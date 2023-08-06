from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN:STATe \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.inputPy.gain.state.set(state = False, rangePy = repcap.RangePy.Default) \n
		Switches the optional preamplifier on or off (if available) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the preamplifier off ON | 1 Switches the preamplifier on
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN:STATe \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.listPy.range.inputPy.gain.state.get(rangePy = repcap.RangePy.Default) \n
		Switches the optional preamplifier on or off (if available) . \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the preamplifier off ON | 1 Switches the preamplifier on"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe?')
		return Conversions.str_to_bool(response)
