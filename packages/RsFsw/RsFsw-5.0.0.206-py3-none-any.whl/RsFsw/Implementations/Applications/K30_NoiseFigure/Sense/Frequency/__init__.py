from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 9 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def single(self):
		"""single commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_single'):
			from .Single import Single
			self._single = Single(self._core, self._cmd_group)
		return self._single

	@property
	def table(self):
		"""table commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	@property
	def stop(self):
		"""stop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stop'):
			from .Stop import Stop
			self._stop = Stop(self._core, self._cmd_group)
		return self._stop

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	@property
	def span(self):
		"""span commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_span'):
			from .Span import Span
			self._span = Span(self._core, self._cmd_group)
		return self._span

	@property
	def points(self):
		"""points commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_points'):
			from .Points import Points
			self._points = Points(self._core, self._cmd_group)
		return self._points

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
