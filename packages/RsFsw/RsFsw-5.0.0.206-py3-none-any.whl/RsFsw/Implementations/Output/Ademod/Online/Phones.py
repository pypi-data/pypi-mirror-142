from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phones:
	"""Phones commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phones", core, parent)

	def set(self, state: bool, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:PHONes \n
		Snippet: driver.output.ademod.online.phones.set(state = False, outputConnector = repcap.OutputConnector.Default) \n
		In addition to sending the output to the IF/VIDEO/DEMOD output connector (on the rear panel of the R&S FSW) , it can also
		be output to headphones connected on the front panel ([Phones] connector) . CAUTION: To protect your hearing, make sure
		that the volume setting is not too high before putting on the headphones. If you do not hear output on the connected
		headphones despite having enabled both general online demod output method RsFsw.Output.Ademod.Online.State.set and this
		command, adjust the volume setting. (Using method RsFsw.System.Speaker.Volume.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(state)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:PHONes {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> bool:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:PHONes \n
		Snippet: value: bool = driver.output.ademod.online.phones.get(outputConnector = repcap.OutputConnector.Default) \n
		In addition to sending the output to the IF/VIDEO/DEMOD output connector (on the rear panel of the R&S FSW) , it can also
		be output to headphones connected on the front panel ([Phones] connector) . CAUTION: To protect your hearing, make sure
		that the volume setting is not too high before putting on the headphones. If you do not hear output on the connected
		headphones despite having enabled both general online demod output method RsFsw.Output.Ademod.Online.State.set and this
		command, adjust the volume setting. (Using method RsFsw.System.Speaker.Volume.set. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:PHONes?')
		return Conversions.str_to_bool(response)
