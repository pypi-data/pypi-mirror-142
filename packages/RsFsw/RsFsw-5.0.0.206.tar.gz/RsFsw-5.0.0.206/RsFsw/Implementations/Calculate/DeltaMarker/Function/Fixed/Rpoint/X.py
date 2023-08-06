from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, ref_point: float, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed:RPOint:X \n
		Snippet: driver.calculate.deltaMarker.function.fixed.rpoint.x.set(ref_point = 1.0, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command defines the horizontal position of the fixed delta marker reference point. The coordinates of the reference
		may be anywhere in the diagram. \n
			:param ref_point: Numeric value that defines the horizontal position of the reference. For frequency domain measurements, it is a frequency in Hz. For time domain measurements, it is a point in time in s. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.decimal_value_to_str(ref_point)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:RPOint:X {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed:RPOint:X \n
		Snippet: value: float = driver.calculate.deltaMarker.function.fixed.rpoint.x.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command defines the horizontal position of the fixed delta marker reference point. The coordinates of the reference
		may be anywhere in the diagram. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: ref_point: Numeric value that defines the horizontal position of the reference. For frequency domain measurements, it is a frequency in Hz. For time domain measurements, it is a point in time in s. Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:RPOint:X?')
		return Conversions.str_to_float(response)
