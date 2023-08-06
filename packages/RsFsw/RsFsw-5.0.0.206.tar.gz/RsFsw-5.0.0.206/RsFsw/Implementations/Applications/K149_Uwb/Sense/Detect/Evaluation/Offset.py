from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: [SENSe]:DETect:EVALuation:OFFSet \n
		Snippet: driver.applications.k149Uwb.sense.detect.evaluation.offset.set(offset = 1.0) \n
		Sets the offset of the beginning of the detected burst to where to start detection within SYNC section. \n
			:param offset: numeric value
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SENSe:DETect:EVALuation:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:EVALuation:OFFSet \n
		Snippet: value: float = driver.applications.k149Uwb.sense.detect.evaluation.offset.get() \n
		Sets the offset of the beginning of the detected burst to where to start detection within SYNC section. \n
			:return: offset: numeric value"""
		response = self._core.io.query_str(f'SENSe:DETect:EVALuation:OFFSet?')
		return Conversions.str_to_float(response)
