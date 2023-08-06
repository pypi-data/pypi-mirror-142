from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:USER:NAME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.user.name.set(name = '1') \n
		Selects the file that contains a user-defined modulation. For details on user-defined modulation files see 'User-defined
		modulation'. This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is
		installed. The default storage location for user-defined modulations is C:/R_S/INSTR/USER/vsa/Constellation. \n
			:param name: string Path and file name of the *.vam file.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:DDEMod:PATTern:USER:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:USER:NAME \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.user.name.get() \n
		Selects the file that contains a user-defined modulation. For details on user-defined modulation files see 'User-defined
		modulation'. This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is
		installed. The default storage location for user-defined modulations is C:/R_S/INSTR/USER/vsa/Constellation. \n
			:return: name: string Path and file name of the *.vam file."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:USER:NAME?')
		return trim_str_response(response)
