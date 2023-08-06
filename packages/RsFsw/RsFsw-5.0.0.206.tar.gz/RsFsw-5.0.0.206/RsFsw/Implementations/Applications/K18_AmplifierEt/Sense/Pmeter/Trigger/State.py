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
		"""SCPI: [SENSe]:PMETer:TRIGger[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.state.set(state = False) \n
		This command turns the external power trigger on and off. This command requires the use of a Rohde & Schwarz power sensor.
		For a list of supported sensors, see the data sheet. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:PMETer:TRIGger:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:PMETer:TRIGger[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.pmeter.trigger.state.get() \n
		This command turns the external power trigger on and off. This command requires the use of a Rohde & Schwarz power sensor.
		For a list of supported sensors, see the data sheet. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:STATe?')
		return Conversions.str_to_bool(response)
