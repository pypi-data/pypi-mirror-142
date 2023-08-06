from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, mode: enums.FftOffsetMode) -> None:
		"""SCPI: [SENSe]:DEMod:FFT:OFFSet \n
		Snippet: driver.applications.k91Wlan.sense.demod.fft.offset.set(mode = enums.FftOffsetMode.AUTO) \n
		This command specifies the start offset of the FFT for OFDM demodulation (not for the FFT Spectrum display) . \n
			:param mode: AUTO | GICenter | PEAK AUTO The FFT start offset is automatically chosen to minimize the intersymbol interference. GICenter Guard Interval Center: The FFT start offset is placed to the center of the guard interval. PEAK The peak of the fine timing metric is used to determine the FFT start offset.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FftOffsetMode)
		self._core.io.write(f'SENSe:DEMod:FFT:OFFSet {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FftOffsetMode:
		"""SCPI: [SENSe]:DEMod:FFT:OFFSet \n
		Snippet: value: enums.FftOffsetMode = driver.applications.k91Wlan.sense.demod.fft.offset.get() \n
		This command specifies the start offset of the FFT for OFDM demodulation (not for the FFT Spectrum display) . \n
			:return: mode: AUTO | GICenter | PEAK AUTO The FFT start offset is automatically chosen to minimize the intersymbol interference. GICenter Guard Interval Center: The FFT start offset is placed to the center of the guard interval. PEAK The peak of the fine timing metric is used to determine the FFT start offset."""
		response = self._core.io.query_str(f'SENSe:DEMod:FFT:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.FftOffsetMode)
