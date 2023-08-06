from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADEMod[:STATe] \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.state.set(state = False) \n
		This command switches to the Analog Demodulation application or disables it. Note that this command is maintained for
		compatibility reasons only. Use the INST:SEL ADEM command for new remote control programs. \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod[:STATe] \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.ademod.state.get() \n
		This command switches to the Analog Demodulation application or disables it. Note that this command is maintained for
		compatibility reasons only. Use the INST:SEL ADEM command for new remote control programs. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:STATe?')
		return Conversions.str_to_bool(response)
