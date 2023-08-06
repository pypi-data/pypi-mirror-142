from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ostate:
	"""Ostate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ostate", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.ControlState:
		"""SCPI: CONFigure:GENerator:MCGD:OSTate \n
		Snippet: value: enums.ControlState = driver.applications.k17Mcgd.configure.generator.mcgd.ostate.get() \n
		Queries the overall status of the generator control settings. \n
			:return: state: OFF | SUCCessful | ERRor OFF Signal generator control off SUCCessful Connection established and all settings valid ERRor Control error, for example because a specified value cannot be applied on the signal generator"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:OSTate?')
		return Conversions.str_to_scalar_enum(response, enums.ControlState)
