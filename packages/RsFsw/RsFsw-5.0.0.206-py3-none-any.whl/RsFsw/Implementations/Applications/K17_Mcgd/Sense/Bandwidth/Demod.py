from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:BWIDth:DEMod \n
		Snippet: driver.applications.k17Mcgd.sense.bandwidth.demod.set(bandwidth = 1.0) \n
		No command help available \n
			:param bandwidth: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:BWIDth:DEMod {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth:DEMod \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.bandwidth.demod.get() \n
		No command help available \n
			:return: bandwidth: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:BWIDth:DEMod?')
		return Conversions.str_to_float(response)
