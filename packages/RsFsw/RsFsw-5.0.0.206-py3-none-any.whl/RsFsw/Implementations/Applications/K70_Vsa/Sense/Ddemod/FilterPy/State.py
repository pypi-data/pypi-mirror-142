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
		"""SCPI: [SENSe]:DDEMod:FILTer[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.filterPy.state.set(state = False) \n
		This command defines whether the input signal that is evaluated is filtered by the measurement filter. This command has
		no effect on the transmit filter. \n
			:param state: ON | 1 [SENSe:]DDEMod:MFILter:AUTO is activated. OFF | 0 The input signal is not filtered. [SENSe:]DDEMod:MFILter:AUTO is deactivated.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:FILTer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:FILTer[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.filterPy.state.get() \n
		This command defines whether the input signal that is evaluated is filtered by the measurement filter. This command has
		no effect on the transmit filter. \n
			:return: state: ON | 1 [SENSe:]DDEMod:MFILter:AUTO is activated. OFF | 0 The input signal is not filtered. [SENSe:]DDEMod:MFILter:AUTO is deactivated."""
		response = self._core.io.query_str(f'SENSe:DDEMod:FILTer:STATe?')
		return Conversions.str_to_bool(response)
