from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, source_window: str, target_window: str, arg_2: enums.WindowDirReplace) -> None:
		"""SCPI: LAYout:MOVE[:WINDow] \n
		Snippet: driver.applications.k40PhaseNoise.layout.move.window.set(source_window = '1', target_window = '1', arg_2 = enums.WindowDirReplace.ABOVe) \n
		No command help available \n
			:param source_window: No help available
			:param target_window: No help available
			:param arg_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_window', source_window, DataType.String), ArgSingle('target_window', target_window, DataType.String), ArgSingle('arg_2', arg_2, DataType.Enum, enums.WindowDirReplace))
		self._core.io.write_with_opc(f'LAYout:MOVE:WINDow {param}'.rstrip())
