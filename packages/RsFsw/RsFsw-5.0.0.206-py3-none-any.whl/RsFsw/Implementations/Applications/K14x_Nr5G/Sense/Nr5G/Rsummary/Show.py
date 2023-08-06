from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Show:
	"""Show commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("show", core, parent)

	def set(self, result: enums.SummaryMode) -> None:
		"""SCPI: [SENSe]:NR5G:RSUMmary:SHOW \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.rsummary.show.set(result = enums.SummaryMode.AVERage) \n
		This command selects the way the contents of the result summary are calculated. \n
			:param result: AVERage Shows the average over all analyzed frames. SINGle Shows the result for the frame selected with [SENSe:]NR5G[:CCcc]:FRAMe:SELect. If only one frame has been captured, the results are the same in both cases.
		"""
		param = Conversions.enum_scalar_to_str(result, enums.SummaryMode)
		self._core.io.write(f'SENSe:NR5G:RSUMmary:SHOW {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SummaryMode:
		"""SCPI: [SENSe]:NR5G:RSUMmary:SHOW \n
		Snippet: value: enums.SummaryMode = driver.applications.k14Xnr5G.sense.nr5G.rsummary.show.get() \n
		This command selects the way the contents of the result summary are calculated. \n
			:return: result: AVERage Shows the average over all analyzed frames. SINGle Shows the result for the frame selected with [SENSe:]NR5G[:CCcc]:FRAMe:SELect. If only one frame has been captured, the results are the same in both cases."""
		response = self._core.io.query_str(f'SENSe:NR5G:RSUMmary:SHOW?')
		return Conversions.str_to_scalar_enum(response, enums.SummaryMode)
