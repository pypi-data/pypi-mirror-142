from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoLocation:
	"""LoLocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loLocation", core, parent)

	def set(self, location: enums.LoscLocation) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:LOLocation \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.loLocation.set(location = enums.LoscLocation.CACB) \n
		This command selects the location of the local oscillator in a system with contiguous aggregated carriers. \n
			:param location: CACB LO is at the center of the aggregated channel bandwidth. CCC One LO is at the center of each component carrier. USER One LO is used for all component carriers. The frequency is not necessarily at the center of the aggregated channel bandwidth. You can define the LO frequency with .
		"""
		param = Conversions.enum_scalar_to_str(location, enums.LoscLocation)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:LOLocation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LoscLocation:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:LOLocation \n
		Snippet: value: enums.LoscLocation = driver.applications.k10Xlte.sense.lte.uplink.demod.loLocation.get() \n
		This command selects the location of the local oscillator in a system with contiguous aggregated carriers. \n
			:return: location: CACB LO is at the center of the aggregated channel bandwidth. CCC One LO is at the center of each component carrier. USER One LO is used for all component carriers. The frequency is not necessarily at the center of the aggregated channel bandwidth. You can define the LO frequency with ."""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:LOLocation?')
		return Conversions.str_to_scalar_enum(response, enums.LoscLocation)
