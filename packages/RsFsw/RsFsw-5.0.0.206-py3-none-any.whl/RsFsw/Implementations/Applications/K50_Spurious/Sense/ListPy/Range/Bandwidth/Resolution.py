from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, rbw: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth[:RESolution] \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.bandwidth.resolution.set(rbw = 1.0, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param rbw: Range: 1 Hz to 10 MHz , Unit: HZ
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(rbw)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:RESolution {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth[:RESolution] \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.bandwidth.resolution.get(rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: rbw: Range: 1 Hz to 10 MHz , Unit: HZ"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:RESolution?')
		return Conversions.str_to_float(response)
