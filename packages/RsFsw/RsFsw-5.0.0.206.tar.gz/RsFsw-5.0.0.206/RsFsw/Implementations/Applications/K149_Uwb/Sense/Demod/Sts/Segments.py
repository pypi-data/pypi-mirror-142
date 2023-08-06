from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segments:
	"""Segments commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segments", core, parent)

	def set(self, sts_segments: enums.StsSegments) -> None:
		"""SCPI: [SENSe]:DEMod:STS:SEGMents \n
		Snippet: driver.applications.k149Uwb.sense.demod.sts.segments.set(sts_segments = enums.StsSegments.S1) \n
		Sets the STS segments. \n
			:param sts_segments: S1 | S2 | S3 | S4
		"""
		param = Conversions.enum_scalar_to_str(sts_segments, enums.StsSegments)
		self._core.io.write(f'SENSe:DEMod:STS:SEGMents {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StsSegments:
		"""SCPI: [SENSe]:DEMod:STS:SEGMents \n
		Snippet: value: enums.StsSegments = driver.applications.k149Uwb.sense.demod.sts.segments.get() \n
		Sets the STS segments. \n
			:return: sts_segments: S1 | S2 | S3 | S4"""
		response = self._core.io.query_str(f'SENSe:DEMod:STS:SEGMents?')
		return Conversions.str_to_scalar_enum(response, enums.StsSegments)
