from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.DisplayFormat) -> None:
		"""SCPI: DISPlay:FORMat \n
		Snippet: driver.display.formatPy.set(format_py = enums.DisplayFormat.SINGle) \n
		This command determines which tab is displayed. \n
			:param format_py: SPLit Displays the MultiView tab with an overview of all active channels (See 'R&S MultiView') . SINGle Displays the measurement channel that was previously focused.
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.DisplayFormat)
		self._core.io.write(f'DISPlay:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DisplayFormat:
		"""SCPI: DISPlay:FORMat \n
		Snippet: value: enums.DisplayFormat = driver.display.formatPy.get() \n
		This command determines which tab is displayed. \n
			:return: format_py: SPLit Displays the MultiView tab with an overview of all active channels (See 'R&S MultiView') . SINGle Displays the measurement channel that was previously focused."""
		response = self._core.io.query_str(f'DISPlay:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayFormat)
