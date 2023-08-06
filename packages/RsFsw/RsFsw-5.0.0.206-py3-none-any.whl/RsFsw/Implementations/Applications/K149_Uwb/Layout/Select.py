from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, selected_layout: int) -> None:
		"""SCPI: LAYout:SELect \n
		Snippet: driver.applications.k149Uwb.layout.select.set(selected_layout = 1) \n
		Sets and queries the window layout. The layout number increases with a new release of the R&S FSW-K149 application, if a
		new default layout is defined. This ensures backwards compatibility for scripts that were created using a different
		layout in a previous version of the application. \n
			:param selected_layout: No help available
		"""
		param = Conversions.decimal_value_to_str(selected_layout)
		self._core.io.write_with_opc(f'LAYout:SELect {param}')

	def get(self) -> int:
		"""SCPI: LAYout:SELect \n
		Snippet: value: int = driver.applications.k149Uwb.layout.select.get() \n
		Sets and queries the window layout. The layout number increases with a new release of the R&S FSW-K149 application, if a
		new default layout is defined. This ensures backwards compatibility for scripts that were created using a different
		layout in a previous version of the application. \n
			:return: selected_layout: No help available"""
		response = self._core.io.query_str_with_opc(f'LAYout:SELect?')
		return Conversions.str_to_int(response)
