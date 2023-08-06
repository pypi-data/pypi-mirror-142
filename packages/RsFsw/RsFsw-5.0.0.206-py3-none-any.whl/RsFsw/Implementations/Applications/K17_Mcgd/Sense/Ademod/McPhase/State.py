from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADEMod:MCPHase[:STATe] \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.mcPhase.state.set(state = False) \n
		This command switches to the Multi-Carrier Group Delay application of the instrument or disables it. Note that this
		command is maintained for compatibility reasons only. Use the INST:SEL MCGD command for new remote control programs (see
		method RsFsw.Instrument.Select.set) . \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:MCPHase:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod:MCPHase[:STATe] \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.ademod.mcPhase.state.get() \n
		This command switches to the Multi-Carrier Group Delay application of the instrument or disables it. Note that this
		command is maintained for compatibility reasons only. Use the INST:SEL MCGD command for new remote control programs (see
		method RsFsw.Instrument.Select.set) . \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MCPHase:STATe?')
		return Conversions.str_to_bool(response)
