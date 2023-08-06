from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def memory(self):
		"""memory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_memory'):
			from .Memory import Memory
			self._memory = Memory(self._core, self._cmd_group)
		return self._memory

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	def get(self) -> List[float]:
		"""SCPI: TRACe:IQ:DATA \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.trace.iq.data.get() \n
		Sweeps and transfers raw I/Q data. \n
			:return: iq_data: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe:IQ:DATA?')
		return response

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
