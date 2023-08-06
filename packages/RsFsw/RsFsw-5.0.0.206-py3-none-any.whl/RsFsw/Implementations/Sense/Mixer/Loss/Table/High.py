from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: driver.sense.mixer.loss.table.high.set(filename = '1') \n
		This command defines the conversion loss table to be used for the high (second) range. \n
			:param filename: String containing the path and name of the file, or the serial number of the external mixer whose file is required. The R&S FSW automatically selects the correct cvl file for the current IF. As an alternative, you can also select a user-defined conversion loss table (.acl file) .
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:MIXer:LOSS:TABLe:HIGH {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: value: str = driver.sense.mixer.loss.table.high.get() \n
		This command defines the conversion loss table to be used for the high (second) range. \n
			:return: filename: String containing the path and name of the file, or the serial number of the external mixer whose file is required. The R&S FSW automatically selects the correct cvl file for the current IF. As an alternative, you can also select a user-defined conversion loss table (.acl file) ."""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:TABLe:HIGH?')
		return trim_str_response(response)
