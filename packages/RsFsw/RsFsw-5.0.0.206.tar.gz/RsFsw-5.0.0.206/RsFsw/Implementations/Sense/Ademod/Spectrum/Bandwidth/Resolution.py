from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:BWIDth[:RESolution] \n
		Snippet: driver.sense.ademod.spectrum.bandwidth.resolution.set(bandwidth = 1.0) \n
		Defines the resolution bandwidth for data acquisition. From the specified RBW and the demodulation span set by
		[SENSe:]ADEMod:SPECtrum:SPAN[:MAXimum] or [SENSe:]BWIDth:DEMod, the required measurement time is calculated.
		If the available measurement time is not sufficient for the given bandwidth, the measurement time is set to its maximum
		and the resolution bandwidth is increased to the resulting bandwidth.
		This command is identical to [SENSe:]BANDwidth[:RESolution]. \n
			:param bandwidth: refer to data sheet Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:BWIDth:RESolution {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:BWIDth[:RESolution] \n
		Snippet: value: float = driver.sense.ademod.spectrum.bandwidth.resolution.get() \n
		Defines the resolution bandwidth for data acquisition. From the specified RBW and the demodulation span set by
		[SENSe:]ADEMod:SPECtrum:SPAN[:MAXimum] or [SENSe:]BWIDth:DEMod, the required measurement time is calculated.
		If the available measurement time is not sufficient for the given bandwidth, the measurement time is set to its maximum
		and the resolution bandwidth is increased to the resulting bandwidth.
		This command is identical to [SENSe:]BANDwidth[:RESolution]. \n
			:return: bandwidth: refer to data sheet Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:BWIDth:RESolution?')
		return Conversions.str_to_float(response)
