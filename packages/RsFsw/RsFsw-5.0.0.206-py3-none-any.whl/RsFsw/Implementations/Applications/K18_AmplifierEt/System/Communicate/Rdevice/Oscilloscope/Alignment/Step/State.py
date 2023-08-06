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
		Snippet: value: bool = driver.applications.k18AmplifierEt.system.communicate.rdevice.oscilloscope.alignment.step.state.get(step = repcap.Step.Default) \n
		No command help available \n
			:param step: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Step')
			:return: alignment_step: No help available"""
		step_cmd_val = self._cmd_group.get_repcap_cmd_value(step, repcap.Step)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:ALIGnment:STEP{step_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
