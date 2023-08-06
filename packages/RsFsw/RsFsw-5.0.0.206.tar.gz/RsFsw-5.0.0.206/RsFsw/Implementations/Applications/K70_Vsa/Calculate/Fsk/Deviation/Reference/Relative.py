from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, fsk_ref_dev: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FSK:DEViation:REFerence:RELative \n
		Snippet: driver.applications.k70Vsa.calculate.fsk.deviation.reference.relative.set(fsk_ref_dev = 1.0, window = repcap.Window.Default) \n
		This command defines the deviation to the reference frequency for FSK modulation as a multiple of the symbol rate. \n
			:param fsk_ref_dev: Range: 0.1 to 60, Unit: none
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(fsk_ref_dev)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FSK:DEViation:REFerence:RELative {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:FSK:DEViation:REFerence:RELative \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.fsk.deviation.reference.relative.get(window = repcap.Window.Default) \n
		This command defines the deviation to the reference frequency for FSK modulation as a multiple of the symbol rate. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: fsk_ref_dev: Range: 0.1 to 60, Unit: none"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FSK:DEViation:REFerence:RELative?')
		return Conversions.str_to_float(response)
