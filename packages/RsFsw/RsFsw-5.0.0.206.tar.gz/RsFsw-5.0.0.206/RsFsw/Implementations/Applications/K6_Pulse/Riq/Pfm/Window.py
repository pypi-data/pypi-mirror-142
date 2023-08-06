from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, window_type: enums.IqFftWindowType) -> None:
		"""SCPI: RIQ:PFM:WINDow \n
		Snippet: driver.applications.k6Pulse.riq.pfm.window.set(window_type = enums.IqFftWindowType.BLACkman) \n
		Defines the FFT window function to be applied to the reference I/Q data. By default, a rectangular window function is
		applied (i.e. no windowing) . For details on the effects of FFT windowing functions see Table 'Characteristics of typical
		FFT window functions'. \n
			:param window_type: RECTangle | GAUSs | CHEByshev | FLATtop | HAMMing | HANNing | BLACkman
		"""
		param = Conversions.enum_scalar_to_str(window_type, enums.IqFftWindowType)
		self._core.io.write(f'RIQ:PFM:WINDow {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqFftWindowType:
		"""SCPI: RIQ:PFM:WINDow \n
		Snippet: value: enums.IqFftWindowType = driver.applications.k6Pulse.riq.pfm.window.get() \n
		Defines the FFT window function to be applied to the reference I/Q data. By default, a rectangular window function is
		applied (i.e. no windowing) . For details on the effects of FFT windowing functions see Table 'Characteristics of typical
		FFT window functions'. \n
			:return: window_type: RECTangle | GAUSs | CHEByshev | FLATtop | HAMMing | HANNing | BLACkman"""
		response = self._core.io.query_str(f'RIQ:PFM:WINDow?')
		return Conversions.str_to_scalar_enum(response, enums.IqFftWindowType)
