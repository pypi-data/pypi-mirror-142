from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factor:
	"""Factor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factor", core, parent)

	def set(self, factor: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: driver.applications.k10Xlte.sense.frequency.center.step.link.factor.set(factor = 1.0) \n
		No command help available \n
			:param factor: No help available
		"""
		param = Conversions.decimal_value_to_str(factor)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:LINK:FACTor {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: value: float = driver.applications.k10Xlte.sense.frequency.center.step.link.factor.get() \n
		No command help available \n
			:return: factor: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP:LINK:FACTor?')
		return Conversions.str_to_float(response)
