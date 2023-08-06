from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, fsk_ref_dev_abs_res: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FSK:DEViation:REFerence[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.fsk.deviation.reference.value.set(fsk_ref_dev_abs_res = 1.0, window = repcap.Window.Default) \n
		This command defines the deviation to the reference frequency for FSK modulation as an absolute value in Hz. \n
			:param fsk_ref_dev_abs_res: Range: 10.0 to 256e9, Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(fsk_ref_dev_abs_res)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FSK:DEViation:REFerence:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:FSK:DEViation:REFerence[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.fsk.deviation.reference.value.get(window = repcap.Window.Default) \n
		This command defines the deviation to the reference frequency for FSK modulation as an absolute value in Hz. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: fsk_ref_dev_abs_res: Range: 10.0 to 256e9, Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FSK:DEViation:REFerence:VALue?')
		return Conversions.str_to_float(response)
