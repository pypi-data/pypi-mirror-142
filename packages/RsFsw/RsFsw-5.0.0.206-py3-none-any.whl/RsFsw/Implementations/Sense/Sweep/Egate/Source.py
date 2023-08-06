from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.TriggerSourceD) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: driver.sense.sweep.egate.source.set(source = enums.TriggerSourceD.EXT2) \n
		This command selects the signal source for gated measurements. If an IF power signal is used, the gate is opened as soon
		as a signal at > -20 dBm is detected within the IF path bandwidth (10 MHz) . For more information see 'Trigger Source'.
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- 'External Trigger 1/2/3'
			- 'Power Sensor'
		For details see 'Triggered gated measurements' \n
			:param source: EXTernal | EXT2 | EXT3 | IFPower | IQPower | VIDeo | RFPower | PSEN
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceD)
		self._core.io.write(f'SENSe:SWEep:EGATe:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerSourceD:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: value: enums.TriggerSourceD = driver.sense.sweep.egate.source.get() \n
		This command selects the signal source for gated measurements. If an IF power signal is used, the gate is opened as soon
		as a signal at > -20 dBm is detected within the IF path bandwidth (10 MHz) . For more information see 'Trigger Source'.
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- 'External Trigger 1/2/3'
			- 'Power Sensor'
		For details see 'Triggered gated measurements' \n
			:return: source: EXTernal | EXT2 | EXT3 | IFPower | IQPower | VIDeo | RFPower | PSEN"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceD)
