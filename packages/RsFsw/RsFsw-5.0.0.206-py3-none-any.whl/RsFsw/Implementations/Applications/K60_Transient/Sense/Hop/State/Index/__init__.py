from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

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
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._cmd_group)
		return self._standardDev

	def get(self, query_range: enums.SelectionRange) -> str:
		"""SCPI: [SENSe]:HOP:STATe[:INDex] \n
		Snippet: value: str = driver.applications.k60Transient.sense.hop.state.index.get(query_range = enums.SelectionRange.ALL) \n
		Returns the hop state indexes from the Results table for the specified hop(s) . \n
			:param query_range: SELected | CURRent | ALL SELected Selected hop CURRent Detected hops in the current capture buffer ALL All hops detected in the entire measurement
			:return: result: integer"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRange)
		response = self._core.io.query_str(f'SENSe:HOP:STATe:INDex? {param}')
		return trim_str_response(response)

	def clone(self) -> 'Index':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Index(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
