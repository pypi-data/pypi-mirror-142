from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def slots(self):
		"""slots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slots'):
			from .Slots import Slots
			self._slots = Slots(self._core, self._cmd_group)
		return self._slots

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:EVM \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.evm.set() \n
		This command adjusts the amplitude settings, including attenuator and preamplifier, to achieve the optimal EVM using the
		maximum dynamic range. Note that this process can up to several minutes, depending on the number of component carriers
		you are measuring. For the auto EVM routine, it is sufficient to send this command. It is not necessary to send method
		RsFsw.Applications.K10x_Lte.Initiate.Immediate.set. \n
		"""
		self._core.io.write(f'SENSe:ADJust:EVM')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:EVM \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.evm.set_with_opc() \n
		This command adjusts the amplitude settings, including attenuator and preamplifier, to achieve the optimal EVM using the
		maximum dynamic range. Note that this process can up to several minutes, depending on the number of component carriers
		you are measuring. For the auto EVM routine, it is sufficient to send this command. It is not necessary to send method
		RsFsw.Applications.K10x_Lte.Initiate.Immediate.set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:EVM', opc_timeout_ms)

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
