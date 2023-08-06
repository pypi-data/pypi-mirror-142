from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, mapping: str) -> None:
		"""SCPI: [SENSe]:DDEMod:MAPPing[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.mapping.value.set(mapping = '1') \n
		This command selects the mapping for digital demodulation. The mapping describes the assignment of constellation points
		to symbols. When using PRBS generators, select the _SMx mapping, which corresponds to the mapping used by R&S SMx signal
		generators. \n
			:param mapping: To obtain a list of available symbol mappings for the current modulation type use the [SENSe:]DDEMod:MAPPing:CATalog?? query.
		"""
		param = Conversions.value_to_quoted_str(mapping)
		self._core.io.write(f'SENSe:DDEMod:MAPPing:VALue {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:MAPPing[:VALue] \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.mapping.value.get() \n
		This command selects the mapping for digital demodulation. The mapping describes the assignment of constellation points
		to symbols. When using PRBS generators, select the _SMx mapping, which corresponds to the mapping used by R&S SMx signal
		generators. \n
			:return: mapping: To obtain a list of available symbol mappings for the current modulation type use the [SENSe:]DDEMod:MAPPing:CATalog?? query."""
		response = self._core.io.query_str(f'SENSe:DDEMod:MAPPing:VALue?')
		return trim_str_response(response)
