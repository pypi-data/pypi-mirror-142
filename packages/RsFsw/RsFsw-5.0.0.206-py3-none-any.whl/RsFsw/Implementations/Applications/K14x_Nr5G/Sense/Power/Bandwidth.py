from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:POWer:BWIDth \n
		Snippet: driver.applications.k14Xnr5G.sense.power.bandwidth.set(bandwidth = 1.0) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:POWer:BWIDth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:BWIDth \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.bandwidth.get() \n
		No command help available \n
			:return: bandwidth: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:BWIDth?')
		return Conversions.str_to_float(response)
