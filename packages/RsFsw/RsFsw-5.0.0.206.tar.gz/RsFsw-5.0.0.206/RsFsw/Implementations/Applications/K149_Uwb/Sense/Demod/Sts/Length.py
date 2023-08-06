from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, sts_format: enums.StsLength) -> None:
		"""SCPI: [SENSe]:DEMod:STS:LENGth \n
		Snippet: driver.applications.k149Uwb.sense.demod.sts.length.set(sts_format = enums.StsLength.L128) \n
		Sets the STS Length. \n
			:param sts_format: L16 | L32 | L64 | L128 | L256
		"""
		param = Conversions.enum_scalar_to_str(sts_format, enums.StsLength)
		self._core.io.write(f'SENSe:DEMod:STS:LENGth {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StsLength:
		"""SCPI: [SENSe]:DEMod:STS:LENGth \n
		Snippet: value: enums.StsLength = driver.applications.k149Uwb.sense.demod.sts.length.get() \n
		Sets the STS Length. \n
			:return: sts_format: L16 | L32 | L64 | L128 | L256"""
		response = self._core.io.query_str(f'SENSe:DEMod:STS:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.StsLength)
