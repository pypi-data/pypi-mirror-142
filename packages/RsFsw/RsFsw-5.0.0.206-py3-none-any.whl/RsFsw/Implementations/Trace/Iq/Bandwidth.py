from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: TRACe:IQ:BWIDth \n
		Snippet: driver.trace.iq.bandwidth.set(bandwidth = 1.0) \n
		This command defines or queries the bandwidth of the resampling filter. The bandwidth of the resampling filter depends on
		the sample rate. \n
			:param bandwidth: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'TRACe:IQ:BWIDth {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:BWIDth \n
		Snippet: value: float = driver.trace.iq.bandwidth.get() \n
		This command defines or queries the bandwidth of the resampling filter. The bandwidth of the resampling filter depends on
		the sample rate. \n
			:return: bandwidth: Unit: HZ"""
		response = self._core.io.query_str(f'TRACe:IQ:BWIDth?')
		return Conversions.str_to_float(response)
