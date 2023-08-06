from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SRATe \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.symbolRate.get() \n
		This command returns the sample rate set up for current measurement settings. \n
			:return: sample_rate: Current sample rate used by the application."""
		response = self._core.io.query_str(f'SENSe:SRATe?')
		return Conversions.str_to_float(response)
