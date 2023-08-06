from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Low:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, harm_order: float) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic[:LOW] \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.harmonic.low.set(harm_order = 1.0) \n
		No command help available \n
			:param harm_order: No help available
		"""
		param = Conversions.decimal_value_to_str(harm_order)
		self._core.io.write(f'SENSe:MIXer:HARMonic:LOW {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:HARMonic[:LOW] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.mixer.harmonic.low.get() \n
		No command help available \n
			:return: harm_order: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:LOW?')
		return Conversions.str_to_float(response)
