from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, eval_mode: enums.EvaluationMode, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:IQ:MODE \n
		Snippet: driver.calculate.iq.mode.set(eval_mode = enums.EvaluationMode.FDOMain, window = repcap.Window.Default) \n
		This command defines whether the captured I/Q data is evaluated directly, or if it is converted (via FFT) to spectral or
		time data first. It is currently only available for I/Q Analyzer secondary applications in multistandard mode (not the
		MSRA primary application) . \n
			:param eval_mode: TDOMain Evaluation in time domain (zero span) . FDOMain Evaluation in frequency domain. IQ Evaluation using I/Q data.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(eval_mode, enums.EvaluationMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:IQ:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.EvaluationMode:
		"""SCPI: CALCulate<n>:IQ:MODE \n
		Snippet: value: enums.EvaluationMode = driver.calculate.iq.mode.get(window = repcap.Window.Default) \n
		This command defines whether the captured I/Q data is evaluated directly, or if it is converted (via FFT) to spectral or
		time data first. It is currently only available for I/Q Analyzer secondary applications in multistandard mode (not the
		MSRA primary application) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: eval_mode: TDOMain Evaluation in time domain (zero span) . FDOMain Evaluation in frequency domain. IQ Evaluation using I/Q data."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:IQ:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluationMode)
