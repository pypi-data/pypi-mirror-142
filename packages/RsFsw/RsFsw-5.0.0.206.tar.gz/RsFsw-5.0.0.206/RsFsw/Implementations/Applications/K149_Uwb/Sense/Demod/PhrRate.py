from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhrRate:
	"""PhrRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phrRate", core, parent)

	def set(self, phr_rate: enums.PhrRate) -> None:
		"""SCPI: [SENSe]:DEMod:PHRRate \n
		Snippet: driver.applications.k149Uwb.sense.demod.phrRate.set(phr_rate = enums.PhrRate.BMHP) \n
		Selects PHY Mode/Rate modes. \n
			:param phr_rate: BMLP | BMHP | HMLR | HMHR
		"""
		param = Conversions.enum_scalar_to_str(phr_rate, enums.PhrRate)
		self._core.io.write(f'SENSe:DEMod:PHRRate {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PhrRate:
		"""SCPI: [SENSe]:DEMod:PHRRate \n
		Snippet: value: enums.PhrRate = driver.applications.k149Uwb.sense.demod.phrRate.get() \n
		Selects PHY Mode/Rate modes. \n
			:return: phr_rate: BMLP | BMHP | HMLR | HMHR"""
		response = self._core.io.query_str(f'SENSe:DEMod:PHRRate?')
		return Conversions.str_to_scalar_enum(response, enums.PhrRate)
