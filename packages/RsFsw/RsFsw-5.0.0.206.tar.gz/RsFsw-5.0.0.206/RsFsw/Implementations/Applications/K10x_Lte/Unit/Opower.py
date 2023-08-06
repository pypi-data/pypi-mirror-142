from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Opower:
	"""Opower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("opower", core, parent)

	def set(self, unit: enums.OffPowerUnit) -> None:
		"""SCPI: UNIT:OPOWer \n
		Snippet: driver.applications.k10Xlte.unit.opower.set(unit = enums.OffPowerUnit.DBM) \n
		This command selects the unit the off power (transmit on / off power measurements) is displayed in. \n
			:param unit: DBM Displays the power as an absolute value in dBm. DMHZ Displays the power as a relative value in dBm/MHz.
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.OffPowerUnit)
		self._core.io.write(f'UNIT:OPOWer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OffPowerUnit:
		"""SCPI: UNIT:OPOWer \n
		Snippet: value: enums.OffPowerUnit = driver.applications.k10Xlte.unit.opower.get() \n
		This command selects the unit the off power (transmit on / off power measurements) is displayed in. \n
			:return: unit: DBM Displays the power as an absolute value in dBm. DMHZ Displays the power as a relative value in dBm/MHz."""
		response = self._core.io.query_str(f'UNIT:OPOWer?')
		return Conversions.str_to_scalar_enum(response, enums.OffPowerUnit)
