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
		"""SCPI: [SENSe]:DDEMod:EQUalizer[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.state.set(state = False) \n
		This command activates or deactivates the equalizer. For more information on the equalizer see 'The equalizer'. \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:EQUalizer[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.equalizer.state.get() \n
		This command activates or deactivates the equalizer. For more information on the equalizer see 'The equalizer'. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:STATe?')
		return Conversions.str_to_bool(response)
