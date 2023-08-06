from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrData:
	"""PrData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prData", core, parent)

	def set(self, reference: enums.Reference) -> None:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:PRData \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.demod.prData.set(reference = enums.Reference.ALL0) \n
		This command selects the type of reference data to calculate the EVM for the PDSCH. \n
			:param reference: AUTO Automatic identification of reference data. ALL0 Reference data is 0, according to the test model definition.
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.Reference)
		self._core.io.write(f'SENSe:LTE:DL:DEMod:PRData {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Reference:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:PRData \n
		Snippet: value: enums.Reference = driver.applications.k10Xlte.sense.lte.downlink.demod.prData.get() \n
		This command selects the type of reference data to calculate the EVM for the PDSCH. \n
			:return: reference: AUTO Automatic identification of reference data. ALL0 Reference data is 0, according to the test model definition."""
		response = self._core.io.query_str(f'SENSe:LTE:DL:DEMod:PRData?')
		return Conversions.str_to_scalar_enum(response, enums.Reference)
