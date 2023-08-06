from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, limit_value: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:EVM:PCURrent:VALue \n
		Snippet: driver.applications.k70Vsa.calculate.limit.maccuracy.evm.pcurrent.value.set(limit_value = 1.0, window = repcap.Window.Default) \n
		This command defines the value for the current, peak or mean EVM (peak or RMS) limit. Note that the limits for the
		current and the peak value are always kept identical. \n
			:param limit_value: Range: 0.0 to 100, Unit: %
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(limit_value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:EVM:PCURrent:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:EVM:PCURrent:VALue \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.limit.maccuracy.evm.pcurrent.value.get(window = repcap.Window.Default) \n
		This command defines the value for the current, peak or mean EVM (peak or RMS) limit. Note that the limits for the
		current and the peak value are always kept identical. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: limit_value: Range: 0.0 to 100, Unit: %"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:EVM:PCURrent:VALue?')
		return Conversions.str_to_float(response)
