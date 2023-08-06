from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfactor:
	"""Cfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfactor", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:SINFo:CFACtor \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.sinfo.cfactor.get() \n
		Returns the crest factor of the reference signal. \n
			:return: crest_factor: numeric value"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SINFo:CFACtor?')
		return Conversions.str_to_float(response)
