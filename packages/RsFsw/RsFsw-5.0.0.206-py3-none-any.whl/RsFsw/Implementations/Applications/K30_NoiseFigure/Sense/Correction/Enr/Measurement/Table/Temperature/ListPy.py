from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe:TEMPerature:LIST \n
		Snippet: value: str = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.temperature.listPy.get() \n
		This command queries all temperature tables available in the application. \n
			:return: tables: list String containing the names of the tables as a comma separated list."""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:MEASurement:TABLe:TEMPerature:LIST?')
		return trim_str_response(response)
