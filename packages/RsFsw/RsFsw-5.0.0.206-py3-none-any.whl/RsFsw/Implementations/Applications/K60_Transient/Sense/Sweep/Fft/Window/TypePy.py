from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, color_scheme: enums.FftWindowTypeK60) -> None:
		"""SCPI: [SENSe]:SWEep:FFT:WINDow:TYPE \n
		Snippet: driver.applications.k60Transient.sense.sweep.fft.window.typePy.set(color_scheme = enums.FftWindowTypeK60.BLACkharris) \n
		This command queries or sets the FFT windowing function. \n
			:param color_scheme: BLACkharris | CHEByshev | FLATtop | GAUSsian | HAMMing | HANNing | RECTangular
		"""
		param = Conversions.enum_scalar_to_str(color_scheme, enums.FftWindowTypeK60)
		self._core.io.write(f'SENSe:SWEep:FFT:WINDow:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FftWindowTypeK60:
		"""SCPI: [SENSe]:SWEep:FFT:WINDow:TYPE \n
		Snippet: value: enums.FftWindowTypeK60 = driver.applications.k60Transient.sense.sweep.fft.window.typePy.get() \n
		This command queries or sets the FFT windowing function. \n
			:return: color_scheme: BLACkharris | CHEByshev | FLATtop | GAUSsian | HAMMing | HANNing | RECTangular"""
		response = self._core.io.query_str(f'SENSe:SWEep:FFT:WINDow:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FftWindowTypeK60)
