from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Initiate:
	"""Initiate commands group definition. 13 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("initiate", core, parent)

	@property
	def spurious(self):
		"""spurious commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spurious'):
			from .Spurious import Spurious
			self._spurious = Spurious(self._core, self._cmd_group)
		return self._spurious

	@property
	def espectrum(self):
		"""espectrum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import Espectrum
			self._espectrum = Espectrum(self._core, self._cmd_group)
		return self._espectrum

	@property
	def refresh(self):
		"""refresh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refresh'):
			from .Refresh import Refresh
			self._refresh = Refresh(self._core, self._cmd_group)
		return self._refresh

	@property
	def sequencer(self):
		"""sequencer commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	@property
	def block(self):
		"""block commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_block'):
			from .Block import Block
			self._block = Block(self._core, self._cmd_group)
		return self._block

	@property
	def conMeas(self):
		"""conMeas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conMeas'):
			from .ConMeas import ConMeas
			self._conMeas = ConMeas(self._core, self._cmd_group)
		return self._conMeas

	@property
	def continuous(self):
		"""continuous commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_continuous'):
			from .Continuous import Continuous
			self._continuous = Continuous(self._core, self._cmd_group)
		return self._continuous

	def immediate(self) -> None:
		"""SCPI: INITiate[:IMMediate] \n
		Snippet: driver.initiate.immediate() \n
		This command starts a (single) new measurement. With sweep count or average count > 0, this means a restart of the
		corresponding number of measurements. With trace mode MAXHold, MINHold and AVERage, the previous results are reset on
		restarting the measurement. You can synchronize to the end of the measurement with *OPC, *OPC? or *WAI. For details on
		synchronization see Remote control via SCPI. \n
		"""
		self._core.io.write(f'INITiate:IMMediate')

	def immediate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate[:IMMediate] \n
		Snippet: driver.initiate.immediate_with_opc() \n
		This command starts a (single) new measurement. With sweep count or average count > 0, this means a restart of the
		corresponding number of measurements. With trace mode MAXHold, MINHold and AVERage, the previous results are reset on
		restarting the measurement. You can synchronize to the end of the measurement with *OPC, *OPC? or *WAI. For details on
		synchronization see Remote control via SCPI. \n
		Same as immediate, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:IMMediate', opc_timeout_ms)

	def clone(self) -> 'Initiate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Initiate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
