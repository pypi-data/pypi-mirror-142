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
		"""SCPI: CONFigure[:LTE]:OOPower:NFRames \n
		Snippet: driver.applications.k10Xlte.configure.lte.ooPower.nframes.set(frames = 1.0) \n
		This command defines the number of frames that are analyzed for On/Off Power measurements. \n
			:param frames: numeric value
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'CONFigure:LTE:OOPower:NFRames {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:OOPower:NFRames \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.ooPower.nframes.get() \n
		This command defines the number of frames that are analyzed for On/Off Power measurements. \n
			:return: frames: numeric value"""
		response = self._core.io.query_str(f'CONFigure:LTE:OOPower:NFRames?')
		return Conversions.str_to_float(response)
