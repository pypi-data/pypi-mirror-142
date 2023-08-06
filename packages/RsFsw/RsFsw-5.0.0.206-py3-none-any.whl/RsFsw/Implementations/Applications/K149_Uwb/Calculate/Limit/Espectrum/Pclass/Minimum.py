from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, min_py: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>:MINimum \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.pclass.minimum.set(min_py = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param min_py: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.decimal_value_to_str(min_py)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:MINimum {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>:MINimum \n
		Snippet: value: float = driver.applications.k149Uwb.calculate.limit.espectrum.pclass.minimum.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: min_py: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:MINimum?')
		return Conversions.str_to_float(response)
