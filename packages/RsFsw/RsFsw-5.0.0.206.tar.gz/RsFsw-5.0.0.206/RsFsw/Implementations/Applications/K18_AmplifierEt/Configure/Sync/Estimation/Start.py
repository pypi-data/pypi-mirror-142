from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, start: float) -> None:
		"""SCPI: CONFigure:SYNC:ESTimation:STARt \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.estimation.start.set(start = 1.0) \n
		No command help available \n
			:param start: No help available
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'CONFigure:SYNC:ESTimation:STARt {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:SYNC:ESTimation:STARt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.sync.estimation.start.get() \n
		No command help available \n
			:return: start: No help available"""
		response = self._core.io.query_str(f'CONFigure:SYNC:ESTimation:STARt?')
		return Conversions.str_to_float(response)
