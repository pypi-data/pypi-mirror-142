from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cvl:
	"""Cvl commands group definition. 11 total commands, 10 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cvl", core, parent)

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Band import Band
			self._band = Band(self._core, self._cmd_group)
		return self._band

	@property
	def bias(self):
		"""bias commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bias'):
			from .Bias import Bias
			self._bias = Bias(self._core, self._cmd_group)
		return self._bias

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def harmonic(self):
		"""harmonic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_harmonic'):
			from .Harmonic import Harmonic
			self._harmonic = Harmonic(self._core, self._cmd_group)
		return self._harmonic

	@property
	def mixer(self):
		"""mixer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import Mixer
			self._mixer = Mixer(self._core, self._cmd_group)
		return self._mixer

	@property
	def ports(self):
		"""ports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import Ports
			self._ports = Ports(self._core, self._cmd_group)
		return self._ports

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import Snumber
			self._snumber = Snumber(self._core, self._cmd_group)
		return self._snumber

	def clear(self) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:CLEar \n
		Snippet: driver.sense.correction.cvl.clear() \n
		This command deletes the selected conversion loss table. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
		"""
		self._core.io.write(f'SENSe:CORRection:CVL:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:CLEar \n
		Snippet: driver.sense.correction.cvl.clear_with_opc() \n
		This command deletes the selected conversion loss table. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:CVL:CLEar', opc_timeout_ms)

	def clone(self) -> 'Cvl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cvl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
