from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:SELect \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.select.set(filename = '1') \n
		This command selects a predefined sync pattern file. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:SELect {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:SELect \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.select.get() \n
		This command selects a predefined sync pattern file. \n
			:return: filename: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:SELect?')
		return trim_str_response(response)
