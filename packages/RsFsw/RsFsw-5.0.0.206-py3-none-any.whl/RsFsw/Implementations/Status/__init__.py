from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 112 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	@property
	def operation(self):
		"""operation commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_operation'):
			from .Operation import Operation
			self._operation = Operation(self._core, self._cmd_group)
		return self._operation

	@property
	def questionable(self):
		"""questionable commands group. 20 Sub-classes, 0 commands."""
		if not hasattr(self, '_questionable'):
			from .Questionable import Questionable
			self._questionable = Questionable(self._core, self._cmd_group)
		return self._questionable

	@property
	def queue(self):
		"""queue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_queue'):
			from .Queue import Queue
			self._queue = Queue(self._core, self._cmd_group)
		return self._queue

	def preset(self) -> None:
		"""SCPI: STATus:PRESet \n
		Snippet: driver.status.preset() \n
		This command resets the edge detectors and ENABle parts of all registers to a defined value. All PTRansition parts are
		set to FFFFh, i.e. all transitions from 0 to 1 are detected. All NTRansition parts are set to 0, i.e. a transition from 1
		to 0 in a CONDition bit is not detected. The ENABle part of the method RsFsw.Status.Operation.Event.get_ and method RsFsw.
		Status.Questionable.Event.get_ registers are set to 0, i.e. all events in these registers are not passed on. \n
		"""
		self._core.io.write(f'STATus:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STATus:PRESet \n
		Snippet: driver.status.preset_with_opc() \n
		This command resets the edge detectors and ENABle parts of all registers to a defined value. All PTRansition parts are
		set to FFFFh, i.e. all transitions from 0 to 1 are detected. All NTRansition parts are set to 0, i.e. a transition from 1
		to 0 in a CONDition bit is not detected. The ENABle part of the method RsFsw.Status.Operation.Event.get_ and method RsFsw.
		Status.Questionable.Event.get_ registers are set to 0, i.e. all events in these registers are not passed on. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STATus:PRESet', opc_timeout_ms)

	def clone(self) -> 'Status':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Status(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
