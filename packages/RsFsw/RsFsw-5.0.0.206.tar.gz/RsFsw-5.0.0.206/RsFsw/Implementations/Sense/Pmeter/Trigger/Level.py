from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:LEVel \n
		Snippet: driver.sense.pmeter.trigger.level.set(level = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		This command defines the trigger level for external power triggers. This command requires the use of a Rohde & Schwarz
		power sensor. For a list of supported sensors see the datasheet. \n
			:param level: -20 to +20 dBm Range: -20 dBm to 20 dBm, Unit: DBM
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(level)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:LEVel {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:LEVel \n
		Snippet: value: float = driver.sense.pmeter.trigger.level.get(powerMeter = repcap.PowerMeter.Default) \n
		This command defines the trigger level for external power triggers. This command requires the use of a Rohde & Schwarz
		power sensor. For a list of supported sensors see the datasheet. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: level: -20 to +20 dBm Range: -20 dBm to 20 dBm, Unit: DBM"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:LEVel?')
		return Conversions.str_to_float(response)
