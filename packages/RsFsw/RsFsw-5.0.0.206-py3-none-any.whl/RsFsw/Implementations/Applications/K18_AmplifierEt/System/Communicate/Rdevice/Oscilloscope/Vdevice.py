from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vdevice:
	"""Vdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vdevice", core, parent)

	def set(self, valid_device: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:VDEVice \n
		Snippet: driver.applications.k18AmplifierEt.system.communicate.rdevice.oscilloscope.vdevice.set(valid_device = False) \n
		No command help available \n
			:param valid_device: No help available
		"""
		param = Conversions.bool_to_str(valid_device)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:VDEVice {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:VDEVice \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.system.communicate.rdevice.oscilloscope.vdevice.get() \n
		No command help available \n
			:return: valid_device: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:VDEVice?')
		return Conversions.str_to_bool(response)
