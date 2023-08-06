from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency: List[float]) -> None:
		"""SCPI: [SENSe]:FREQuency:TABLe:DATA \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.table.data.set(frequency = [1.1, 2.2, 3.3]) \n
		This command defines the contents of the frequency table. The command overwrites the current contents of the frequency
		table. \n
			:param frequency: Defines a frequency for each entry in the frequency table. A frequency table can contain up to 10001 entries. Range: 0 Hz to fmax, Unit: HZ
		"""
		param = Conversions.list_to_csv_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:TABLe:DATA {param}')

	def get(self) -> List[float]:
		"""SCPI: [SENSe]:FREQuency:TABLe:DATA \n
		Snippet: value: List[float] = driver.applications.k30NoiseFigure.sense.frequency.table.data.get() \n
		This command defines the contents of the frequency table. The command overwrites the current contents of the frequency
		table. \n
			:return: frequency: Defines a frequency for each entry in the frequency table. A frequency table can contain up to 10001 entries. Range: 0 Hz to fmax, Unit: HZ"""
		response = self._core.io.query_bin_or_ascii_float_list(f'SENSe:FREQuency:TABLe:DATA?')
		return response
