from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	def set(self, ref_level: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:RLEVel \n
		Snippet: driver.calculate.statistics.scale.x.refLevel.set(ref_level = 1.0, window = repcap.Window.Default) \n
		This command sets the reference level for statistical measurements. The effects are identical to method RsFsw.
		Applications.K17_Mcgd.Display.Window.Trace.Y.Scale.RefLevel.set. Note that in case of statistical measurements the
		reference level applies to the x-axis. \n
			:param ref_level: The unit is variable. If a reference level offset is included, the range is adjusted by that offset. Range: -130 dBm to 30 dBm, Unit: dBm
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(ref_level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:RLEVel {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:RLEVel \n
		Snippet: value: float = driver.calculate.statistics.scale.x.refLevel.get(window = repcap.Window.Default) \n
		This command sets the reference level for statistical measurements. The effects are identical to method RsFsw.
		Applications.K17_Mcgd.Display.Window.Trace.Y.Scale.RefLevel.set. Note that in case of statistical measurements the
		reference level applies to the x-axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: ref_level: The unit is variable. If a reference level offset is included, the range is adjusted by that offset. Range: -130 dBm to 30 dBm, Unit: dBm"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:RLEVel?')
		return Conversions.str_to_float(response)
