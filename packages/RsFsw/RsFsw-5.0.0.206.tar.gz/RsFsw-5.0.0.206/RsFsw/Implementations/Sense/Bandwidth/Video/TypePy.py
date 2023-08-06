from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, mode: enums.ScalingMode) -> None:
		"""SCPI: [SENSe]:BWIDth:VIDeo:TYPE \n
		Snippet: driver.sense.bandwidth.video.typePy.set(mode = enums.ScalingMode.LINear) \n
		This command enables or disables the logarithmic amplifier in front of the video filter in the signal path. \n
			:param mode: LINear The logarithmic amplifier in front of the video filter is bypassed to process linear detector samples. LOGarithmic The logarithmic amplifier in front of the video filter is enabled to process logarithmic detector samples.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ScalingMode)
		self._core.io.write(f'SENSe:BWIDth:VIDeo:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ScalingMode:
		"""SCPI: [SENSe]:BWIDth:VIDeo:TYPE \n
		Snippet: value: enums.ScalingMode = driver.sense.bandwidth.video.typePy.get() \n
		This command enables or disables the logarithmic amplifier in front of the video filter in the signal path. \n
			:return: mode: LINear The logarithmic amplifier in front of the video filter is bypassed to process linear detector samples. LOGarithmic The logarithmic amplifier in front of the video filter is enabled to process logarithmic detector samples."""
		response = self._core.io.query_str(f'SENSe:BWIDth:VIDeo:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingMode)
