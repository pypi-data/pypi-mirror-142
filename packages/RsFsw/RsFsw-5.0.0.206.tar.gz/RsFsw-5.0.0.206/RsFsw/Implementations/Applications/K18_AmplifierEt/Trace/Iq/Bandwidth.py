from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: TRACe:IQ:BWIDth \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.bandwidth.set(bandwidth = 1.0) \n
		This command defines the analysis bandwidth with which the amplified signal is captured. This command is available when
		method RsFsw.Applications.K18_AmplifierEt.Trace.Iq.SymbolRate.Auto.set has been turned off. Note that when you change the
		analysis bandwidth, the sample rate and capture length are adjusted automatically to the new bandwidth. \n
			:param bandwidth: numeric value Note that the application automatically adjusts the sample rate when you change the bandwidth manually. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'TRACe:IQ:BWIDth {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:BWIDth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.trace.iq.bandwidth.get() \n
		This command defines the analysis bandwidth with which the amplified signal is captured. This command is available when
		method RsFsw.Applications.K18_AmplifierEt.Trace.Iq.SymbolRate.Auto.set has been turned off. Note that when you change the
		analysis bandwidth, the sample rate and capture length are adjusted automatically to the new bandwidth. \n
			:return: bandwidth: numeric value Note that the application automatically adjusts the sample rate when you change the bandwidth manually. Unit: Hz"""
		response = self._core.io.query_str(f'TRACe:IQ:BWIDth?')
		return Conversions.str_to_float(response)
