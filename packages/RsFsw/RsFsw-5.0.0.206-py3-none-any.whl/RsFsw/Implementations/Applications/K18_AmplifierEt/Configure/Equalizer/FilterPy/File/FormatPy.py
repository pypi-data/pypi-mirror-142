from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, source: enums.FileFormatSource) -> None:
		"""SCPI: CONFigure:EQUalizer:FILTer:FILE:FORMat \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.filterPy.file.formatPy.set(source = enums.FileFormatSource.CSV) \n
		This command selects the file format to which the equalizer filter is exported. \n
			:param source: CSV Filter is written to a csv file. FRES Filter is written to a fres file.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.FileFormatSource)
		self._core.io.write(f'CONFigure:EQUalizer:FILTer:FILE:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FileFormatSource:
		"""SCPI: CONFigure:EQUalizer:FILTer:FILE:FORMat \n
		Snippet: value: enums.FileFormatSource = driver.applications.k18AmplifierEt.configure.equalizer.filterPy.file.formatPy.get() \n
		This command selects the file format to which the equalizer filter is exported. \n
			:return: source: CSV Filter is written to a csv file. FRES Filter is written to a fres file."""
		response = self._core.io.query_str(f'CONFigure:EQUalizer:FILTer:FILE:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.FileFormatSource)
