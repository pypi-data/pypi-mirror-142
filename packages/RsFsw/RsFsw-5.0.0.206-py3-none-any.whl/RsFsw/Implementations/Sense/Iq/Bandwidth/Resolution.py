from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:IQ:BWIDth:RESolution \n
		Snippet: driver.sense.iq.bandwidth.resolution.set(bandwidth = 1.0) \n
		This command defines the resolution bandwidth manually if [SENSe:]IQ:BWIDth:MODE is set to MAN. Defines the resolution
		bandwidth. The available RBW values depend on the sample rate and record length. For details see 'Frequency resolution of
		FFT results - RBW'. \n
			:param bandwidth: refer to data sheet Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:IQ:BWIDth:RESolution {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:IQ:BWIDth:RESolution \n
		Snippet: value: float = driver.sense.iq.bandwidth.resolution.get() \n
		This command defines the resolution bandwidth manually if [SENSe:]IQ:BWIDth:MODE is set to MAN. Defines the resolution
		bandwidth. The available RBW values depend on the sample rate and record length. For details see 'Frequency resolution of
		FFT results - RBW'. \n
			:return: bandwidth: refer to data sheet Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:IQ:BWIDth:RESolution?')
		return Conversions.str_to_float(response)
