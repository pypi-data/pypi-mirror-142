from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slength:
	"""Slength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slength", core, parent)

	def set(self, samples: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:SLENgth \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.slength.set(samples = 1.0) \n
		This command defines the length of the internally generated reference signal. \n
			:param samples: numeric value: (integer only) Unit: Samples
		"""
		param = Conversions.decimal_value_to_str(samples)
		self._core.io.write(f'CONFigure:REFSignal:GOS:SLENgth {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:SLENgth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.slength.get() \n
		This command defines the length of the internally generated reference signal. \n
			:return: samples: numeric value: (integer only) Unit: Samples"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:SLENgth?')
		return Conversions.str_to_float(response)
