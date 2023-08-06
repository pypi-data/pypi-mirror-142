from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 98 total commands, 4 Subgroups, 0 group commands
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
	def cycPrefix(self):
		"""cycPrefix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycPrefix'):
			from .CycPrefix import CycPrefix
			self._cycPrefix = CycPrefix(self._core, self._cmd_group)
		return self._cycPrefix

	@property
	def plc(self):
		"""plc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_plc'):
			from .Plc import Plc
			self._plc = Plc(self._core, self._cmd_group)
		return self._plc

	@property
	def plci(self):
		"""plci commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_plci'):
			from .Plci import Plci
			self._plci = Plci(self._core, self._cmd_group)
		return self._plci

	@property
	def summary(self):
		"""summary commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_summary'):
			from .Summary import Summary
			self._summary = Summary(self._core, self._cmd_group)
		return self._summary

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
