from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factor:
	"""Factor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factor", core, parent)

	def set(self, link_factor: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: driver.applications.k17Mcgd.sense.frequency.center.step.link.factor.set(link_factor = 1.0) \n
		This command defines a step size factor if the center frequency step size is coupled to the span. \n
			:param link_factor: 1 to 100 PCT Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(link_factor)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:LINK:FACTor {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.frequency.center.step.link.factor.get() \n
		This command defines a step size factor if the center frequency step size is coupled to the span. \n
			:return: link_factor: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP:LINK:FACTor?')
		return Conversions.str_to_float(response)
