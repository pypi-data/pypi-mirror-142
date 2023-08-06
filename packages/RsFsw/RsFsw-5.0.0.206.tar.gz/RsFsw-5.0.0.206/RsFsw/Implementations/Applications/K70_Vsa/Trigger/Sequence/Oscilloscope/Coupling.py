from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, coupling: enums.CouplingTypeB, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:OSCilloscope:COUPling \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.oscilloscope.coupling.set(coupling = enums.CouplingTypeB.AC, triggerPort = repcap.TriggerPort.Default) \n
		Configures the coupling of the external trigger to the oscilloscope. \n
			:param coupling: Coupling type DC Direct connection with 50 Ω termination, passes both DC and AC components of the trigger signal. CDLimit Direct connection with 1 MΩ termination, passes both DC and AC components of the trigger signal. AC Connection through capacitor, removes unwanted DC and very low-frequency components.
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingTypeB)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:OSCilloscope:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.CouplingTypeB:
		"""SCPI: TRIGger<tp>[:SEQuence]:OSCilloscope:COUPling \n
		Snippet: value: enums.CouplingTypeB = driver.applications.k70Vsa.trigger.sequence.oscilloscope.coupling.get(triggerPort = repcap.TriggerPort.Default) \n
		Configures the coupling of the external trigger to the oscilloscope. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: coupling: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:OSCilloscope:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeB)
