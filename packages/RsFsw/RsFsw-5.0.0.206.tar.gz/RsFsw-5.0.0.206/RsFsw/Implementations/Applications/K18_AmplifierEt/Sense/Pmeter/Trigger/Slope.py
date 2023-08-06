from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slope:
	"""Slope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)

	def set(self, edge: enums.SlopeType) -> None:
		"""SCPI: [SENSe]:PMETer:TRIGger:SLOPe \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.slope.set(edge = enums.SlopeType.NEGative) \n
		This command selects the trigger condition for external power triggers. \n
			:param edge: POSitive The measurement starts in case the trigger signal shows a positive edge. NEGative The measurement starts in case the trigger signal shows a negative edge.
		"""
		param = Conversions.enum_scalar_to_str(edge, enums.SlopeType)
		self._core.io.write(f'SENSe:PMETer:TRIGger:SLOPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SlopeType:
		"""SCPI: [SENSe]:PMETer:TRIGger:SLOPe \n
		Snippet: value: enums.SlopeType = driver.applications.k18AmplifierEt.sense.pmeter.trigger.slope.get() \n
		This command selects the trigger condition for external power triggers. \n
			:return: edge: POSitive The measurement starts in case the trigger signal shows a positive edge. NEGative The measurement starts in case the trigger signal shows a negative edge."""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
