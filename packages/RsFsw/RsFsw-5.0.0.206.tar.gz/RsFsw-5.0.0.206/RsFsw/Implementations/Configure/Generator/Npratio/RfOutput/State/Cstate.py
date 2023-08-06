from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstate:
	"""Cstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cstate", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.ControlState:
		"""SCPI: CONFigure:GENerator:NPRatio:RFOutput:STATe:CSTate \n
		Snippet: value: enums.ControlState = driver.configure.generator.npratio.rfOutput.state.cstate.get() \n
		Queries the state of the generator RF output. \n
			:return: control_state: OFF | SUCCessful | ERRor OFF Signal generator control off SUCCessful Setting successfully applied on the signal generator ERRor Control error, for example because a specified value cannot be applied on the signal generator"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:RFOutput:STATe:CSTate?')
		return Conversions.str_to_scalar_enum(response, enums.ControlState)
