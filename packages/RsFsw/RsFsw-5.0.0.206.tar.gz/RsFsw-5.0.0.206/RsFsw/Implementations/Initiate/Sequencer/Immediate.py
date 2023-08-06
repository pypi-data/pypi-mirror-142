from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self) -> None:
		"""SCPI: INITiate:SEQuencer:IMMediate \n
		Snippet: driver.initiate.sequencer.immediate.set() \n
		This command starts a new sequence of measurements by the Sequencer. Its effect is similar to the method RsFsw.
		Applications.K10x_Lte.Initiate.Immediate.set command used for a single measurement. Before this command can be executed,
		the Sequencer must be activated (see method RsFsw.System.Sequencer.set) . \n
		"""
		self._core.io.write(f'INITiate:SEQuencer:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:SEQuencer:IMMediate \n
		Snippet: driver.initiate.sequencer.immediate.set_with_opc() \n
		This command starts a new sequence of measurements by the Sequencer. Its effect is similar to the method RsFsw.
		Applications.K10x_Lte.Initiate.Immediate.set command used for a single measurement. Before this command can be executed,
		the Sequencer must be activated (see method RsFsw.System.Sequencer.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:SEQuencer:IMMediate', opc_timeout_ms)
