from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, percent: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:PDEViation:LENGth \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.pdeviation.length.set(percent = 1.0, window = repcap.Window.Default) \n
		Defines the length of the measurement range for frequency results in percent of the hop's dwell time. This command is
		only available if the reference is CENT (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Pdeviation.
		Reference.set) . For details on the measurement range parameters see 'Measurement range'. \n
			:param percent: percent of the hop dwell time Range: 0 to 100
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(percent)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:PDEViation:LENGth {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:HOPDetection:PDEViation:LENGth \n
		Snippet: value: float = driver.applications.k60Transient.calculate.hopDetection.pdeviation.length.get(window = repcap.Window.Default) \n
		Defines the length of the measurement range for frequency results in percent of the hop's dwell time. This command is
		only available if the reference is CENT (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Pdeviation.
		Reference.set) . For details on the measurement range parameters see 'Measurement range'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: percent: percent of the hop dwell time Range: 0 to 100"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:PDEViation:LENGth?')
		return Conversions.str_to_float(response)
