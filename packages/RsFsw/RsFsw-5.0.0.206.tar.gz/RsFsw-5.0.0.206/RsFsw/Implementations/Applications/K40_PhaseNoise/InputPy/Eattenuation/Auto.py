from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: INPut:EATTenuation:AUTO \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.eattenuation.auto.set(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'INPut:EATTenuation:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EATTenuation:AUTO \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.inputPy.eattenuation.auto.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INPut:EATTenuation:AUTO?')
		return Conversions.str_to_bool(response)
