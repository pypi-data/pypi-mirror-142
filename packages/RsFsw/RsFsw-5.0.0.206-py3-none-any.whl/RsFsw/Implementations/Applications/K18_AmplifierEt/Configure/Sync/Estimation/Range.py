from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, start: float, stop: float) -> None:
		"""SCPI: CONFigure:SYNC:ESTimation:RANGe \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.estimation.range.set(start = 1.0, stop = 1.0) \n
		No command help available \n
			:param start: No help available
			:param stop: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Float), ArgSingle('stop', stop, DataType.Float))
		self._core.io.write(f'CONFigure:SYNC:ESTimation:RANGe {param}'.rstrip())
