from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:DIQ:RANGe[:UPPer]:AUTO \n
		Snippet: driver.applications.k14Xnr5G.inputPy.diq.range.upper.auto.set(state = False) \n
		If enabled, the digital input full scale level is automatically set to the value provided by the connected device (if
		available) . This command is only available if the optional Digital Baseband interface is installed. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:DIQ:RANGe:UPPer:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:DIQ:RANGe[:UPPer]:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.inputPy.diq.range.upper.auto.get() \n
		If enabled, the digital input full scale level is automatically set to the value provided by the connected device (if
		available) . This command is only available if the optional Digital Baseband interface is installed. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'INPut:DIQ:RANGe:UPPer:AUTO?')
		return Conversions.str_to_bool(response)
