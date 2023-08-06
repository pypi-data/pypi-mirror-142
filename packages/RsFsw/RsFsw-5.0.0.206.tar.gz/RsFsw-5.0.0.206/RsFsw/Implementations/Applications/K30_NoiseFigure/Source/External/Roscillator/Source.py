from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.SourceInt) -> None:
		"""SCPI: SOURce:EXTernal:ROSCillator[:SOURce] \n
		Snippet: driver.applications.k30NoiseFigure.source.external.roscillator.source.set(source = enums.SourceInt.EXTernal) \n
		This command controls selection of the reference oscillator for the external generator. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. If the external reference oscillator is selected, the reference
		signal must be connected to the rear panel of the instrument. \n
			:param source: INTernal Uses the internal reference. EXTernal Uses the external reference; if none is available, an error flag is displayed in the status bar.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce:EXTernal:ROSCillator:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceInt:
		"""SCPI: SOURce:EXTernal:ROSCillator[:SOURce] \n
		Snippet: value: enums.SourceInt = driver.applications.k30NoiseFigure.source.external.roscillator.source.get() \n
		This command controls selection of the reference oscillator for the external generator. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. If the external reference oscillator is selected, the reference
		signal must be connected to the rear panel of the instrument. \n
			:return: source: INTernal Uses the internal reference. EXTernal Uses the external reference; if none is available, an error flag is displayed in the status bar."""
		response = self._core.io.query_str(f'SOURce:EXTernal:ROSCillator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)
