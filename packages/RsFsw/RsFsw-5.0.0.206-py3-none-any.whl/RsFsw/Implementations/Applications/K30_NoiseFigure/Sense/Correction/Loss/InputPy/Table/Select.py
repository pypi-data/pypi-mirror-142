from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, table_name: str) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:TABLe:SELect \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.table.select.set(table_name = '1') \n
		This command selects an input loss table. \n
			:param table_name: String containing the table name.
		"""
		param = Conversions.value_to_quoted_str(table_name)
		self._core.io.write(f'SENSe:CORRection:LOSS:INPut:TABLe:SELect {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:TABLe:SELect \n
		Snippet: value: str = driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.table.select.get() \n
		This command selects an input loss table. \n
			:return: table_name: String containing the table name."""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:INPut:TABLe:SELect?')
		return trim_str_response(response)
