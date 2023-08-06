from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Width:
	"""Width commands group definition. 8 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("width", core, parent)

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import Maximum
			self._maximum = Maximum(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import Minimum
			self._minimum = Minimum(self._core, self._cmd_group)
		return self._minimum

	@property
	def passed(self):
		"""passed commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_passed'):
			from .Passed import Passed
			self._passed = Passed(self._core, self._cmd_group)
		return self._passed

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh<n>:SUMMary:XCORr:MLOBe:WIDTh \n
		Snippet: value: float = driver.applications.k149Uwb.fetch.summary.xcorr.mlobe.width.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:SUMMary:XCORr:MLOBe:WIDTh?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Width':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Width(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
