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

	def set(self, vert_line_abs_pos: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TLABs[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.tlAbs.value.set(vert_line_abs_pos = 1.0, window = repcap.Window.Default) \n
		Defines or queries the x-value of the absolute vertical line in the specified window. This command is only available for
		eye diagrams, and only if an absolute vertical line is already available in the diagram (see method RsFsw.Applications.
		K70_Vsa.Calculate.TlAbs.State.set) . \n
			:param vert_line_abs_pos: numeric value X-value of the absolute vertical line. Range: -1e9 to 1e9, Unit: Sym
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(vert_line_abs_pos)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TLABs:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:TLABs[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.tlAbs.value.get(window = repcap.Window.Default) \n
		Defines or queries the x-value of the absolute vertical line in the specified window. This command is only available for
		eye diagrams, and only if an absolute vertical line is already available in the diagram (see method RsFsw.Applications.
		K70_Vsa.Calculate.TlAbs.State.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: vert_line_abs_pos: numeric value X-value of the absolute vertical line. Range: -1e9 to 1e9, Unit: Sym"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TLABs:VALue?')
		return Conversions.str_to_float(response)
