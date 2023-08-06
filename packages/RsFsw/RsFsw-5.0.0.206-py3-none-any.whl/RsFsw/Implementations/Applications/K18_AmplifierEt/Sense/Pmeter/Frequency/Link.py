from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, coupling: enums.PmeterFreqLink) -> None:
		"""SCPI: [SENSe]:PMETer:FREQuency:LINK \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.frequency.link.set(coupling = enums.PmeterFreqLink.CENTer) \n
		This command selects the frequency coupling for power sensor measurements. \n
			:param coupling: CENTer Couples the frequency to the center frequency of the analyzer MARKer1 Couples the frequency to the position of marker 1 OFF Switches the frequency coupling off
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.PmeterFreqLink)
		self._core.io.write(f'SENSe:PMETer:FREQuency:LINK {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PmeterFreqLink:
		"""SCPI: [SENSe]:PMETer:FREQuency:LINK \n
		Snippet: value: enums.PmeterFreqLink = driver.applications.k18AmplifierEt.sense.pmeter.frequency.link.get() \n
		This command selects the frequency coupling for power sensor measurements. \n
			:return: coupling: CENTer Couples the frequency to the center frequency of the analyzer MARKer1 Couples the frequency to the position of marker 1 OFF Switches the frequency coupling off"""
		response = self._core.io.query_str(f'SENSe:PMETer:FREQuency:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.PmeterFreqLink)
