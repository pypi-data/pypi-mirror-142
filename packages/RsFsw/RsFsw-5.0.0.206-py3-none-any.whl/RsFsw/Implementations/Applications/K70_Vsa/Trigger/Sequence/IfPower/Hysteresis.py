from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def set(self, hysteresis: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:IFPower:HYSTeresis \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.ifPower.hysteresis.set(hysteresis = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command defines the trigger hysteresis, which is only available for 'IF Power' trigger sources. \n
			:param hysteresis: Range: 3 dB to 50 dB, Unit: DB
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:IFPower:HYSTeresis {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:IFPower:HYSTeresis \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.ifPower.hysteresis.get(triggerPort = repcap.TriggerPort.Default) \n
		This command defines the trigger hysteresis, which is only available for 'IF Power' trigger sources. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: hysteresis: Range: 3 dB to 50 dB, Unit: DB"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:IFPower:HYSTeresis?')
		return Conversions.str_to_float(response)
