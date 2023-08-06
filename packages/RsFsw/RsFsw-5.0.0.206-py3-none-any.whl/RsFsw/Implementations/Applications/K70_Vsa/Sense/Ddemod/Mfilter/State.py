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
		"""SCPI: [SENSe]:DDEMod:MFILter[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.mfilter.state.set(state = False) \n
		Use this command to switch the measurement filter off. To switch a measurement filter on,
		use the [SENSe:]DDEMod:MFILter:NAME command. \n
			:param state: OFF | 0 Switches the measurement filter off. ON | 1 Switches the measurement filter specified by [SENSe:]DDEMod:MFILter:NAME on. However, this command is not necessary, as the [SENSe:]DDEMod:MFILter:NAME command automatically switches the selected filter on.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:MFILter:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:MFILter[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.mfilter.state.get() \n
		Use this command to switch the measurement filter off. To switch a measurement filter on,
		use the [SENSe:]DDEMod:MFILter:NAME command. \n
			:return: state: OFF | 0 Switches the measurement filter off. ON | 1 Switches the measurement filter specified by [SENSe:]DDEMod:MFILter:NAME on. However, this command is not necessary, as the [SENSe:]DDEMod:MFILter:NAME command automatically switches the selected filter on."""
		response = self._core.io.query_str(f'SENSe:DDEMod:MFILter:STATe?')
		return Conversions.str_to_bool(response)
