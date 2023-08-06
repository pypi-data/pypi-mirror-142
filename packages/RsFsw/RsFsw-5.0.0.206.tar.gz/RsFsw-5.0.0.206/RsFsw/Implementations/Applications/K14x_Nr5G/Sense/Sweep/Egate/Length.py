from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LENGth \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.length.set(length = 1.0) \n
		No command help available \n
			:param length: No help available
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:SWEep:EGATe:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LENGth \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.length.get() \n
		No command help available \n
			:return: length: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LENGth?')
		return Conversions.str_to_float(response)
