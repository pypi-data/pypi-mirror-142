from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimization:
	"""Optimization commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimization", core, parent)

	def set(self, state: enums.FrameOptimize) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:OPTimization \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.optimization.set(state = enums.FrameOptimize.DYNamic) \n
		This command selects the data capture method for combined measurements. \n
			:param state: DYNamic Separate capture of carrier and neighboring channels. SPEed Capture all channels in one take.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.FrameOptimize)
		self._core.io.write(f'SENSe:NR5G:FRAMe:OPTimization {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrameOptimize:
		"""SCPI: [SENSe]:NR5G:FRAMe:OPTimization \n
		Snippet: value: enums.FrameOptimize = driver.applications.k14Xnr5G.sense.nr5G.frame.optimization.get() \n
		This command selects the data capture method for combined measurements. \n
			:return: state: DYNamic Separate capture of carrier and neighboring channels. SPEed Capture all channels in one take."""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:OPTimization?')
		return Conversions.str_to_scalar_enum(response, enums.FrameOptimize)
