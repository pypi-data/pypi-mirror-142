from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, freq: List[float], level: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: driver.applications.k9X11Ad.sense.correction.cvl.data.set(freq = [1.1, 2.2, 3.3], level = [1.1, 2.2, 3.3]) \n
		This command defines the reference values of the selected conversion loss tables. The values are entered as a set of
		frequency/level pairs. A maximum of 50 frequency/level pairs may be entered. Before this command can be performed, the
		conversion loss table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option
		B21 (External Mixer) installed. \n
			:param freq: The frequencies have to be sent in ascending order. Unit: HZ
			:param level: Unit: DB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('freq', freq, DataType.FloatList, None), ArgSingle.as_open_list('level', level, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:CVL:DATA {param}'.rstrip())

	def get(self, freq: List[float], level: List[float]) -> List[float]:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: value: List[float] = driver.applications.k9X11Ad.sense.correction.cvl.data.get(freq = [1.1, 2.2, 3.3], level = [1.1, 2.2, 3.3]) \n
		This command defines the reference values of the selected conversion loss tables. The values are entered as a set of
		frequency/level pairs. A maximum of 50 frequency/level pairs may be entered. Before this command can be performed, the
		conversion loss table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option
		B21 (External Mixer) installed. \n
			:param freq: The frequencies have to be sent in ascending order. Unit: HZ
			:param level: Unit: DB
			:return: freq: The frequencies have to be sent in ascending order. Unit: HZ"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('freq', freq, DataType.FloatList, None), ArgSingle.as_open_list('level', level, DataType.FloatList, None))
		response = self._core.io.query_bin_or_ascii_float_list(f'SENSe:CORRection:CVL:DATA? {param}'.rstrip())
		return response
