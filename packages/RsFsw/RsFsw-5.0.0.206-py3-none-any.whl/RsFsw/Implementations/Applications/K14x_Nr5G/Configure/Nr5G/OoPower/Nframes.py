from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nframes:
	"""Nframes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nframes", core, parent)

	def set(self, frames: float) -> None:
		"""SCPI: CONFigure[:NR5G]:OOPower:NFRames \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.ooPower.nframes.set(frames = 1.0) \n
		This command defines the number of frames to analyze in on / off power measurements. \n
			:param frames: No help available
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'CONFigure:NR5G:OOPower:NFRames {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:NR5G]:OOPower:NFRames \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.ooPower.nframes.get() \n
		This command defines the number of frames to analyze in on / off power measurements. \n
			:return: frames: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:OOPower:NFRames?')
		return Conversions.str_to_float(response)
