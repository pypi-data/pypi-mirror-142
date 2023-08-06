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
		"""SCPI: [SENSe][:LTE]:FRAMe:SCOunt \n
		Snippet: driver.applications.k10Xlte.sense.lte.frame.scount.set(sub_frames = 1.0) \n
		This command selects the maximum number of subframes to analyze. Selecting a number of subframes different from the
		default one may become necessary if the capture time is less than 20.1 ms. \n
			:param sub_frames: ALL Analyzes all subframes of a frame (10) . numeric value (integer only) Number of subframes that the application analyzes. Range: 1 to 9
		"""
		param = Conversions.decimal_value_to_str(sub_frames)
		self._core.io.write(f'SENSe:LTE:FRAMe:SCOunt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe][:LTE]:FRAMe:SCOunt \n
		Snippet: value: float = driver.applications.k10Xlte.sense.lte.frame.scount.get() \n
		This command selects the maximum number of subframes to analyze. Selecting a number of subframes different from the
		default one may become necessary if the capture time is less than 20.1 ms. \n
			:return: sub_frames: ALL Analyzes all subframes of a frame (10) . numeric value (integer only) Number of subframes that the application analyzes. Range: 1 to 9"""
		response = self._core.io.query_str(f'SENSe:LTE:FRAMe:SCOunt?')
		return Conversions.str_to_float(response)
