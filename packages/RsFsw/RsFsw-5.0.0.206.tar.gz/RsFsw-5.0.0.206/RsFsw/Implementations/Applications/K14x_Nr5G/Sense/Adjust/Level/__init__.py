from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.level.set() \n
		This command adjusts the level settings, including attenuator and preamplifier, to achieve the best dynamic range.
		Compared to [SENSe:]ADJust:EVM, which achieves the best amplitude settings to optimize the EVM, you can use this command
		for a quick determination of preliminary amplitude settings. \n
		"""
		self._core.io.write(f'SENSe:ADJust:LEVel')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.level.set_with_opc() \n
		This command adjusts the level settings, including attenuator and preamplifier, to achieve the best dynamic range.
		Compared to [SENSe:]ADJust:EVM, which achieves the best amplitude settings to optimize the EVM, you can use this command
		for a quick determination of preliminary amplitude settings. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:LEVel', opc_timeout_ms)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
