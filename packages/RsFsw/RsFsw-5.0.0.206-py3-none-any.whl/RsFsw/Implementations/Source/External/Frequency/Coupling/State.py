from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, externalGen=repcap.ExternalGen.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency:COUPling[:STATe] \n
		Snippet: driver.source.external.frequency.coupling.state.set(state = False, externalGen = repcap.ExternalGen.Nr1) \n
		This command couples the frequency of the external generator output to the R&S FSW. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. \n
			:param state: ON | OFF | 0 | 1 ON | 1 Default setting: a series of frequencies is defined (one for each sweep point) , based on the current frequency at the RF input of the R&S FSW; the RF frequency range covers the currently defined span of the R&S FSW (unless limited by the range of the signal generator) OFF | 0 The generator uses a single fixed frequency, defined by method RsFsw.Source.External.Frequency.set.
			:param externalGen: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.bool_to_str(state)
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		self._core.io.write(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency:COUPling:STATe {param}')

	def get(self, externalGen=repcap.ExternalGen.Nr1) -> bool:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency:COUPling[:STATe] \n
		Snippet: value: bool = driver.source.external.frequency.coupling.state.get(externalGen = repcap.ExternalGen.Nr1) \n
		This command couples the frequency of the external generator output to the R&S FSW. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. \n
			:param externalGen: optional repeated capability selector. Default value: Nr1
			:return: state: ON | OFF | 0 | 1 ON | 1 Default setting: a series of frequencies is defined (one for each sweep point) , based on the current frequency at the RF input of the R&S FSW; the RF frequency range covers the currently defined span of the R&S FSW (unless limited by the range of the signal generator) OFF | 0 The generator uses a single fixed frequency, defined by method RsFsw.Source.External.Frequency.set."""
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency:COUPling:STATe?')
		return Conversions.str_to_bool(response)
