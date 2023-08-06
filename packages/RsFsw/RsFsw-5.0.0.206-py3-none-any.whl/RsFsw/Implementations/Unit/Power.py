from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, unit: enums.PowerUnit) -> None:
		"""SCPI: UNIT:POWer \n
		Snippet: driver.unit.power.set(unit = enums.PowerUnit.A) \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:param unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DBUa_mhz | DBUV_mhz | DBmV_mhz | DBpW_mhz (Units based on 1 MHz require installed R&S FSW-K54 (EMI measurements) option.)
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PowerUnit)
		self._core.io.write(f'UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerUnit:
		"""SCPI: UNIT:POWer \n
		Snippet: value: enums.PowerUnit = driver.unit.power.get() \n
		This command selects the unit of the y-axis. The unit applies to all power-based measurement windows with absolute values. \n
			:return: unit: DBM | V | A | W | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DBUa_mhz | DBUV_mhz | DBmV_mhz | DBpW_mhz (Units based on 1 MHz require installed R&S FSW-K54 (EMI measurements) option.)"""
		response = self._core.io.query_str(f'UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerUnit)
