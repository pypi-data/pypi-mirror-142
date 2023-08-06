from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:COMMent \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.comment.set(comment = '1') \n
		This command enters the comment for a new standard. The comment is stored with the standard and is only displayed in the
		selection menu (manual operation) . In remote control, the string is deleted after the standard has been stored, allowing
		a new comment to be entered for the next standard. In this case a blank string is returned when for the query. \n
			:param comment: No help available
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'SENSe:DDEMod:STANdard:COMMent {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:STANdard:COMMent \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.standard.comment.get() \n
		This command enters the comment for a new standard. The comment is stored with the standard and is only displayed in the
		selection menu (manual operation) . In remote control, the string is deleted after the standard has been stored, allowing
		a new comment to be entered for the next standard. In this case a blank string is returned when for the query. \n
			:return: comment: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:STANdard:COMMent?')
		return trim_str_response(response)
