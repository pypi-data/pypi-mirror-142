from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, unit: enums.PowerUnit, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: driver.calculate.unit.power.set(unit = enums.PowerUnit.A, window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DBUa_mhz | DBUV_mhz | DBmV_mhz | DBpW_mhz (Units based on 1 MHz require installed R&S FSW-K54 (EMI measurements) option.)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PowerUnit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PowerUnit:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: value: enums.PowerUnit = driver.calculate.unit.power.get(window = repcap.Window.Default) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DBUa_mhz | DBUV_mhz | DBmV_mhz | DBpW_mhz (Units based on 1 MHz require installed R&S FSW-K54 (EMI measurements) option.)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerUnit)
