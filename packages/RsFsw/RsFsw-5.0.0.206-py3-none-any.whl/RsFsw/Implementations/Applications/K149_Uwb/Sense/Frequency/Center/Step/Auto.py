from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, link_mode: bool) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:AUTO \n
		Snippet: driver.applications.k149Uwb.sense.frequency.center.step.auto.set(link_mode = False) \n
		This command couples or decouples the center frequency step size to the span. \n
			:param link_mode: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(link_mode)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:AUTO \n
		Snippet: value: bool = driver.applications.k149Uwb.sense.frequency.center.step.auto.get() \n
		This command couples or decouples the center frequency step size to the span. \n
			:return: link_mode: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP:AUTO?')
		return Conversions.str_to_bool(response)
