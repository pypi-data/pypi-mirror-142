from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:ATTenuation:AUTO \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.attenuation.auto.set(state = False) \n
		This command couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the
		R&S FSW determines the signal level for optimal internal data processing and sets the required attenuation accordingly. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:ATTenuation:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:ATTenuation:AUTO \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.inputPy.attenuation.auto.get() \n
		This command couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the
		R&S FSW determines the signal level for optimal internal data processing and sets the required attenuation accordingly. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'INPut:ATTenuation:AUTO?')
		return Conversions.str_to_bool(response)
