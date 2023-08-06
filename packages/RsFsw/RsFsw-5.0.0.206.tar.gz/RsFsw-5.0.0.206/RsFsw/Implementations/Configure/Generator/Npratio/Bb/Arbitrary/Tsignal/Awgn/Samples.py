from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Samples:
	"""Samples commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("samples", core, parent)

	def set(self, arbn_of_samples: float) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:ARBitrary:TSIGnal:AWGN:SAMPles \n
		Snippet: driver.configure.generator.npratio.bb.arbitrary.tsignal.awgn.samples.set(arbn_of_samples = 1.0) \n
		No command help available \n
			:param arbn_of_samples: No help available
		"""
		param = Conversions.decimal_value_to_str(arbn_of_samples)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:BB:ARBitrary:TSIGnal:AWGN:SAMPles {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:ARBitrary:TSIGnal:AWGN:SAMPles \n
		Snippet: value: float = driver.configure.generator.npratio.bb.arbitrary.tsignal.awgn.samples.get() \n
		No command help available \n
			:return: arbn_of_samples: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:BB:ARBitrary:TSIGnal:AWGN:SAMPles?')
		return Conversions.str_to_float(response)
