from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, sub_span_frequency: float) -> None:
		"""SCPI: [SENSe]:SUBSpan[:BANDwidth] \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.bandwidth.set(sub_span_frequency = 1.0) \n
		Defines the bandwidth of the subspans for active frequency subspan measurements. \n
			:param sub_span_frequency: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(sub_span_frequency)
		self._core.io.write(f'SENSe:SUBSpan:BANDwidth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan[:BANDwidth] \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.bandwidth.get() \n
		Defines the bandwidth of the subspans for active frequency subspan measurements. \n
			:return: sub_span_frequency: Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:BANDwidth?')
		return Conversions.str_to_float(response)
