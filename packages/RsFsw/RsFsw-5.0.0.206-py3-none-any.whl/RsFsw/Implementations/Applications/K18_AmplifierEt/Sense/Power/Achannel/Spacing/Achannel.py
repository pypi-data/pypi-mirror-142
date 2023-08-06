from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:ACHannel \n
		Snippet: driver.applications.k18AmplifierEt.sense.power.achannel.spacing.achannel.set(bandwidth = 1.0) \n
		This command defines the distance from transmission channel to adjacent channel. A change of the adjacent channel spacing
		causes a change in the spacing of all alternate channels below the adjacent channel. \n
			:param bandwidth: Range: 100 Hz to 2000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:ACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:ACHannel \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.power.achannel.spacing.achannel.get() \n
		This command defines the distance from transmission channel to adjacent channel. A change of the adjacent channel spacing
		causes a change in the spacing of all alternate channels below the adjacent channel. \n
			:return: bandwidth: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:ACHannel?')
		return Conversions.str_to_float(response)
