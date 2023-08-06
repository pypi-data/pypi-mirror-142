from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:DATE \n
		Snippet: value: str = driver.applications.k60Transient.system.communicate.rdevice.oscilloscope.alignment.date.get() \n
		Returns the date of alignment of the 'IF OUT 2 GHz/ IF OUT 5 GHz' to the oscilloscope for the optional 2 GHz/ 5 GHz
		bandwidth extension (R&S FSW-B2000/B5000) . For details see 'Alignment'. \n
			:return: date: Returns the date of alignment."""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:DATE?')
		return trim_str_response(response)
