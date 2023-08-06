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
		"""SCPI: MMEMory:STORe:IQ:STATe \n
		Snippet: driver.massMemory.store.iq.state.set(filename = '1') \n
		This command writes the captured I/Q data to a file. The file extension is *.iq.tar. By default, the contents of the file
		are in 32-bit floating point format. \n
			:param filename: String containing the path and name of the target file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:STORe:IQ:STATe 1, {param}')
