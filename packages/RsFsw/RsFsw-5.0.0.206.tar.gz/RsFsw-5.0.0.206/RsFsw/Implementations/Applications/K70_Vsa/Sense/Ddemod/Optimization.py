from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimization:
	"""Optimization commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimization", core, parent)

	def set(self, criterion: enums.OptimizationCriterion) -> None:
		"""SCPI: [SENSe]:DDEMod:OPTimization \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.optimization.set(criterion = enums.OptimizationCriterion.EVMMin) \n
		This command determines the optimization criteria for the demodulation. \n
			:param criterion: RMSMin | EVMMin RMSMin Optimizes calculation such that the RMS of the error vector is minimal. EVMMin Optimizes calculation such that EVM is minimal.
		"""
		param = Conversions.enum_scalar_to_str(criterion, enums.OptimizationCriterion)
		self._core.io.write(f'SENSe:DDEMod:OPTimization {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OptimizationCriterion:
		"""SCPI: [SENSe]:DDEMod:OPTimization \n
		Snippet: value: enums.OptimizationCriterion = driver.applications.k70Vsa.sense.ddemod.optimization.get() \n
		This command determines the optimization criteria for the demodulation. \n
			:return: criterion: RMSMin | EVMMin RMSMin Optimizes calculation such that the RMS of the error vector is minimal. EVMMin Optimizes calculation such that EVM is minimal."""
		response = self._core.io.query_str(f'SENSe:DDEMod:OPTimization?')
		return Conversions.str_to_scalar_enum(response, enums.OptimizationCriterion)
