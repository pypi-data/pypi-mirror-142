from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcpip:
	"""Tcpip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcpip", core, parent)

	def set(self, tcpip: str) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip \n
		Snippet: driver.applications.k18AmplifierEt.system.communicate.rdevice.oscilloscope.tcpip.set(tcpip = '1') \n
		No command help available \n
			:param tcpip: No help available
		"""
		param = Conversions.value_to_quoted_str(tcpip)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip \n
		Snippet: value: str = driver.applications.k18AmplifierEt.system.communicate.rdevice.oscilloscope.tcpip.get() \n
		No command help available \n
			:return: tcpip: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip?')
		return trim_str_response(response)
