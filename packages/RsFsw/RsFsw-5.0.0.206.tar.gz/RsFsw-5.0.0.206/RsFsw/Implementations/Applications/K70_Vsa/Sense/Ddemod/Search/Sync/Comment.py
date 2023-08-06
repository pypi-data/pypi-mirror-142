from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:COMMent \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.comment.set(comment = '1') \n
		This command defines a comment to a sync pattern. The pattern must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. \n
			:param comment: No help available
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:COMMent {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:COMMent \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.comment.get() \n
		This command defines a comment to a sync pattern. The pattern must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. \n
			:return: comment: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:COMMent?')
		return trim_str_response(response)
