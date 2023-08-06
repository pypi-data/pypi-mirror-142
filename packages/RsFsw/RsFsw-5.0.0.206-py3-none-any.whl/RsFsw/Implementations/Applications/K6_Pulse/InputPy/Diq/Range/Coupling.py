from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:DIQ:RANGe:COUPling \n
		Snippet: driver.applications.k6Pulse.inputPy.diq.range.coupling.set(state = False) \n
		If enabled, the reference level for digital input is adjusted to the full scale level automatically if the full scale
		level changes. This command is only available if the optional Digital Baseband Interface is installed. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:DIQ:RANGe:COUPling {param}')

	def get(self) -> bool:
		"""SCPI: INPut:DIQ:RANGe:COUPling \n
		Snippet: value: bool = driver.applications.k6Pulse.inputPy.diq.range.coupling.get() \n
		If enabled, the reference level for digital input is adjusted to the full scale level automatically if the full scale
		level changes. This command is only available if the optional Digital Baseband Interface is installed. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'INPut:DIQ:RANGe:COUPling?')
		return Conversions.str_to_bool(response)
