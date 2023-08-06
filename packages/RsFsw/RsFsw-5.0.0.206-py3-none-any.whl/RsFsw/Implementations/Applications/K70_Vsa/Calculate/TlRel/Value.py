from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, line_rel_pos_rel: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TLRel[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.tlRel.value.set(line_rel_pos_rel = 1.0, window = repcap.Window.Default) \n
		Defines or queries the x-value of the relative vertical line in the specified window. This command is only available for
		eye diagrams, and only if an absolute vertical line and a relative vertical line are already available in the same
		diagram (see method RsFsw.Applications.K70_Vsa.Calculate.TlAbs.State.set and method RsFsw.Applications.K70_Vsa.Calculate.
		TlRel.State.set) . \n
			:param line_rel_pos_rel: Relative distance of the second vertical line to the first (absolute) vertical line. Unit: SYMB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(line_rel_pos_rel)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TLRel:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:TLRel[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.tlRel.value.get(window = repcap.Window.Default) \n
		Defines or queries the x-value of the relative vertical line in the specified window. This command is only available for
		eye diagrams, and only if an absolute vertical line and a relative vertical line are already available in the same
		diagram (see method RsFsw.Applications.K70_Vsa.Calculate.TlAbs.State.set and method RsFsw.Applications.K70_Vsa.Calculate.
		TlRel.State.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: line_rel_pos_rel: Relative distance of the second vertical line to the first (absolute) vertical line. Unit: SYMB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TLRel:VALue?')
		return Conversions.str_to_float(response)
