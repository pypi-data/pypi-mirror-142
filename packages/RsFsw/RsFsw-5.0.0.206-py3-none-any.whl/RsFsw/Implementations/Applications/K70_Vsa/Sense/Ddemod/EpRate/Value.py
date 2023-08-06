from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, est_oversampling: float) -> None:
		"""SCPI: [SENSe]:DDEMod:EPRate[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.epRate.value.set(est_oversampling = 1.0) \n
		Defines how many sample points are used at each symbol to calculate modulation accuracy results. For more information see
		'Estimation points per symbol'. You can also let the VSA application decide how many estimation points to use, see
		[SENSe:]DDEMod:EPRate:AUTO. \n
			:param est_oversampling: 1 the estimation algorithm takes only the symbol time instants into account 2 two points per symbol instant are used (required for Offset QPSK) 4 | 8 | 16 | 32 the number of samples per symbol defined in the signal capture settings is used (see [SENSe:]DDEMod:PRATe) , i.e. all sample time instants are weighted equally
		"""
		param = Conversions.decimal_value_to_str(est_oversampling)
		self._core.io.write(f'SENSe:DDEMod:EPRate:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:EPRate[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.epRate.value.get() \n
		Defines how many sample points are used at each symbol to calculate modulation accuracy results. For more information see
		'Estimation points per symbol'. You can also let the VSA application decide how many estimation points to use, see
		[SENSe:]DDEMod:EPRate:AUTO. \n
			:return: est_oversampling: 1 the estimation algorithm takes only the symbol time instants into account 2 two points per symbol instant are used (required for Offset QPSK) 4 | 8 | 16 | 32 the number of samples per symbol defined in the signal capture settings is used (see [SENSe:]DDEMod:PRATe) , i.e. all sample time instants are weighted equally"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EPRate:VALue?')
		return Conversions.str_to_float(response)
