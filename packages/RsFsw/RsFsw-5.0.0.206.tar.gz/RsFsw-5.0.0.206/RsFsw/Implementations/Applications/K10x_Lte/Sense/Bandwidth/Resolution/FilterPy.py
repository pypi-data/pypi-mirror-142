from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:FILTer \n
		Snippet: driver.applications.k10Xlte.sense.bandwidth.resolution.filterPy.set(bandwidth = 1.0) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:BWIDth:RESolution:FILTer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:FILTer \n
		Snippet: value: float = driver.applications.k10Xlte.sense.bandwidth.resolution.filterPy.get() \n
		No command help available \n
			:return: bandwidth: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:FILTer?')
		return Conversions.str_to_float(response)
