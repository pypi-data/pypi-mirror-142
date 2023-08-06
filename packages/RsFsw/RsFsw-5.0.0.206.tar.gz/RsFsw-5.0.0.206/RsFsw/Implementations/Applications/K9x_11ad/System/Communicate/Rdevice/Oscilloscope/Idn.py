from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Idn:
	"""Idn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("idn", core, parent)

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:IDN \n
		Snippet: value: str = driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.idn.get() \n
		Returns the identification string of the oscilloscope connected to the R&S FSW. \n
			:return: idn: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:IDN?')
		return trim_str_response(response)
