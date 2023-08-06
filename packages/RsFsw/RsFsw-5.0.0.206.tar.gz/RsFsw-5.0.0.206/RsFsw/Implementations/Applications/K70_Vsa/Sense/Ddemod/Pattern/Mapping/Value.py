from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, mapping: str) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:MAPPing[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.mapping.value.set(mapping = '1') \n
		This command selects the mapping for pattern demodulation. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param mapping: To obtain a list of available symbol mappings for the current modulation type use the [SENSe:]DDEMod:PATTern:MAPPing:CATalog?? query.
		"""
		param = Conversions.value_to_quoted_str(mapping)
		self._core.io.write(f'SENSe:DDEMod:PATTern:MAPPing:VALue {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:MAPPing[:VALue] \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.mapping.value.get() \n
		This command selects the mapping for pattern demodulation. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: mapping: To obtain a list of available symbol mappings for the current modulation type use the [SENSe:]DDEMod:PATTern:MAPPing:CATalog?? query."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:MAPPing:VALue?')
		return trim_str_response(response)
