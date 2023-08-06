from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 24 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: InputIx, default value after init: InputIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_inputIx_get', 'repcap_inputIx_set', repcap.InputIx.Nr1)

	def repcap_inputIx_set(self, inputIx: repcap.InputIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputIx.Default
		Default value after init: InputIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(inputIx)

	def repcap_inputIx_get(self) -> repcap.InputIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def user(self):
		"""user commands group. 6 Sub-classes, 2 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
