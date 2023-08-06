from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, if_power_holdoff: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:BBPower:HOLDoff \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.bbPower.holdoff.set(if_power_holdoff = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command defines the holding time before the baseband power trigger event. The command requires the optional Digital
		Baseband Interface or the optional Analog Baseband Interface. Note that this command is maintained for compatibility
		reasons only. Use the method RsFsw.Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote
		control programs. \n
			:param if_power_holdoff: Range: 150 ns to 1000 s, Unit: S
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(if_power_holdoff)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:BBPower:HOLDoff {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:BBPower:HOLDoff \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.bbPower.holdoff.get(triggerPort = repcap.TriggerPort.Default) \n
		This command defines the holding time before the baseband power trigger event. The command requires the optional Digital
		Baseband Interface or the optional Analog Baseband Interface. Note that this command is maintained for compatibility
		reasons only. Use the method RsFsw.Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote
		control programs. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: if_power_holdoff: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:BBPower:HOLDoff?')
		return Conversions.str_to_float(response)
