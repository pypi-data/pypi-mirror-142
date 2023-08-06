from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:UPPer \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.configure.hysteresis.upper.set(threshold = 1.0) \n
		No command help available \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:UPPer \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.adjust.configure.hysteresis.upper.get() \n
		No command help available \n
			:return: threshold: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer?')
		return Conversions.str_to_float(response)
