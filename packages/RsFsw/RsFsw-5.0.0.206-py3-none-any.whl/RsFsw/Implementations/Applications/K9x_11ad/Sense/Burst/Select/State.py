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
		"""SCPI: [SENSe]:BURSt:SELect:STATe \n
		Snippet: driver.applications.k9X11Ad.sense.burst.select.state.set(state = False) \n
		Defines the evaluation basis for result displays. Note that this setting is only applicable after a measurement has been
		performed. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 All detected PPDUs in the current capture buffer are evaluated. ON | 1 The IEEE 802.11ad I/Q results are based on one individual PPDU only, namely the defined using [SENSe:]BURSt:SELect. As soon as a new measurement is started, the evaluation range is reset to all PPDUs in the current capture buffer.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:BURSt:SELect:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:BURSt:SELect:STATe \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.burst.select.state.get() \n
		Defines the evaluation basis for result displays. Note that this setting is only applicable after a measurement has been
		performed. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 All detected PPDUs in the current capture buffer are evaluated. ON | 1 The IEEE 802.11ad I/Q results are based on one individual PPDU only, namely the defined using [SENSe:]BURSt:SELect. As soon as a new measurement is started, the evaluation range is reset to all PPDUs in the current capture buffer."""
		response = self._core.io.query_str(f'SENSe:BURSt:SELect:STATe?')
		return Conversions.str_to_bool(response)
