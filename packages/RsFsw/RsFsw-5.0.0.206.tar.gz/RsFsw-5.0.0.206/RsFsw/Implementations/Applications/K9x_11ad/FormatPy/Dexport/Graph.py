from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Graph:
	"""Graph commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("graph", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: FORMat:DEXPort:GRAPh \n
		Snippet: driver.applications.k9X11Ad.formatPy.dexport.graph.set(state = False) \n
		If enabled, all traces for the currently selected graphical result display are included in the export file. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'FORMat:DEXPort:GRAPh {param}')

	def get(self) -> bool:
		"""SCPI: FORMat:DEXPort:GRAPh \n
		Snippet: value: bool = driver.applications.k9X11Ad.formatPy.dexport.graph.get() \n
		If enabled, all traces for the currently selected graphical result display are included in the export file. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'FORMat:DEXPort:GRAPh?')
		return Conversions.str_to_bool(response)
