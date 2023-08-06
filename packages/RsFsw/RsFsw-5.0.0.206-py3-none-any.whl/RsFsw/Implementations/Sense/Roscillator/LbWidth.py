from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LbWidth:
	"""LbWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lbWidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:ROSCillator:LBWidth \n
		Snippet: driver.sense.roscillator.lbWidth.set(bandwidth = 1.0) \n
		Defines the loop bandwidth, that is, the speed of internal synchronization with the reference frequency. The setting
		requires a compromise between performance and increasing phase noise. For a variable external reference frequency with a
		narrow tuning range (+/- 0.5 ppm) , the loop bandwidth is fixed to 0.1 Hz and cannot be changed. \n
			:param bandwidth: 0.1 Hz | 1 Hz | 3 Hz | 10 Hz | 30 Hz | 100 Hz | 300 Hz The possible values depend on the reference source and tuning range (see Table 'Available Reference Frequency Input') . Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:ROSCillator:LBWidth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ROSCillator:LBWidth \n
		Snippet: value: float = driver.sense.roscillator.lbWidth.get() \n
		Defines the loop bandwidth, that is, the speed of internal synchronization with the reference frequency. The setting
		requires a compromise between performance and increasing phase noise. For a variable external reference frequency with a
		narrow tuning range (+/- 0.5 ppm) , the loop bandwidth is fixed to 0.1 Hz and cannot be changed. \n
			:return: bandwidth: 0.1 Hz | 1 Hz | 3 Hz | 10 Hz | 30 Hz | 100 Hz | 300 Hz The possible values depend on the reference source and tuning range (see Table 'Available Reference Frequency Input') . Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:ROSCillator:LBWidth?')
		return Conversions.str_to_float(response)
