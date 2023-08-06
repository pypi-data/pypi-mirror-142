from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, text: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:COMMent \n
		Snippet: driver.sense.correction.cvl.comment.set(text = '1') \n
		This command defines a comment for the conversion loss table. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External
		Mixer) installed. \n
			:param text: No help available
		"""
		param = Conversions.value_to_quoted_str(text)
		self._core.io.write(f'SENSe:CORRection:CVL:COMMent {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:COMMent \n
		Snippet: value: str = driver.sense.correction.cvl.comment.get() \n
		This command defines a comment for the conversion loss table. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External
		Mixer) installed. \n
			:return: text: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:COMMent?')
		return trim_str_response(response)
