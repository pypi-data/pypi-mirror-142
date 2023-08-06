from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlength:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def set(self, samples: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:RLENgth \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.rlength.set(samples = 1.0) \n
		This command defines the ramp length of an internally generated pulsed reference signal. \n
			:param samples: numeric value: (integer only) Number of samples on each side of the pulse (= ramp length) . Unit: Samples
		"""
		param = Conversions.decimal_value_to_str(samples)
		self._core.io.write(f'CONFigure:REFSignal:GOS:RLENgth {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:RLENgth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.rlength.get() \n
		This command defines the ramp length of an internally generated pulsed reference signal. \n
			:return: samples: numeric value: (integer only) Number of samples on each side of the pulse (= ramp length) . Unit: Samples"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:RLENgth?')
		return Conversions.str_to_float(response)
