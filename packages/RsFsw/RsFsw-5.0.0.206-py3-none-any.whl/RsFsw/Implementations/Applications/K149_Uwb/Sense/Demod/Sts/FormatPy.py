from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, sts_format: enums.StsFormat) -> None:
		"""SCPI: [SENSe]:DEMod:STS:FORMat \n
		Snippet: driver.applications.k149Uwb.sense.demod.sts.formatPy.set(sts_format = enums.StsFormat.F0) \n
		Sets the STS format. \n
			:param sts_format: F0 | F1 | F2 | F3
		"""
		param = Conversions.enum_scalar_to_str(sts_format, enums.StsFormat)
		self._core.io.write(f'SENSe:DEMod:STS:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StsFormat:
		"""SCPI: [SENSe]:DEMod:STS:FORMat \n
		Snippet: value: enums.StsFormat = driver.applications.k149Uwb.sense.demod.sts.formatPy.get() \n
		Sets the STS format. \n
			:return: sts_format: F0 | F1 | F2 | F3"""
		response = self._core.io.query_str(f'SENSe:DEMod:STS:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.StsFormat)
