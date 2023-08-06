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

	def set(self, unit: enums.PowerUnitK9x, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: driver.applications.k9X11Ad.calculate.unit.power.set(unit = enums.PowerUnitK9x.A, window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PowerUnitK9x)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PowerUnitK9x:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: value: enums.PowerUnitK9x = driver.applications.k9X11Ad.calculate.unit.power.get(window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerUnitK9x)
