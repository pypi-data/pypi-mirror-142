from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duplicate:
	"""Duplicate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duplicate", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INSTrument:CREate:DUPLicate \n
		Snippet: driver.instrument.create.duplicate.set() \n
		This command duplicates the currently selected channel, i.e creates a new channel of the same type and with the identical
		measurement settings. The name of the new channel is the same as the copied channel, extended by a consecutive number (e.
		g. 'IQAnalyzer' -> 'IQAnalyzer 2') . The channel to be duplicated must be selected first using the INST:SEL command. (See
		method RsFsw.Instrument.Select.set) . This command is not available if the MSRA / MSRT primary channel is selected. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INSTrument:CREate:DUPLicate', opc_timeout_ms)
