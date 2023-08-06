from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spurs:
	"""Spurs commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spurs", core, parent)

	@property
	def discrete(self):
		"""discrete commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_discrete'):
			from .Discrete import Discrete
			self._discrete = Discrete(self._core, self._cmd_group)
		return self._discrete

	@property
	def random(self):
		"""random commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_random'):
			from .Random import Random
			self._random = Random(self._core, self._cmd_group)
		return self._random

	def get(self, trace=repcap.Trace.Default) -> List[float]:
		"""SCPI: FETCh:PNOise<t>:SPURs \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.fetch.pnoise.spurs.get(trace = repcap.Trace.Default) \n
		This command queries the location and level of all spurs that have been detected. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: spurs: Returns two values (frequency and level) for each each spur that has been detected."""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:PNOise{trace_cmd_val}:SPURs?')
		return response

	def clone(self) -> 'Spurs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spurs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
