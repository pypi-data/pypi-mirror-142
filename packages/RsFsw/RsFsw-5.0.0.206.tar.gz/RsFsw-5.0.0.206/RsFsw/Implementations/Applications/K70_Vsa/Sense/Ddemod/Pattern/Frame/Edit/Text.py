from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:TEXT \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.text.set(filename = '1') \n
		Defines the description for the frame structure in a previously loaded file. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. Note that the file must be loaded for editing
		before the description can be defined using this command (see [SENSe:]DDEMod:PATTern:FRAMe:EDIT) . \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:TEXT {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:TEXT \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.text.get() \n
		Defines the description for the frame structure in a previously loaded file. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. Note that the file must be loaded for editing
		before the description can be defined using this command (see [SENSe:]DDEMod:PATTern:FRAMe:EDIT) . \n
			:return: filename: string"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:TEXT?')
		return trim_str_response(response)
