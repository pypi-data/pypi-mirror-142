from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CetAverage:
	"""CetAverage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cetAverage", core, parent)

	def set(self, state: enums.AveragingMode) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CETaverage \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.cetAverage.set(state = enums.AveragingMode.PALL) \n
		This command select the averaging interval for channel estimation. \n
			:param state: PALL Averaging every allocation. TGPP Averaging according to 3GPP.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AveragingMode)
		self._core.io.write(f'SENSe:NR5G:DEMod:CETaverage {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AveragingMode:
		"""SCPI: [SENSe]:NR5G:DEMod:CETaverage \n
		Snippet: value: enums.AveragingMode = driver.applications.k14Xnr5G.sense.nr5G.demod.cetAverage.get() \n
		This command select the averaging interval for channel estimation. \n
			:return: state: PALL Averaging every allocation. TGPP Averaging according to 3GPP."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CETaverage?')
		return Conversions.str_to_scalar_enum(response, enums.AveragingMode)
