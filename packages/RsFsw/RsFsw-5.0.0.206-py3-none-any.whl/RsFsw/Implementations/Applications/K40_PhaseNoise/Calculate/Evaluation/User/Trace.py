from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace: enums.TraceTypeIxNone, window=repcap.Window.Default, userRange=repcap.UserRange.Default) -> None:
		"""SCPI: CALCulate<n>:EVALuation:USER<res>:TRACe \n
		Snippet: driver.applications.k40PhaseNoise.calculate.evaluation.user.trace.set(trace = enums.TraceTypeIxNone.NONE, window = repcap.Window.Default, userRange = repcap.UserRange.Default) \n
		This command selects the trace for a custom residual noise calculation range. \n
			:param trace: NONE | TRACe1 | TRACe2 | TRACe3 | TRACe4 | TRACe5 | TRACe6 TRACE1 ... TRACE6 Trace to assign the user range to. NONE Turns a user range off.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param userRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(trace, enums.TraceTypeIxNone)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		userRange_cmd_val = self._cmd_group.get_repcap_cmd_value(userRange, repcap.UserRange)
		self._core.io.write(f'CALCulate{window_cmd_val}:EVALuation:USER{userRange_cmd_val}:TRACe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, userRange=repcap.UserRange.Default) -> enums.TraceTypeIxNone:
		"""SCPI: CALCulate<n>:EVALuation:USER<res>:TRACe \n
		Snippet: value: enums.TraceTypeIxNone = driver.applications.k40PhaseNoise.calculate.evaluation.user.trace.get(window = repcap.Window.Default, userRange = repcap.UserRange.Default) \n
		This command selects the trace for a custom residual noise calculation range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param userRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: trace: NONE | TRACe1 | TRACe2 | TRACe3 | TRACe4 | TRACe5 | TRACe6 TRACE1 ... TRACE6 Trace to assign the user range to. NONE Turns a user range off."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		userRange_cmd_val = self._cmd_group.get_repcap_cmd_value(userRange, repcap.UserRange)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:EVALuation:USER{userRange_cmd_val}:TRACe?')
		return Conversions.str_to_scalar_enum(response, enums.TraceTypeIxNone)
