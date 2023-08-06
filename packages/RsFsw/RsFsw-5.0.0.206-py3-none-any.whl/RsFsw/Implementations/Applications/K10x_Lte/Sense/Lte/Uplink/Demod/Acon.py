from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acon:
	"""Acon commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acon", core, parent)

	def set(self, type_py: enums.AutoDemodType) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:ACON \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.acon.set(type_py = enums.AutoDemodType.ALL) \n
		This command selects the method of automatic demodulation. \n
			:param type_py: ALL Automatically detects and demodulates the PUSCH and SRS. OFF Automatic demodulation is off. SCON Automatically detects and demodulates the values available in the subframe configuration table.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.AutoDemodType)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:ACON {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoDemodType:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:ACON \n
		Snippet: value: enums.AutoDemodType = driver.applications.k10Xlte.sense.lte.uplink.demod.acon.get() \n
		This command selects the method of automatic demodulation. \n
			:return: type_py: ALL Automatically detects and demodulates the PUSCH and SRS. OFF Automatic demodulation is off. SCON Automatically detects and demodulates the values available in the subframe configuration table."""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:ACON?')
		return Conversions.str_to_scalar_enum(response, enums.AutoDemodType)
