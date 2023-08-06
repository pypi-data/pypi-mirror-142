from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str) -> None:
		"""SCPI: MMEMory:COMMent \n
		Snippet: driver.massMemory.comment.set(comment = '1') \n
		This command defines a comment for the stored settings. \n
			:param comment: String containing the comment.
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'MMEMory:COMMent {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:COMMent \n
		Snippet: value: str = driver.massMemory.comment.get() \n
		This command defines a comment for the stored settings. \n
			:return: comment: String containing the comment."""
		response = self._core.io.query_str(f'MMEMory:COMMent?')
		return trim_str_response(response)
