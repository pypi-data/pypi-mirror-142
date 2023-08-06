from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 11 total commands, 11 Subgroups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, carrierComponent: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponent)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def allocation(self):
		"""allocation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_allocation'):
			from .Allocation import Allocation
			self._allocation = Allocation(self._core, self._cmd_group)
		return self._allocation

	@property
	def bwPart(self):
		"""bwPart commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwPart'):
			from .BwPart import BwPart
			self._bwPart = BwPart(self._core, self._cmd_group)
		return self._bwPart

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def frame(self):
		"""frame commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def preamble(self):
		"""preamble commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def rap(self):
		"""rap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rap'):
			from .Rap import Rap
			self._rap = Rap(self._core, self._cmd_group)
		return self._rap

	@property
	def slot(self):
		"""slot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def smId(self):
		"""smId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smId'):
			from .SmId import SmId
			self._smId = SmId(self._core, self._cmd_group)
		return self._smId

	@property
	def subframe(self):
		"""subframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import Subframe
			self._subframe = Subframe(self._core, self._cmd_group)
		return self._subframe

	@property
	def symbol(self):
		"""symbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import Symbol
			self._symbol = Symbol(self._core, self._cmd_group)
		return self._symbol

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
