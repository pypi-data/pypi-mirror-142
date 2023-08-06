from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbPower:
	"""BbPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbPower", core, parent)

	def set(self, level_bb_power: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel:BBPower \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.level.bbPower.set(level_bb_power = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command sets the level of the baseband power trigger. This command is available for the optional Digital Baseband
		Interface and the optional Analog Baseband Interface. \n
			:param level_bb_power: Range: -50 dBm to +20 dBm, Unit: DBM
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(level_bb_power)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:BBPower {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel:BBPower \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.level.bbPower.get(triggerPort = repcap.TriggerPort.Default) \n
		This command sets the level of the baseband power trigger. This command is available for the optional Digital Baseband
		Interface and the optional Analog Baseband Interface. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: level_bb_power: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:BBPower?')
		return Conversions.str_to_float(response)
