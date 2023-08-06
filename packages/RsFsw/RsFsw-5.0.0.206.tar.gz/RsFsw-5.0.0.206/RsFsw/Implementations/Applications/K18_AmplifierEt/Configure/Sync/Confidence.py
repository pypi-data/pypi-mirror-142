from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Confidence:
	"""Confidence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	def set(self, confidence: float) -> None:
		"""SCPI: CONFigure:SYNC:CONFidence \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.confidence.set(confidence = 1.0) \n
		This command defines the synchronization confidence level. \n
			:param confidence: numeric value Range: 0 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(confidence)
		self._core.io.write(f'CONFigure:SYNC:CONFidence {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:SYNC:CONFidence \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.sync.confidence.get() \n
		This command defines the synchronization confidence level. \n
			:return: confidence: numeric value Range: 0 to 100, Unit: PCT"""
		response = self._core.io.query_str(f'CONFigure:SYNC:CONFidence?')
		return Conversions.str_to_float(response)
