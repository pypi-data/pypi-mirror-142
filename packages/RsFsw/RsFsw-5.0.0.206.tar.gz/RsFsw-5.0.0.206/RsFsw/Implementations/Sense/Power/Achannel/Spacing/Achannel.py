from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, spacing: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing[:ACHannel] \n
		Snippet: driver.sense.power.achannel.spacing.achannel.set(spacing = 1.0) \n
		This command defines the distance from transmission channel to adjacent channel. For MSR signals, this command defines
		the distance from the CF of the first Tx channel in the first sub block to the lower adjacent channel. To configure the
		spacing for the upper adjacent channel in asymmetrical configurations, use the [SENSe:]POWer:ACHannel:SPACing:UACHannel
		command. A change of the adjacent channel spacing causes a change in the spacing of all alternate channels below the
		adjacent channel (not for MSR signals) . \n
			:param spacing: Range: 100 Hz to 2000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:ACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing[:ACHannel] \n
		Snippet: value: float = driver.sense.power.achannel.spacing.achannel.get() \n
		This command defines the distance from transmission channel to adjacent channel. For MSR signals, this command defines
		the distance from the CF of the first Tx channel in the first sub block to the lower adjacent channel. To configure the
		spacing for the upper adjacent channel in asymmetrical configurations, use the [SENSe:]POWer:ACHannel:SPACing:UACHannel
		command. A change of the adjacent channel spacing causes a change in the spacing of all alternate channels below the
		adjacent channel (not for MSR signals) . \n
			:return: spacing: Range: 100 Hz to 2000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:ACHannel?')
		return Conversions.str_to_float(response)
