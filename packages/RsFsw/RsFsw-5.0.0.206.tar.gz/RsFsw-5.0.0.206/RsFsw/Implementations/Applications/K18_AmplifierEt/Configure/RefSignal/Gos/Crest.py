from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crest:
	"""Crest commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crest", core, parent)

	def set(self, crest_factor: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:CRESt \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.crest.set(crest_factor = 1.0) \n
		This command defines the crest factor of the internally generated reference signal. \n
			:param crest_factor: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(crest_factor)
		self._core.io.write(f'CONFigure:REFSignal:GOS:CRESt {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:CRESt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.crest.get() \n
		This command defines the crest factor of the internally generated reference signal. \n
			:return: crest_factor: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:CRESt?')
		return Conversions.str_to_float(response)
