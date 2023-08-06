from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espectrum:
	"""Espectrum commands group definition. 9 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: SubBlock, default value after init: SubBlock.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espectrum", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subBlock_get', 'repcap_subBlock_set', repcap.SubBlock.Nr1)

	def repcap_subBlock_set(self, subBlock: repcap.SubBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubBlock.Default
		Default value after init: SubBlock.Nr1"""
		self._cmd_group.set_repcap_enum_value(subBlock)

	def repcap_subBlock_get(self) -> repcap.SubBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def restore(self):
		"""restore commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restore'):
			from .Restore import Restore
			self._restore = Restore(self._core, self._cmd_group)
		return self._restore

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	@property
	def pclass(self):
		"""pclass commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pclass'):
			from .Pclass import Pclass
			self._pclass = Pclass(self._core, self._cmd_group)
		return self._pclass

	@property
	def limits(self):
		"""limits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limits'):
			from .Limits import Limits
			self._limits = Limits(self._core, self._cmd_group)
		return self._limits

	def clone(self) -> 'Espectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Espectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
