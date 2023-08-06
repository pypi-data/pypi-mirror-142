from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.HardcopyMode) -> None:
		"""SCPI: HCOPy:MODE \n
		Snippet: driver.hardCopy.mode.set(mode = enums.HardcopyMode.REPort) \n
		No command help available \n
			:param mode: SCReen HCOPy:IMMediate prints the current screen contents. REPort HCOPy:IMMediate generates a measurement report.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HardcopyMode)
		self._core.io.write(f'HCOPy:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.HardcopyMode:
		"""SCPI: HCOPy:MODE \n
		Snippet: value: enums.HardcopyMode = driver.hardCopy.mode.get() \n
		No command help available \n
			:return: mode: SCReen HCOPy:IMMediate prints the current screen contents. REPort HCOPy:IMMediate generates a measurement report."""
		response = self._core.io.query_str(f'HCOPy:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.HardcopyMode)
