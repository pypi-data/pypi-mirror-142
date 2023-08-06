from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mask:
	"""Mask commands group definition. 15 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mask", core, parent)

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def upper(self):
		"""upper commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	@property
	def lower(self):
		"""lower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import Lower
			self._lower = Lower(self._core, self._cmd_group)
		return self._lower

	@property
	def currentDirectory(self):
		"""currentDirectory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_currentDirectory'):
			from .CurrentDirectory import CurrentDirectory
			self._currentDirectory = CurrentDirectory(self._core, self._cmd_group)
		return self._currentDirectory

	@property
	def span(self):
		"""span commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_span'):
			from .Span import Span
			self._span = Span(self._core, self._cmd_group)
		return self._span

	def delete(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:DELete \n
		Snippet: driver.calculate.mask.delete(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:DELete')

	def delete_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:MASK:DELete \n
		Snippet: driver.calculate.mask.delete_with_opc(window = repcap.Window.Default) \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MASK:DELete', opc_timeout_ms)

	def clone(self) -> 'Mask':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mask(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
