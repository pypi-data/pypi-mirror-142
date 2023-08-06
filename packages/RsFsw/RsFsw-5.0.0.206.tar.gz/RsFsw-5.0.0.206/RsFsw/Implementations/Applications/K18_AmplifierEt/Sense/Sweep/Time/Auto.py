from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:TIME:AUTO \n
		Snippet: driver.applications.k18AmplifierEt.sense.sweep.time.auto.set(state = False) \n
		This command turns automatic selection of an appropriate capture time on and off. When you turn on this feature, the
		application calculates an appropriate capture time based on the reference signal and adjusts the other acquisition
		settings accordingly. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:TIME:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:TIME:AUTO \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.sweep.time.auto.get() \n
		This command turns automatic selection of an appropriate capture time on and off. When you turn on this feature, the
		application calculates an appropriate capture time based on the reference signal and adjusts the other acquisition
		settings accordingly. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:SWEep:TIME:AUTO?')
		return Conversions.str_to_bool(response)
