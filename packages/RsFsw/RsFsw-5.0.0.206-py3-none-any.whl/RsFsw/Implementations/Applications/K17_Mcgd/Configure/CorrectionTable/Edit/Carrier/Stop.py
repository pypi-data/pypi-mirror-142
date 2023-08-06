from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, assistant_stop: float) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STOP \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.stop.set(assistant_stop = 1.0) \n
		Sets the last selected carrier in the configuration assistant. \n
			:param assistant_stop: Carrier position
		"""
		param = Conversions.decimal_value_to_str(assistant_stop)
		self._core.io.write(f'CONFigure:CTABle:EDIT:CARRier:STOP {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STOP \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.stop.get() \n
		Sets the last selected carrier in the configuration assistant. \n
			:return: assistant_stop: Carrier position"""
		response = self._core.io.query_str(f'CONFigure:CTABle:EDIT:CARRier:STOP?')
		return Conversions.str_to_float(response)
