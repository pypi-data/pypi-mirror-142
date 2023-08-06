from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vfirmware:
	"""Vfirmware commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vfirmware", core, parent)

	def set(self, valid_device: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:VFIRmware \n
		Snippet: driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.vfirmware.set(valid_device = False) \n
		Queries whether the firmware on the connected oscilloscope is supported by the 2 GHz / 5 GHz bandwidth extension
		(B2000/B5000) option. For details see 'Alignment'. \n
			:param valid_device: No help available
		"""
		param = Conversions.bool_to_str(valid_device)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:VFIRmware {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:VFIRmware \n
		Snippet: value: bool = driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.vfirmware.get() \n
		Queries whether the firmware on the connected oscilloscope is supported by the 2 GHz / 5 GHz bandwidth extension
		(B2000/B5000) option. For details see 'Alignment'. \n
			:return: valid_device: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:VFIRmware?')
		return Conversions.str_to_bool(response)
