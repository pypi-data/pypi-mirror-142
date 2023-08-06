from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, unit: enums.ScaleYaxisUnit, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:Y:UNIT \n
		Snippet: driver.calculate.statistics.scale.y.unit.set(unit = enums.ScaleYaxisUnit.ABS, window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. \n
			:param unit: PCT | ABS
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.ScaleYaxisUnit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:Y:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ScaleYaxisUnit:
		"""SCPI: CALCulate<n>:STATistics:SCALe:Y:UNIT \n
		Snippet: value: enums.ScaleYaxisUnit = driver.calculate.statistics.scale.y.unit.get(window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: PCT | ABS"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:SCALe:Y:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.ScaleYaxisUnit)
