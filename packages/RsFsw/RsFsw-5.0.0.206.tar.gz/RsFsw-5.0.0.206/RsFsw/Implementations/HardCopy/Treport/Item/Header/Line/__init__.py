from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Line:
	"""Line commands group definition. 3 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Line, default value after init: Line.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("line", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_line_get', 'repcap_line_set', repcap.Line.Ix1)

	def repcap_line_set(self, line: repcap.Line) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Line.Default
		Default value after init: Line.Ix1"""
		self._cmd_group.set_repcap_enum_value(line)

	def repcap_line_get(self) -> repcap.Line:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def control(self):
		"""control commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Text import Text
			self._text = Text(self._core, self._cmd_group)
		return self._text

	@property
	def title(self):
		"""title commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_title'):
			from .Title import Title
			self._title = Title(self._core, self._cmd_group)
		return self._title

	def clone(self) -> 'Line':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Line(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
