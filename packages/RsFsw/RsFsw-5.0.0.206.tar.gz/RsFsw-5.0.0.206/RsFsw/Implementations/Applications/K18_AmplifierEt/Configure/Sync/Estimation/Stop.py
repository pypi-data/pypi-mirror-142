from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, stop: float) -> None:
		"""SCPI: CONFigure:SYNC:ESTimation:STOP \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.estimation.stop.set(stop = 1.0) \n
		No command help available \n
			:param stop: No help available
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'CONFigure:SYNC:ESTimation:STOP {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:SYNC:ESTimation:STOP \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.sync.estimation.stop.get() \n
		No command help available \n
			:return: stop: No help available"""
		response = self._core.io.query_str(f'CONFigure:SYNC:ESTimation:STOP?')
		return Conversions.str_to_float(response)
