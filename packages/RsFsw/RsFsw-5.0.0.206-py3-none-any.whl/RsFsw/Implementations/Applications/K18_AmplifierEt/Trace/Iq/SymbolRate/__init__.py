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
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.symbolRate.set(sample_rate = 1.0) \n
		This command defines the sample rate with which the amplified signal is captured. This command is available when method
		RsFsw.Applications.K18_AmplifierEt.Trace.Iq.SymbolRate.Auto.set has been turned off. Note that when you change the sample
		rate, the analysis bandwidth and capture length are adjusted automatically to the new sample rate. \n
			:param sample_rate: numeric value Note that the application automatically adjusts the analysis bandwidth when you change the sample rate manually. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'TRACe:IQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.trace.iq.symbolRate.get() \n
		This command defines the sample rate with which the amplified signal is captured. This command is available when method
		RsFsw.Applications.K18_AmplifierEt.Trace.Iq.SymbolRate.Auto.set has been turned off. Note that when you change the sample
		rate, the analysis bandwidth and capture length are adjusted automatically to the new sample rate. \n
			:return: sample_rate: numeric value Note that the application automatically adjusts the analysis bandwidth when you change the sample rate manually. Unit: Hz"""
		response = self._core.io.query_str(f'TRACe:IQ:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SymbolRate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
