from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


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

	def get(self) -> str:
		"""SCPI: TRACe:IQ:DATA \n
		Snippet: value: str = driver.applications.k60Transient.trace.iq.data.get() \n
		This command initiates a measurement with the current settings and returns the captured data from I/Q measurements. This
		command corresponds to: INIT:IMM;*WAI;method RsFsw.Trace.Iq.Data.Memory.get_ However, the method RsFsw.Trace.Iq.Data.get_
		command is quicker in comparison. \n
			:return: results: Measured voltage for I and Q component for each sample that has been captured during the measurement. For more information see 'I/Q Processing Modes'. Unit: V"""
		response = self._core.io.query_str(f'TRACe:IQ:DATA?')
		return trim_str_response(response)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
