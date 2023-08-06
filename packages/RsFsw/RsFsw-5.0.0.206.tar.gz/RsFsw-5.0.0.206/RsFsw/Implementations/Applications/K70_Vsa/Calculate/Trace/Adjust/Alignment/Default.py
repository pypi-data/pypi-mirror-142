from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self, alignment: enums.AdjustAlignment, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust:ALIGnment[:DEFault] \n
		Snippet: driver.applications.k70Vsa.calculate.trace.adjust.alignment.default.set(alignment = enums.AdjustAlignment.CENTer, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines where the reference point is to appear in the result range. \n
			:param alignment: LEFT | CENTer | RIGHt LEFT The reference point is at the start of the result range. CENTer The reference point is in the middle of the result range. RIGHt The reference point is displayed at the end of the result range.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(alignment, enums.AdjustAlignment)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:ALIGnment:DEFault {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.AdjustAlignment:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust:ALIGnment[:DEFault] \n
		Snippet: value: enums.AdjustAlignment = driver.applications.k70Vsa.calculate.trace.adjust.alignment.default.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines where the reference point is to appear in the result range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: alignment: LEFT | CENTer | RIGHt LEFT The reference point is at the start of the result range. CENTer The reference point is in the middle of the result range. RIGHt The reference point is displayed at the end of the result range."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:ALIGnment:DEFault?')
		return Conversions.str_to_scalar_enum(response, enums.AdjustAlignment)
