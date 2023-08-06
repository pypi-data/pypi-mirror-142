from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Memory:
	"""Memory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("memory", core, parent)

	def get(self, points_offset: int, points_count: int) -> List[float]:
		"""SCPI: TRACe:IQ:DATA:MEMory \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.trace.iq.data.memory.get(points_offset = 1, points_count = 1) \n
		Tansfers raw I/Q data. \n
			:param points_offset: No help available
			:param points_count: No help available
			:return: iq_data: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('points_offset', points_offset, DataType.Integer), ArgSingle('points_count', points_count, DataType.Integer))
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe:IQ:DATA:MEMory? {param}'.rstrip())
		return response
