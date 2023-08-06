from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdevice:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	def get(self) -> str:
		"""SCPI: OUTPut:IQHS:CDEVice \n
		Snippet: value: str = driver.applications.k60Transient.output.iqhs.cdevice.get() \n
		Returns a comma-separated list of information on the instrument connected to the QSFP+ connector, if available.
		For details on Digital I/Q 40G Streaming Output (R&S FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:return: device: No help available"""
		response = self._core.io.query_str(f'OUTPut:IQHS:CDEVice?')
		return trim_str_response(response)
