from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, once: enums.EventOnce, window=repcap.Window.Default, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: CALCulate<n>:PMETer<p>:RELative[:MAGNitude]:AUTO \n
		Snippet: driver.applications.k14Xnr5G.calculate.pmeter.relative.magnitude.auto.set(once = enums.EventOnce.ONCE, window = repcap.Window.Default, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param once: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(once, enums.EventOnce)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'CALCulate{window_cmd_val}:PMETer{powerMeter_cmd_val}:RELative:MAGNitude:AUTO {param}')
