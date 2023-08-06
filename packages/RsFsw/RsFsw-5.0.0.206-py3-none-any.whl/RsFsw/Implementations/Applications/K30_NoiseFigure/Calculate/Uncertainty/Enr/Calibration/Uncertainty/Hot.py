from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hot:
	"""Hot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hot", core, parent)

	def set(self, uncertainty: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty:HOT \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.hot.set(uncertainty = 1.0, window = repcap.Window.Default) \n
		This command defines the uncertainty of a calibration noise source.
		This command is available when [SENSe:]CORRection:ENR:COMMon and method RsFsw.Applications.K30_NoiseFigure.Calculate.
		Uncertainty.Common.set are off. \n
			:param uncertainty: Hot temperature uncertainty value of the noise source. Refer to the data sheet of the noise source to determine its uncertainty.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(uncertainty)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty:HOT {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty:HOT \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.hot.get(window = repcap.Window.Default) \n
		This command defines the uncertainty of a calibration noise source.
		This command is available when [SENSe:]CORRection:ENR:COMMon and method RsFsw.Applications.K30_NoiseFigure.Calculate.
		Uncertainty.Common.set are off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: uncertainty: Hot temperature uncertainty value of the noise source. Refer to the data sheet of the noise source to determine its uncertainty."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty:HOT?')
		return Conversions.str_to_float(response)
