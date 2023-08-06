from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slength:
	"""Slength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slength", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:SINFo:SLENgth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.sinfo.slength.get() \n
		This command queries the sample length of the currently used reference signal. \n
			:return: samples: numeric value: (integer only) Unit: Samples"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SINFo:SLENgth?')
		return Conversions.str_to_float(response)
