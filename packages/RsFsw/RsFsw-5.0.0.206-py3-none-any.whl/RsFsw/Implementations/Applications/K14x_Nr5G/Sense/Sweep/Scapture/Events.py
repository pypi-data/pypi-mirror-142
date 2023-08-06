from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Events:
	"""Events commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("events", core, parent)

	def set(self, events: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.scapture.events.set(events = 1.0) \n
		This command defines the number of segments to capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) .
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:param events: No help available
		"""
		param = Conversions.decimal_value_to_str(events)
		self._core.io.write(f'SENSe:SWEep:SCAPture:EVENts {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.scapture.events.get() \n
		This command defines the number of segments to capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) .
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:return: events: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:EVENts?')
		return Conversions.str_to_float(response)
