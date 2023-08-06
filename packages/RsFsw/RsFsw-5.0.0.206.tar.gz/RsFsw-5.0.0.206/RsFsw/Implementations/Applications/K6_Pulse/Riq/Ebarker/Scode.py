from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scode:
	"""Scode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scode", core, parent)

	def set(self, length: int) -> None:
		"""SCPI: RIQ:EBARker:SCODe \n
		Snippet: driver.applications.k6Pulse.riq.ebarker.scode.set(length = 1) \n
		This command selects the reference IQ embedded barker secondary code length for time sidelobe measurements. \n
			:param length: No help available
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'RIQ:EBARker:SCODe {param}')

	def get(self) -> int:
		"""SCPI: RIQ:EBARker:SCODe \n
		Snippet: value: int = driver.applications.k6Pulse.riq.ebarker.scode.get() \n
		This command selects the reference IQ embedded barker secondary code length for time sidelobe measurements. \n
			:return: length: No help available"""
		response = self._core.io.query_str(f'RIQ:EBARker:SCODe?')
		return Conversions.str_to_int(response)
