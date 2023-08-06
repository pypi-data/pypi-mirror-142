from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, alpha: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:ACHannel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.filterPy.alpha.achannel.set(alpha = 1.0) \n
		No command help available \n
			:param alpha: No help available
		"""
		param = Conversions.decimal_value_to_str(alpha)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:ACHannel \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.filterPy.alpha.achannel.get() \n
		No command help available \n
			:return: alpha: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ACHannel?')
		return Conversions.str_to_float(response)
