from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaChannel:
	"""UaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaChannel", core, parent)

	def set(self, spacing: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:UACHannel \n
		Snippet: driver.sense.power.achannel.spacing.uaChannel.set(spacing = 1.0) \n
		This command defines the distance from the transmission channel to the upper adjacent channel. For MSR signals, this
		command defines the distance from the CF of the last Tx channel in the last sub block to the upper adjacent channel in
		asymmetrical configurations. To configure the spacing for the lower adjacent channel use the
		[SENSe:]POWer:ACHannel:SPACing[:ACHannel] command. \n
			:param spacing: Range: 100 Hz to 2000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:UACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:UACHannel \n
		Snippet: value: float = driver.sense.power.achannel.spacing.uaChannel.get() \n
		This command defines the distance from the transmission channel to the upper adjacent channel. For MSR signals, this
		command defines the distance from the CF of the last Tx channel in the last sub block to the upper adjacent channel in
		asymmetrical configurations. To configure the spacing for the lower adjacent channel use the
		[SENSe:]POWer:ACHannel:SPACing[:ACHannel] command. \n
			:return: spacing: Range: 100 Hz to 2000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:UACHannel?')
		return Conversions.str_to_float(response)
