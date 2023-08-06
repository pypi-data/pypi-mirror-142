from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Efilter:
	"""Efilter commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("efilter", core, parent)

	@property
	def fparameters(self):
		"""fparameters commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fparameters'):
			from .Fparameters import Fparameters
			self._fparameters = Fparameters(self._core, self._cmd_group)
		return self._fparameters

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def preset(self) -> None:
		"""SCPI: [SENSe]:NR5G:EFILter:PRESet \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.efilter.preset() \n
		This command removes all event filters. \n
		"""
		self._core.io.write(f'SENSe:NR5G:EFILter:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:NR5G:EFILter:PRESet \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.efilter.preset_with_opc() \n
		This command removes all event filters. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:NR5G:EFILter:PRESet', opc_timeout_ms)

	def clone(self) -> 'Efilter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Efilter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
