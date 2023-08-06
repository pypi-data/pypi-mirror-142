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
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.time.auto.set(state = False) \n
		If enabled, the sweep time is automatically selected, depending on the current frequency of the sweep point, as defined
		in the frequency table (see 'Using a frequency table') . If disabled, the value defined by [SENSe:]SWEep:TIME is used. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:TIME:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:TIME:AUTO \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.sweep.time.auto.get() \n
		If enabled, the sweep time is automatically selected, depending on the current frequency of the sweep point, as defined
		in the frequency table (see 'Using a frequency table') . If disabled, the value defined by [SENSe:]SWEep:TIME is used. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:SWEep:TIME:AUTO?')
		return Conversions.str_to_bool(response)
