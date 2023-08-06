from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:COMMon \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.common.set(state = False, window = repcap.Window.Default) \n
		This command turns matching of the noise source characteristics used during calibration and measurement on and off. This
		command is available when you use different noise sources for calibration and measurement ([SENSe:]CORRection:ENR:COMMon
		OFF) . \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:COMMon {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:UNCertainty:COMMon \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.calculate.uncertainty.common.get(window = repcap.Window.Default) \n
		This command turns matching of the noise source characteristics used during calibration and measurement on and off. This
		command is available when you use different noise sources for calibration and measurement ([SENSe:]CORRection:ENR:COMMon
		OFF) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:COMMon?')
		return Conversions.str_to_bool(response)
