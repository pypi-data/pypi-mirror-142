from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoFrequency:
	"""LoFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loFrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:LOFRequency \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.loFrequency.set(frequency = 1.0) \n
		This command defines the LO frequency when its location is not at the center of the channel bandwidth.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom LO location ([SENSe:][LTE:]UL:DEMod:LOLocation) . \n
			:param frequency: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:LOFRequency {param}')

	def get(self) -> float:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:LOFRequency \n
		Snippet: value: float = driver.applications.k10Xlte.sense.lte.uplink.demod.loFrequency.get() \n
		This command defines the LO frequency when its location is not at the center of the channel bandwidth.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom LO location ([SENSe:][LTE:]UL:DEMod:LOLocation) . \n
			:return: frequency: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:LOFRequency?')
		return Conversions.str_to_float(response)
