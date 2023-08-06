from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:TIME:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.time.auto.set(state = False) \n
		Determines how the result length is defined for multi-modulation analysis. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The result length is specified by [SENSe:]DDEMod:TIME. ON | 1 The result length is set to the number defined in the currently loaded Frame Structure file.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:TIME:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:TIME:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.time.auto.get() \n
		Determines how the result length is defined for multi-modulation analysis. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The result length is specified by [SENSe:]DDEMod:TIME. ON | 1 The result length is set to the number defined in the currently loaded Frame Structure file."""
		response = self._core.io.query_str(f'SENSe:DDEMod:TIME:AUTO?')
		return Conversions.str_to_bool(response)
