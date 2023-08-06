from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:USER:NAME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.user.name.set(filename = '1') \n
		Selects the file that contains the user-defined modulation to be loaded. \n
			:param filename: Path and file name of the *.vam file The default storage location for user-defined modulations is C:/R_S/INSTR/USER/vsa/Constellation.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:USER:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:USER:NAME \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.user.name.get() \n
		Selects the file that contains the user-defined modulation to be loaded. \n
			:return: filename: Path and file name of the *.vam file The default storage location for user-defined modulations is C:/R_S/INSTR/USER/vsa/Constellation."""
		response = self._core.io.query_str(f'SENSe:DDEMod:USER:NAME?')
		return trim_str_response(response)
