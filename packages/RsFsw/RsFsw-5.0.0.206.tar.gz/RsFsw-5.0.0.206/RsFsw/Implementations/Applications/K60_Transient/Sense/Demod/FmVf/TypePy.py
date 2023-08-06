from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, fm_video_filter_type: enums.FmVideoFilterType) -> None:
		"""SCPI: [SENSe]:DEMod:FMVF:TYPE \n
		Snippet: driver.applications.k60Transient.sense.demod.fmVf.typePy.set(fm_video_filter_type = enums.FmVideoFilterType.LP01) \n
		Activates or deactivates additional filters applied after demodulation to filter out unwanted signals, or correct
		pre-emphasized input signals. \n
			:param fm_video_filter_type: NONE | LP01 | LP1 | LP5 | LP10 | LP25 NONE No video filter applied LP01 Low pass filter 0.1 % bandwidth LP1 Low pass filter1 % bandwidth LP5 Low pass filter 5 % bandwidth LP10 Low pass filter 10 % bandwidth LP25 Low pass filter 25 % bandwidth
		"""
		param = Conversions.enum_scalar_to_str(fm_video_filter_type, enums.FmVideoFilterType)
		self._core.io.write(f'SENSe:DEMod:FMVF:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FmVideoFilterType:
		"""SCPI: [SENSe]:DEMod:FMVF:TYPE \n
		Snippet: value: enums.FmVideoFilterType = driver.applications.k60Transient.sense.demod.fmVf.typePy.get() \n
		Activates or deactivates additional filters applied after demodulation to filter out unwanted signals, or correct
		pre-emphasized input signals. \n
			:return: fm_video_filter_type: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:FMVF:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FmVideoFilterType)
