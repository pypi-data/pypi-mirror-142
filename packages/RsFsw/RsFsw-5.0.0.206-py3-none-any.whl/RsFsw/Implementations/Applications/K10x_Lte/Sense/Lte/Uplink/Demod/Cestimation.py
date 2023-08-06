from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cestimation:
	"""Cestimation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cestimation", core, parent)

	def set(self, type_py: enums.ChannelEstUl) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:CESTimation \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.cestimation.set(type_py = enums.ChannelEstUl.PIL) \n
		This command selects the channel estimation type. \n
			:param type_py: PIL Pilot only PILP Pilot and payload
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChannelEstUl)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:CESTimation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelEstUl:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:CESTimation \n
		Snippet: value: enums.ChannelEstUl = driver.applications.k10Xlte.sense.lte.uplink.demod.cestimation.get() \n
		This command selects the channel estimation type. \n
			:return: type_py: PIL Pilot only PILP Pilot and payload"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:CESTimation?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelEstUl)
