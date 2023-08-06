from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Roscillator:
	"""Roscillator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roscillator", core, parent)

	def set(self, reference_type: enums.SourceInt) -> None:
		"""SCPI: CONFigure:GENerator:EXTernal:ROSCillator \n
		Snippet: driver.configure.generator.external.roscillator.set(reference_type = enums.SourceInt.EXTernal) \n
		Selects the source of the generator reference frequency. \n
			:param reference_type: EXTernal | INTernal EXTernal An external reference is provided via the EXT connectors on the generator, for example by the R&S FSW. INTernal The internal reference is that of the signal generator itself.
		"""
		param = Conversions.enum_scalar_to_str(reference_type, enums.SourceInt)
		self._core.io.write(f'CONFigure:GENerator:EXTernal:ROSCillator {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceInt:
		"""SCPI: CONFigure:GENerator:EXTernal:ROSCillator \n
		Snippet: value: enums.SourceInt = driver.configure.generator.external.roscillator.get() \n
		Selects the source of the generator reference frequency. \n
			:return: reference_type: EXTernal | INTernal EXTernal An external reference is provided via the EXT connectors on the generator, for example by the R&S FSW. INTernal The internal reference is that of the signal generator itself."""
		response = self._core.io.query_str(f'CONFigure:GENerator:EXTernal:ROSCillator?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)
