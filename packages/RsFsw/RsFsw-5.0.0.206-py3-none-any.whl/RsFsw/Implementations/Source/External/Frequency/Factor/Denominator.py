from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Denominator:
	"""Denominator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("denominator", core, parent)

	def set(self, value: float, externalGen=repcap.ExternalGen.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency[:FACTor]:DENominator \n
		Snippet: driver.source.external.frequency.factor.denominator.set(value = 1.0, externalGen = repcap.ExternalGen.Nr1) \n
		This command defines the denominator of the factor with which the analyzer frequency is multiplied in order to obtain the
		transmit frequency of the selected generator. This command is only valid if External Generator Control (R&S FSW-B10) is
		installed and active. Select the multiplication factor such that the frequency range of the generator is not exceeded if
		the following formula is applied to the start and stop frequency of the analyzer: \n
			:param value: numeric value
			:param externalGen: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(value)
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		self._core.io.write(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency:FACTor:DENominator {param}')

	def get(self, externalGen=repcap.ExternalGen.Nr1) -> float:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency[:FACTor]:DENominator \n
		Snippet: value: float = driver.source.external.frequency.factor.denominator.get(externalGen = repcap.ExternalGen.Nr1) \n
		This command defines the denominator of the factor with which the analyzer frequency is multiplied in order to obtain the
		transmit frequency of the selected generator. This command is only valid if External Generator Control (R&S FSW-B10) is
		installed and active. Select the multiplication factor such that the frequency range of the generator is not exceeded if
		the following formula is applied to the start and stop frequency of the analyzer: \n
			:param externalGen: optional repeated capability selector. Default value: Nr1
			:return: value: numeric value"""
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency:FACTor:DENominator?')
		return Conversions.str_to_float(response)
