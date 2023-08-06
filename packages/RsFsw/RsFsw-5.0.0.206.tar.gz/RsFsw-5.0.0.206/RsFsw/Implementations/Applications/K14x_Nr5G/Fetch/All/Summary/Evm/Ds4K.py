from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ds4K:
	"""Ds4K commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ds4K", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:ALL:SUMMary:EVM:DS4K \n
		Snippet: value: float = driver.applications.k14Xnr5G.fetch.all.summary.evm.ds4K.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:ALL:SUMMary:EVM:DS4K?')
		return Conversions.str_to_float(response)
