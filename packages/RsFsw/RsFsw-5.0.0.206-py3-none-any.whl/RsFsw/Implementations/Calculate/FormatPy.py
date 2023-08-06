from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, evaluation: enums.EvaluationFormat, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FORMat \n
		Snippet: driver.calculate.formatPy.set(evaluation = enums.EvaluationFormat.CCDF, window = repcap.Window.Default) \n
		This command selects the evaluation method of the measured data that is to be displayed in the specified window.
		Note that for the I/Q analyzer application, this command is maintained for compatibility reasons only. Use the LAYout
		commands for new remote control programs (see 'Working with windows in the display') . See ''Phase Wrap On/Off (PM Time
		Domain only) ''. \n
			:param evaluation: Type of evaluation you want to display. See the table below for available parameter values.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(evaluation, enums.EvaluationFormat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.EvaluationFormat:
		"""SCPI: CALCulate<n>:FORMat \n
		Snippet: value: enums.EvaluationFormat = driver.calculate.formatPy.get(window = repcap.Window.Default) \n
		This command selects the evaluation method of the measured data that is to be displayed in the specified window.
		Note that for the I/Q analyzer application, this command is maintained for compatibility reasons only. Use the LAYout
		commands for new remote control programs (see 'Working with windows in the display') . See ''Phase Wrap On/Off (PM Time
		Domain only) ''. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: evaluation: Type of evaluation you want to display. See the table below for available parameter values."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluationFormat)
