from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:TYPE \n
		Snippet: driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.typePy.set(name = '1') \n
		This command selects the type of external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:param name: Generator name as string value
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:GENerator:TYPE {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:TYPE \n
		Snippet: value: str = driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.typePy.get() \n
		This command selects the type of external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:return: name: Generator name as string value"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:GENerator:TYPE?')
		return trim_str_response(response)
