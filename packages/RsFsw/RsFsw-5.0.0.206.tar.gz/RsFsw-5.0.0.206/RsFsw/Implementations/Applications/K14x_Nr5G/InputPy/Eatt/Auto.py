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
		Snippet: driver.applications.k14Xnr5G.inputPy.eatt.auto.set(state = False) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command is available with the optional Electronic Attenuator, but not
		if you are using the optional Digital Baseband Input. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:EATT:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EATT:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.inputPy.eatt.auto.get() \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command is available with the optional Electronic Attenuator, but not
		if you are using the optional Digital Baseband Input. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'INPut:EATT:AUTO?')
		return Conversions.str_to_bool(response)
