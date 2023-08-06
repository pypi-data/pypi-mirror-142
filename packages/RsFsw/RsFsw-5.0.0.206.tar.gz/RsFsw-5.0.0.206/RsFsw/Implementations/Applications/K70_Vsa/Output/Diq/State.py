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

	def set(self, state: bool, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:DIQ[:STATe] \n
		Snippet: driver.applications.k70Vsa.output.diq.state.set(state = False, outputConnector = repcap.OutputConnector.Default) \n
		This command turns continuous output of I/Q data to the optional Digital Baseband Interface on and off. Using the digital
		input and digital output simultaneously is not possible. If digital baseband output is active, the sample rate is
		restricted to 100 MHz (200 MHz if enhanced mode is possible; max. 160 MHz bandwidth) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(state)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:DIQ:STATe {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> bool:
		"""SCPI: OUTPut<up>:DIQ[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.output.diq.state.get(outputConnector = repcap.OutputConnector.Default) \n
		This command turns continuous output of I/Q data to the optional Digital Baseband Interface on and off. Using the digital
		input and digital output simultaneously is not possible. If digital baseband output is active, the sample rate is
		restricted to 100 MHz (200 MHz if enhanced mode is possible; max. 160 MHz bandwidth) . \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:DIQ:STATe?')
		return Conversions.str_to_bool(response)
