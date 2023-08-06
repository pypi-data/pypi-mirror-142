from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:BWIDth \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.bandwidth.set(bandwidth = 1.0) \n
		This command defines the bandwidth of the internally generated reference signal. \n
			:param bandwidth: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'CONFigure:REFSignal:GOS:BWIDth {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:BWIDth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.bandwidth.get() \n
		This command defines the bandwidth of the internally generated reference signal. \n
			:return: bandwidth: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:BWIDth?')
		return Conversions.str_to_float(response)
