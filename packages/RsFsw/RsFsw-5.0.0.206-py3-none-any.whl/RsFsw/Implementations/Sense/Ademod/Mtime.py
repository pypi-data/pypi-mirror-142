from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtime:
	"""Mtime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtime", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:ADEMod:MTIMe \n
		Snippet: driver.sense.ademod.mtime.set(time = 1.0) \n
		This command defines the measurement time for Analog Modulation Analysis. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:ADEMod:MTIMe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:MTIMe \n
		Snippet: value: float = driver.sense.ademod.mtime.get() \n
		This command defines the measurement time for Analog Modulation Analysis. \n
			:return: time: Unit: S"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MTIMe?')
		return Conversions.str_to_float(response)
