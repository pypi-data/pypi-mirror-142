from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcgd:
	"""Mcgd commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcgd", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self) -> None:
		"""SCPI: CALibration:MCGD \n
		Snippet: driver.applications.k17Mcgd.calibration.mcgd.set() \n
		This command initiates a new calibration. You can synchronize to the end of the measurement as usual with *OPC, *OPC? or
		*WAI. You can execute this command in two different modes: synchronous and asynchronous. In asynchronous mode, the
		command starts a new calibration and immediately continues processing subsequent commands while calibration is performed
		in the background. In synchronous mode, further processing only continues when the calibration is finished.
		For synchronous mode, add ;*WAI to the end of the method RsFsw.Applications.K17_Mcgd.Calibration.Mcgd.set command. This
		is useful, for example, if you want to run a script file which does not know when the calibration finishes. \n
		"""
		self._core.io.write(f'CALibration:MCGD')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:MCGD \n
		Snippet: driver.applications.k17Mcgd.calibration.mcgd.set_with_opc() \n
		This command initiates a new calibration. You can synchronize to the end of the measurement as usual with *OPC, *OPC? or
		*WAI. You can execute this command in two different modes: synchronous and asynchronous. In asynchronous mode, the
		command starts a new calibration and immediately continues processing subsequent commands while calibration is performed
		in the background. In synchronous mode, further processing only continues when the calibration is finished.
		For synchronous mode, add ;*WAI to the end of the method RsFsw.Applications.K17_Mcgd.Calibration.Mcgd.set command. This
		is useful, for example, if you want to run a script file which does not know when the calibration finishes. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:MCGD', opc_timeout_ms)

	def clone(self) -> 'Mcgd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcgd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
