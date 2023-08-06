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
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:PERRor:PMEan:VALue \n
		Snippet: driver.applications.k70Vsa.calculate.limit.maccuracy.perror.pmean.value.set(limit_value = 1.0, window = repcap.Window.Default) \n
		This command defines the value for the current, peak or mean phase error (peak or RMS) limit. Note that the limits for
		the current and the peak value are always kept identical. \n
			:param limit_value: the value x (x0) defines the interval [-x; x] Range: 0.0 to 360, Unit: deg
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(limit_value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:PERRor:PMEan:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:PERRor:PMEan:VALue \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.limit.maccuracy.perror.pmean.value.get(window = repcap.Window.Default) \n
		This command defines the value for the current, peak or mean phase error (peak or RMS) limit. Note that the limits for
		the current and the peak value are always kept identical. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: limit_value: the value x (x0) defines the interval [-x; x] Range: 0.0 to 360, Unit: deg"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:PERRor:PMEan:VALue?')
		return Conversions.str_to_float(response)
