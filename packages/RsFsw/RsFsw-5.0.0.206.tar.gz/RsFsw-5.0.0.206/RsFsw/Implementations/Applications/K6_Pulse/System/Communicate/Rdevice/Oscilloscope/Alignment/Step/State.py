from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, step=repcap.Step.Default) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:STEP<st>[:STATe] \n
		Snippet: value: bool = driver.applications.k6Pulse.system.communicate.rdevice.oscilloscope.alignment.step.state.get(step = repcap.Step.Default) \n
		Performs the alignment of the oscilloscope itself and the oscilloscope ADC for the optional 2 GHz / 5 GHz bandwidth
		extension (R&S FSW-B2000/B5000) . The correction data for the oscilloscope (including the connection cable between the
		R&S FSW and the oscilloscope) is recorded. As a result, the state of the alignment is returned. Alignment is required
		only once after setup. If alignment was performed successfully, the alignment data is stored on the oscilloscope.
			INTRO_CMD_HELP: Thus, alignment need only be repeated if one of the following applies: \n
			- A new oscilloscope is connected to the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector of the R&S FSW
			- A new cable is used between the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector of the R&S FSW and the oscilloscope
			- A power splitter is inserted between the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector of the R&S FSW and the oscilloscope
			- New firmware is installed on the oscilloscope or the R&S FSW
		For details see 'Alignment'. \n
			:param step: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Step')
			:return: state: Returns the state of the second alignment step. ON | 1 Alignment was successful. OFF | 0 Alignment was not yet performed (successfully) ."""
		step_cmd_val = self._cmd_group.get_repcap_cmd_value(step, repcap.Step)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:STEP{step_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
