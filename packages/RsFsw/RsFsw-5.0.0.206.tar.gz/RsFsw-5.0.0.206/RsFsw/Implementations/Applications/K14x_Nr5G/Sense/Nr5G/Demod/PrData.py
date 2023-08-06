from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrData:
	"""PrData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prData", core, parent)

	def set(self, reference: enums.ReferenceDataNr5G) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:PRData \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.prData.set(reference = enums.ReferenceDataNr5G.ALL0) \n
		This command selects the PDSCH reference data. \n
			:param reference: AUTO Automatic detection of reference values. ALL0 PDSCH consists of 0's only. PN23 PDSCH based on NR-TM PN23 (pseudo random sequence 23) .
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ReferenceDataNr5G)
		self._core.io.write(f'SENSe:NR5G:DEMod:PRData {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceDataNr5G:
		"""SCPI: [SENSe]:NR5G:DEMod:PRData \n
		Snippet: value: enums.ReferenceDataNr5G = driver.applications.k14Xnr5G.sense.nr5G.demod.prData.get() \n
		This command selects the PDSCH reference data. \n
			:return: reference: AUTO Automatic detection of reference values. ALL0 PDSCH consists of 0's only. PN23 PDSCH based on NR-TM PN23 (pseudo random sequence 23) ."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:PRData?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceDataNr5G)
