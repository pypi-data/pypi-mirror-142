from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.massMemory.load.iq.state.set(filename = '1') \n
		This command restores I/Q data from a file. The file extension is *.iq.tar. \n
			:param filename: string String containing the path and name of the source file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:LOAD:IQ:STATe 1, {param}')
