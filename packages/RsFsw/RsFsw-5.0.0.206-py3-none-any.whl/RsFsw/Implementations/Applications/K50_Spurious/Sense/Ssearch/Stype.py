from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stype:
	"""Stype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stype", core, parent)

	def set(self, type_py: enums.MeasurementType) -> None:
		"""SCPI: [SENSe]:SSEarch:STYPe \n
		Snippet: driver.applications.k50Spurious.sense.ssearch.stype.set(type_py = enums.MeasurementType.DIRected) \n
		Defines the type of measurement to be configured and performed. \n
			:param type_py: WIDE | DIRected WIDE A measurement with a large span to detect any possible spurs in the entire frequency span of an input signal. This measurement is useful if you have little or no knowledge of the current input signal or where to expect spurs, and require an overview. DIRected A measurement performed at predefined discrete frequencies with settings optimized for the current signal and noise levels at those frequencies. This measurement is targeted at determining the precise level and exact frequency of spurs that are basically already known or expected.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MeasurementType)
		self._core.io.write(f'SENSe:SSEarch:STYPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementType:
		"""SCPI: [SENSe]:SSEarch:STYPe \n
		Snippet: value: enums.MeasurementType = driver.applications.k50Spurious.sense.ssearch.stype.get() \n
		Defines the type of measurement to be configured and performed. \n
			:return: type_py: WIDE | DIRected WIDE A measurement with a large span to detect any possible spurs in the entire frequency span of an input signal. This measurement is useful if you have little or no knowledge of the current input signal or where to expect spurs, and require an overview. DIRected A measurement performed at predefined discrete frequencies with settings optimized for the current signal and noise levels at those frequencies. This measurement is targeted at determining the precise level and exact frequency of spurs that are basically already known or expected."""
		response = self._core.io.query_str(f'SENSe:SSEarch:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementType)
