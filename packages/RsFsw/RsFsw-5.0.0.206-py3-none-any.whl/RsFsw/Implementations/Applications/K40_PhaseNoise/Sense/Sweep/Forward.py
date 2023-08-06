from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Forward:
	"""Forward commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("forward", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:FORWard \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.forward.set(state = False) \n
		This command selects the measurement direction. Specifies the sweep direction. When switched on the sweep direction is
		from the start frequency to the stop frequency. When switched off the sweep direction is reversed \n
			:param state: ON | 1 Measurements in forward direction. The measurements starts at the smallest offset frequency. OFF | 0 Measurement in reverse direction. The measurement starts at the highest offset frequency.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:FORWard {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:FORWard \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.sweep.forward.get() \n
		This command selects the measurement direction. Specifies the sweep direction. When switched on the sweep direction is
		from the start frequency to the stop frequency. When switched off the sweep direction is reversed \n
			:return: state: ON | 1 Measurements in forward direction. The measurements starts at the smallest offset frequency. OFF | 0 Measurement in reverse direction. The measurement starts at the highest offset frequency."""
		response = self._core.io.query_str(f'SENSe:SWEep:FORWard?')
		return Conversions.str_to_bool(response)
