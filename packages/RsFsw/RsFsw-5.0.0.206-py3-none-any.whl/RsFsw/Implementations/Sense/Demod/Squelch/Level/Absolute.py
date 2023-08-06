from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel:ABSolute \n
		Snippet: driver.sense.demod.squelch.level.absolute.set(threshold = 1.0) \n
		No command help available \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:DEMod:SQUelch:LEVel:ABSolute {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel:ABSolute \n
		Snippet: value: float = driver.sense.demod.squelch.level.absolute.get() \n
		No command help available \n
			:return: threshold: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:SQUelch:LEVel:ABSolute?')
		return Conversions.str_to_float(response)
