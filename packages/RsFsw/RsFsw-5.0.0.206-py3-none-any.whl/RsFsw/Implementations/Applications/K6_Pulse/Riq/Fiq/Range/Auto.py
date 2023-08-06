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
		"""SCPI: RIQ:FIQ:RANGe:AUTO \n
		Snippet: driver.applications.k6Pulse.riq.fiq.range.auto.set(state = False) \n
		If enabled, the data from the entire file is used as the time sidelobe range. If disabled, you can define the length and
		offset of the range manually (see method RsFsw.Applications.K6_Pulse.Riq.Fiq.Range.Length.set and method RsFsw.
		Applications.K6_Pulse.Riq.Fiq.Range.Offset.set. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'RIQ:FIQ:RANGe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: RIQ:FIQ:RANGe:AUTO \n
		Snippet: value: bool = driver.applications.k6Pulse.riq.fiq.range.auto.get() \n
		If enabled, the data from the entire file is used as the time sidelobe range. If disabled, you can define the length and
		offset of the range manually (see method RsFsw.Applications.K6_Pulse.Riq.Fiq.Range.Length.set and method RsFsw.
		Applications.K6_Pulse.Riq.Fiq.Range.Offset.set. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'RIQ:FIQ:RANGe:AUTO?')
		return Conversions.str_to_bool(response)
