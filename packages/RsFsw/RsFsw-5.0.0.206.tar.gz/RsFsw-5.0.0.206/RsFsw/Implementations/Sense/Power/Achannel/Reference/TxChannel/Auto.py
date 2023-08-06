from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, ref_channel: enums.RefChannel) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:TXCHannel:AUTO \n
		Snippet: driver.sense.power.achannel.reference.txChannel.auto.set(ref_channel = enums.RefChannel.LHIGhest) \n
		This command selects the reference channel for relative measurements. You need at least one channel for the command to
		work. \n
			:param ref_channel: MINimum | MAXimum | LHIGhest MINimum Transmission channel with the lowest power MAXimum Transmission channel with the highest power LHIGhest Lowest transmission channel for lower adjacent channels and highest transmission channel for upper adjacent channels
		"""
		param = Conversions.enum_scalar_to_str(ref_channel, enums.RefChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:REFerence:TXCHannel:AUTO {param}')
