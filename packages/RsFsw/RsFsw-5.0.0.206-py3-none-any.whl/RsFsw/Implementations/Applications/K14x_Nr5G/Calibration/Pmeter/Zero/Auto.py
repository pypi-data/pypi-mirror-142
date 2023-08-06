from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, once: enums.EventOnce, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: CALibration:PMETer<p>:ZERO:AUTO \n
		Snippet: driver.applications.k14Xnr5G.calibration.pmeter.zero.auto.set(once = enums.EventOnce.ONCE, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param once: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(once, enums.EventOnce)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'CALibration:PMETer{powerMeter_cmd_val}:ZERO:AUTO {param}')
