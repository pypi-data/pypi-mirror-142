from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def set(self, event: float) -> None:
		"""SCPI: [SENSe]:SWEep:EVENt \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.event.set(event = 1.0) \n
		This command defines the number of events in a combined measurement sequence. \n
			:param event: No help available
		"""
		param = Conversions.decimal_value_to_str(event)
		self._core.io.write(f'SENSe:SWEep:EVENt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EVENt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.event.get() \n
		This command defines the number of events in a combined measurement sequence. \n
			:return: event: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EVENt?')
		return Conversions.str_to_float(response)
