from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RLEVel:OFFSet \n
		Snippet: driver.applications.k60Transient.display.window.trace.y.scale.refLevel.offset.set(offset = 1.0, window = repcap.Window.Default) \n
		This command defines a reference level offset (for all traces in all windows) . \n
			:param offset: Range: -200 dB to 200 dB, Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(offset)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RLEVel:OFFSet {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RLEVel:OFFSet \n
		Snippet: value: float = driver.applications.k60Transient.display.window.trace.y.scale.refLevel.offset.get(window = repcap.Window.Default) \n
		This command defines a reference level offset (for all traces in all windows) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: offset: Range: -200 dB to 200 dB, Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RLEVel:OFFSet?')
		return Conversions.str_to_float(response)
