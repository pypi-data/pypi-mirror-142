from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def set(self, sub_frames: float) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:SCOunt \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.scount.set(sub_frames = 1.0) \n
		No command help available \n
			:param sub_frames: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_frames)
		self._core.io.write(f'SENSe:NR5G:FRAMe:SCOunt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:FRAMe:SCOunt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.frame.scount.get() \n
		No command help available \n
			:return: sub_frames: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:SCOunt?')
		return Conversions.str_to_float(response)
