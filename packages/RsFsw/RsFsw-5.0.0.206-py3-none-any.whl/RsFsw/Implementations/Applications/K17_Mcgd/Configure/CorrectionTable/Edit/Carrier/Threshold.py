from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, selected_carrier_threshold: float) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:THReshold \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.threshold.set(selected_carrier_threshold = 1.0) \n
		Sets the threshold of the selected carriers in the configuration assistant. \n
			:param selected_carrier_threshold: numeric value Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(selected_carrier_threshold)
		self._core.io.write(f'CONFigure:CTABle:EDIT:CARRier:THReshold {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:THReshold \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.threshold.get() \n
		Sets the threshold of the selected carriers in the configuration assistant. \n
			:return: selected_carrier_threshold: numeric value Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:CTABle:EDIT:CARRier:THReshold?')
		return Conversions.str_to_float(response)
