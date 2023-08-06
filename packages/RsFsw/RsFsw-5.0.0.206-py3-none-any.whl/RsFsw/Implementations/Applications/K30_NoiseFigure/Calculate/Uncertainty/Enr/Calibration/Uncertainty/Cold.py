from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cold:
	"""Cold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cold", core, parent)

	def set(self, uncertainty: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty:COLD \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.cold.set(uncertainty = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param uncertainty: 1..n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(uncertainty)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty:COLD {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty:COLD \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.cold.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: uncertainty: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty:COLD?')
		return Conversions.str_to_float(response)
