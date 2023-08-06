from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, unit: enums.TimeLimitUnit, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:X:UNIT:TIME \n
		Snippet: driver.applications.k70Vsa.calculate.x.unit.time.set(unit = enums.TimeLimitUnit.S, window = repcap.Window.Default) \n
		No command help available \n
			:param unit: S | SYM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.TimeLimitUnit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:X:UNIT:TIME {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.TimeLimitUnit:
		"""SCPI: CALCulate<n>:X:UNIT:TIME \n
		Snippet: value: enums.TimeLimitUnit = driver.applications.k70Vsa.calculate.x.unit.time.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: S | SYM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:X:UNIT:TIME?')
		return Conversions.str_to_scalar_enum(response, enums.TimeLimitUnit)
