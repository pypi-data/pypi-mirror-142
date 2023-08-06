from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa[:ALL] \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.filterPy.alpha.all.set(value = 1.0) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ALL {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa[:ALL] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.filterPy.alpha.all.get() \n
		No command help available \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ALL?')
		return Conversions.str_to_float(response)
