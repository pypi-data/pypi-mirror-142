from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)

	def set(self, unit: enums.AngleUnit, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:ANGLe \n
		Snippet: driver.calculate.unit.angle.set(unit = enums.AngleUnit.DEG, window = repcap.Window.Default) \n
		This command selects the unit for angles (for PM display, <n> is irrelevant) . This command is identical to method RsFsw.
		Calculate.Unit.Angle.set \n
			:param unit: DEG | RAD
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.AngleUnit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:ANGLe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AngleUnit:
		"""SCPI: CALCulate<n>:UNIT:ANGLe \n
		Snippet: value: enums.AngleUnit = driver.calculate.unit.angle.get(window = repcap.Window.Default) \n
		This command selects the unit for angles (for PM display, <n> is irrelevant) . This command is identical to method RsFsw.
		Calculate.Unit.Angle.set \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: DEG | RAD"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.AngleUnit)
