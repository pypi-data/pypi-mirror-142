from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, sample_rate: float) -> None:
		"""SCPI: INPut:DIQ:SRATe \n
		Snippet: driver.applications.k14Xnr5G.inputPy.diq.symbolRate.set(sample_rate = 1.0) \n
		This command specifies or queries the sample rate of the input signal from the optional Digital Baseband Interface. \n
			:param sample_rate: Range: 1 Hz to 20 GHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'INPut:DIQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: INPut:DIQ:SRATe \n
		Snippet: value: float = driver.applications.k14Xnr5G.inputPy.diq.symbolRate.get() \n
		This command specifies or queries the sample rate of the input signal from the optional Digital Baseband Interface. \n
			:return: sample_rate: Range: 1 Hz to 20 GHz, Unit: HZ"""
		response = self._core.io.query_str(f'INPut:DIQ:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SymbolRate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
