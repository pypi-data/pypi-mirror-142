from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rl:
	"""Rl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rl", core, parent)

	def set(self, return_loss: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:MATCh:SOURce:CALibration:RL \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.match.source.calibration.rl.set(return_loss = 1.0, window = repcap.Window.Default) \n
		This command defines the return loss at the calibration noise source output. This command is available when
		[SENSe:]CORRection:ENR:COMMon and method RsFsw.Applications.K30_NoiseFigure.Calculate.Uncertainty.Common.set are off. If
		a smart noise source is used, the return loss values defined in the SNS table are used. \n
			:param return_loss: Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(return_loss)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:MATCh:SOURce:CALibration:RL {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:MATCh:SOURce:CALibration:RL \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.match.source.calibration.rl.get(window = repcap.Window.Default) \n
		This command defines the return loss at the calibration noise source output. This command is available when
		[SENSe:]CORRection:ENR:COMMon and method RsFsw.Applications.K30_NoiseFigure.Calculate.Uncertainty.Common.set are off. If
		a smart noise source is used, the return loss values defined in the SNS table are used. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: return_loss: Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:MATCh:SOURce:CALibration:RL?')
		return Conversions.str_to_float(response)
