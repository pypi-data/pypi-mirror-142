from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, unit: enums.PowerUnitDdem, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: driver.applications.k70Vsa.calculate.unit.power.set(unit = enums.PowerUnitDdem.DBM, window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param unit: irrelevant
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PowerUnitDdem)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PowerUnitDdem:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: value: enums.PowerUnitDdem = driver.applications.k70Vsa.calculate.unit.power.get(window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerUnitDdem)
