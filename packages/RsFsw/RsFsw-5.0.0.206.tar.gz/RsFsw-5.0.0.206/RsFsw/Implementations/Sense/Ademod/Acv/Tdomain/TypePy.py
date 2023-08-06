from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, trace_mode: List[enums.TraceModeA]) -> None:
		"""SCPI: [SENSe]:ADEMod:ACV[:TDOMain][:TYPE] \n
		Snippet: driver.sense.ademod.acv.tdomain.typePy.set(trace_mode = [TraceModeA.AVERage, TraceModeA.WRITe]) \n
		No command help available \n
			:param trace_mode: No help available
		"""
		param = Conversions.enum_list_to_str(trace_mode, enums.TraceModeA)
		self._core.io.write(f'SENSe:ADEMod:ACV:TDOMain:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> List[enums.TraceModeA]:
		"""SCPI: [SENSe]:ADEMod:ACV[:TDOMain][:TYPE] \n
		Snippet: value: List[enums.TraceModeA] = driver.sense.ademod.acv.tdomain.typePy.get() \n
		No command help available \n
			:return: trace_mode: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:ACV:TDOMain:TYPE?')
		return Conversions.str_to_list_enum(response, enums.TraceModeA)
