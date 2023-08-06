from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstate:
	"""Cstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cstate", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.ControlState:
		"""SCPI: CONFigure:GENerator:MCGD:CONNection:CSTate \n
		Snippet: value: enums.ControlState = driver.applications.k17Mcgd.configure.generator.mcgd.connection.cstate.get() \n
		Queries the state of the connected signal generator and its availability for the R&S FSW MCGD application. \n
			:return: state: OFF | SUCCessful | ERRor OFF No signal generator defined SUCCessful Connection established to compatible generator ERRor Connection error, for example due to an incompatible generator"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:CONNection:CSTate?')
		return Conversions.str_to_scalar_enum(response, enums.ControlState)
