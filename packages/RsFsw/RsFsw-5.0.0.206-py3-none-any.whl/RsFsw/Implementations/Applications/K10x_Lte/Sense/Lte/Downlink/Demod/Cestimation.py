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

	def set(self, type_py: enums.ChannelEstDl) -> None:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:CESTimation \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.demod.cestimation.set(type_py = enums.ChannelEstDl.OFF) \n
		This command selects the channel estimation type. \n
			:param type_py: OFF Turns off channel estimation. PIL Optimal, pilot only PILP Optimal, pilot and payload TGPP 3GPP EVM definition
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChannelEstDl)
		self._core.io.write(f'SENSe:LTE:DL:DEMod:CESTimation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelEstDl:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:CESTimation \n
		Snippet: value: enums.ChannelEstDl = driver.applications.k10Xlte.sense.lte.downlink.demod.cestimation.get() \n
		This command selects the channel estimation type. \n
			:return: type_py: OFF Turns off channel estimation. PIL Optimal, pilot only PILP Optimal, pilot and payload TGPP 3GPP EVM definition"""
		response = self._core.io.query_str(f'SENSe:LTE:DL:DEMod:CESTimation?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelEstDl)
