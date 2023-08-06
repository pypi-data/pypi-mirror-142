from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)

	def set(self, text: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:TEXT \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.text.set(text = '1') \n
		This command defines a text to explain the pattern. The text is displayed only in the selection menu (manual control) .
		This text should be short and concise. Detailed information about the pattern is given in the comment (see
		[SENSe:]DDEMod:SEARch:SYNC:COMMent) . \n
			:param text: No help available
		"""
		param = Conversions.value_to_quoted_str(text)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:TEXT {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:TEXT \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.text.get() \n
		This command defines a text to explain the pattern. The text is displayed only in the selection menu (manual control) .
		This text should be short and concise. Detailed information about the pattern is given in the comment (see
		[SENSe:]DDEMod:SEARch:SYNC:COMMent) . \n
			:return: text: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:TEXT?')
		return trim_str_response(response)
