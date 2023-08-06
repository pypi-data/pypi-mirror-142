from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, assistant_start: float) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STARt \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.start.set(assistant_start = 1.0) \n
		Sets the first selected carrier in the configuration assistant. \n
			:param assistant_start: Carrier position
		"""
		param = Conversions.decimal_value_to_str(assistant_start)
		self._core.io.write(f'CONFigure:CTABle:EDIT:CARRier:STARt {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STARt \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.start.get() \n
		Sets the first selected carrier in the configuration assistant. \n
			:return: assistant_start: Carrier position"""
		response = self._core.io.query_str(f'CONFigure:CTABle:EDIT:CARRier:STARt?')
		return Conversions.str_to_float(response)
