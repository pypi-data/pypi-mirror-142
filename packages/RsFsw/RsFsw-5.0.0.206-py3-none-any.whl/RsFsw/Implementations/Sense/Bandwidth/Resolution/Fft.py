from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fft:
	"""Fft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fft", core, parent)

	def set(self, filter_mode: enums.FftFilterMode) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:FFT \n
		Snippet: driver.sense.bandwidth.resolution.fft.set(filter_mode = enums.FftFilterMode.AUTO) \n
		Defines the filter mode to be used for FFT filters by defining the subspan size. The subspan is the span which is covered
		by one FFT analysis. This command is only available when using the sweep type 'FFT'. Note: this command is maintained for
		compatibility reasons only. For new remote control programs, use the [SENSe:]SWEep:OPTimize command. \n
			:param filter_mode: WIDE | AUTO | NARRow AUTO Automatically applies the sweep optimization mode that is best for the current measurement. NARRow Optimizes the sweep mode for a large dynamic range. WIDE Optimizes the sweep mode for high performance.
		"""
		param = Conversions.enum_scalar_to_str(filter_mode, enums.FftFilterMode)
		self._core.io.write(f'SENSe:BWIDth:RESolution:FFT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FftFilterMode:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:FFT \n
		Snippet: value: enums.FftFilterMode = driver.sense.bandwidth.resolution.fft.get() \n
		Defines the filter mode to be used for FFT filters by defining the subspan size. The subspan is the span which is covered
		by one FFT analysis. This command is only available when using the sweep type 'FFT'. Note: this command is maintained for
		compatibility reasons only. For new remote control programs, use the [SENSe:]SWEep:OPTimize command. \n
			:return: filter_mode: WIDE | AUTO | NARRow AUTO Automatically applies the sweep optimization mode that is best for the current measurement. NARRow Optimizes the sweep mode for a large dynamic range. WIDE Optimizes the sweep mode for high performance."""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:FFT?')
		return Conversions.str_to_scalar_enum(response, enums.FftFilterMode)
