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

	def set(self, mode: enums.ScalingMode) -> None:
		"""SCPI: [SENSe]:BWIDth:VIDeo:TYPE \n
		Snippet: driver.applications.k10Xlte.sense.bandwidth.video.typePy.set(mode = enums.ScalingMode.LINear) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ScalingMode)
		self._core.io.write(f'SENSe:BWIDth:VIDeo:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ScalingMode:
		"""SCPI: [SENSe]:BWIDth:VIDeo:TYPE \n
		Snippet: value: enums.ScalingMode = driver.applications.k10Xlte.sense.bandwidth.video.typePy.get() \n
		No command help available \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:VIDeo:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingMode)
