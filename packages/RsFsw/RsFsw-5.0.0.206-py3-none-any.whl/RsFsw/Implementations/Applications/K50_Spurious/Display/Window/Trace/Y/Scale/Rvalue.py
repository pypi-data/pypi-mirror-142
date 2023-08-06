from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rvalue:
	"""Rvalue commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvalue", core, parent)

	def set(self, ref_value: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RVALue \n
		Snippet: driver.applications.k50Spurious.display.window.trace.y.scale.rvalue.set(ref_value = 1.0, window = repcap.Window.Default) \n
		This command defines the reference value assigned to the reference position in the specified window. Separate reference
		values are maintained for the various displays. \n
			:param ref_value: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(ref_value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RVALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RVALue \n
		Snippet: value: float = driver.applications.k50Spurious.display.window.trace.y.scale.rvalue.get(window = repcap.Window.Default) \n
		This command defines the reference value assigned to the reference position in the specified window. Separate reference
		values are maintained for the various displays. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: ref_value: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RVALue?')
		return Conversions.str_to_float(response)
