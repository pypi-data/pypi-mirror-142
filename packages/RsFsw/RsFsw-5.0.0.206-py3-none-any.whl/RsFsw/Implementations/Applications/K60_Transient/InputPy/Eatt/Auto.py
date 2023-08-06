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
		"""SCPI: INPut:EATT:AUTO \n
		Snippet: driver.applications.k60Transient.inputPy.eatt.auto.set(state = False) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:EATT:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EATT:AUTO \n
		Snippet: value: bool = driver.applications.k60Transient.inputPy.eatt.auto.get() \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'INPut:EATT:AUTO?')
		return Conversions.str_to_bool(response)
