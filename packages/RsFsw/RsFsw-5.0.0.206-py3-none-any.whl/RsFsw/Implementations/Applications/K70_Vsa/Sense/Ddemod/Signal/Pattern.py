from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:SIGNal:PATTern \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.signal.pattern.set(state = False) \n
		This command specifies whether the signal contains a pattern or not. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The signal does not contain a pattern. ON | 1 The signal contains a pattern.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:SIGNal:PATTern {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:SIGNal:PATTern \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.signal.pattern.get() \n
		This command specifies whether the signal contains a pattern or not. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The signal does not contain a pattern. ON | 1 The signal contains a pattern."""
		response = self._core.io.query_str(f'SENSe:DDEMod:SIGNal:PATTern?')
		return Conversions.str_to_bool(response)
