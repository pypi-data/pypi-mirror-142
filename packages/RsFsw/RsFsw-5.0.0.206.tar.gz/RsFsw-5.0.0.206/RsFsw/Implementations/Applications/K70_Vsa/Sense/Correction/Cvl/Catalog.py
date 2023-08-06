from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:CATalog \n
		Snippet: value: str = driver.applications.k70Vsa.sense.correction.cvl.catalog.get() \n
		This command queries all available conversion loss tables saved in the C:/R_S/INSTR/USER/cvl/ directory on the instrument.
		This command is only available with option B21 (External Mixer) installed. \n
			:return: files: 'string' Comma-separated list of strings containing the file names."""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:CATalog?')
		return trim_str_response(response)
