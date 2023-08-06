from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Falignment:
	"""Falignment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("falignment", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:FALignment \n
		Snippet: driver.system.communicate.rdevice.oscilloscope.alignment.falignment.set(state = False) \n
		Performs a self-alignment on the oscilloscope before the B2000/B5000 alignment on the R&S FSW. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:FALignment {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:FALignment \n
		Snippet: value: bool = driver.system.communicate.rdevice.oscilloscope.alignment.falignment.get() \n
		Performs a self-alignment on the oscilloscope before the B2000/B5000 alignment on the R&S FSW. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:FALignment?')
		return Conversions.str_to_bool(response)
