from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mhelper:
	"""Mhelper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mhelper", core, parent)

	def set(self, format_py: enums.FormatMHelper) -> None:
		"""SCPI: CONFigure[:NR5G]:MSHelper:MHELper \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.msHelper.mhelper.set(format_py = enums.FormatMHelper.MANual) \n
		No command help available \n
			:param format_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.FormatMHelper)
		self._core.io.write(f'CONFigure:NR5G:MSHelper:MHELper {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FormatMHelper:
		"""SCPI: CONFigure[:NR5G]:MSHelper:MHELper \n
		Snippet: value: enums.FormatMHelper = driver.applications.k14Xnr5G.configure.nr5G.msHelper.mhelper.get() \n
		No command help available \n
			:return: format_py: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:MSHelper:MHELper?')
		return Conversions.str_to_scalar_enum(response, enums.FormatMHelper)
