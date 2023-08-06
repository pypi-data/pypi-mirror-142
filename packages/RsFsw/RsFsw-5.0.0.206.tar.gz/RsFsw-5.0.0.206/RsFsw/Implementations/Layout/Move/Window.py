from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, source_window: str, target_window: str, direction: enums.WindowDirReplace) -> None:
		"""SCPI: LAYout:MOVE[:WINDow] \n
		Snippet: driver.layout.move.window.set(source_window = '1', target_window = '1', direction = enums.WindowDirReplace.ABOVe) \n
		No command help available \n
			:param source_window: String containing the name of an existing window that is to be moved. By default, the name of a window is the same as its index. To determine the name and index of all active windows in the active channel, use the method RsFsw.Layout.Catalog.Window.get_ query.
			:param target_window: String containing the name of an existing window that is to be moved. By default, the name of a window is the same as its index. To determine the name and index of all active windows in the active channel, use the method RsFsw.Layout.Catalog.Window.get_ query.
			:param direction: LEFT | RIGHt | ABOVe | BELow | REPLace Destination the selected window is moved to, relative to the reference window.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_window', source_window, DataType.String), ArgSingle('target_window', target_window, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.WindowDirReplace))
		self._core.io.write_with_opc(f'LAYout:MOVE:WINDow {param}'.rstrip())
