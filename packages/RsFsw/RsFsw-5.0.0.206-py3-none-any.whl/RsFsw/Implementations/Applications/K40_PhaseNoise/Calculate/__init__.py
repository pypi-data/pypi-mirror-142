from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calculate:
	"""Calculate commands group definition. 61 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calculate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def snoise(self):
		"""snoise commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_snoise'):
			from .Snoise import Snoise
			self._snoise = Snoise(self._core, self._cmd_group)
		return self._snoise

	@property
	def limit(self):
		"""limit commands group. 11 Sub-classes, 2 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def pnLimit(self):
		"""pnLimit commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnLimit'):
			from .PnLimit import PnLimit
			self._pnLimit = PnLimit(self._core, self._cmd_group)
		return self._pnLimit

	@property
	def deltaMarker(self):
		"""deltaMarker commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarker
			self._deltaMarker = DeltaMarker(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def marker(self):
		"""marker commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	@property
	def evaluation(self):
		"""evaluation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evaluation'):
			from .Evaluation import Evaluation
			self._evaluation = Evaluation(self._core, self._cmd_group)
		return self._evaluation

	@property
	def math(self):
		"""math commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_math'):
			from .Math import Math
			self._math = Math(self._core, self._cmd_group)
		return self._math

	def clone(self) -> 'Calculate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calculate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
