from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obw:
	"""Obw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("obw", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:SINFo:OBW \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.sinfo.obw.get() \n
		Returns the occupied bandwidth of the reference signal. \n
			:return: bandwidth: numeric value"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SINFo:OBW?')
		return Conversions.str_to_float(response)
