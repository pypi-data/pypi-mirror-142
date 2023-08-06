from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ratio:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, ratio: float) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:RATio \n
		Snippet: driver.applications.k10Xlte.sense.bandwidth.resolution.ratio.set(ratio = 1.0) \n
		No command help available \n
			:param ratio: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SENSe:BWIDth:RESolution:RATio {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:RATio \n
		Snippet: value: float = driver.applications.k10Xlte.sense.bandwidth.resolution.ratio.get() \n
		No command help available \n
			:return: ratio: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:RATio?')
		return Conversions.str_to_float(response)
