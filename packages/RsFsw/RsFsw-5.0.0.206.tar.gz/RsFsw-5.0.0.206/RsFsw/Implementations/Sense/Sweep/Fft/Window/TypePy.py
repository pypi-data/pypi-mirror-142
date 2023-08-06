from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, fft_window: enums.FftWindowType) -> None:
		"""SCPI: [SENSe]:SWEep:FFT:WINDow:TYPE \n
		Snippet: driver.sense.sweep.fft.window.typePy.set(fft_window = enums.FftWindowType.BLACkharris) \n
		This command selects the type of FFT window that you want to use in Real-Time mode. \n
			:param fft_window: BLACkharris FLATtop GAUSsian HAMMing HANNing KAISerbessel RECTangular
		"""
		param = Conversions.enum_scalar_to_str(fft_window, enums.FftWindowType)
		self._core.io.write(f'SENSe:SWEep:FFT:WINDow:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FftWindowType:
		"""SCPI: [SENSe]:SWEep:FFT:WINDow:TYPE \n
		Snippet: value: enums.FftWindowType = driver.sense.sweep.fft.window.typePy.get() \n
		This command selects the type of FFT window that you want to use in Real-Time mode. \n
			:return: fft_window: BLACkharris FLATtop GAUSsian HAMMing HANNing KAISerbessel RECTangular"""
		response = self._core.io.query_str(f'SENSe:SWEep:FFT:WINDow:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FftWindowType)
