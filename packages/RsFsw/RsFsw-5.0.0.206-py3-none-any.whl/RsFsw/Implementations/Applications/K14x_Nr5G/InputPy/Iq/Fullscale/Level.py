from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, peak_voltage: float) -> None:
		"""SCPI: INPut:IQ:FULLscale[:LEVel] \n
		Snippet: driver.applications.k14Xnr5G.inputPy.iq.fullscale.level.set(peak_voltage = 1.0) \n
		No command help available \n
			:param peak_voltage: No help available
		"""
		param = Conversions.decimal_value_to_str(peak_voltage)
		self._core.io.write(f'INPut:IQ:FULLscale:LEVel {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:FULLscale[:LEVel] \n
		Snippet: value: float = driver.applications.k14Xnr5G.inputPy.iq.fullscale.level.get() \n
		No command help available \n
			:return: peak_voltage: No help available"""
		response = self._core.io.query_str(f'INPut:IQ:FULLscale:LEVel?')
		return Conversions.str_to_float(response)
