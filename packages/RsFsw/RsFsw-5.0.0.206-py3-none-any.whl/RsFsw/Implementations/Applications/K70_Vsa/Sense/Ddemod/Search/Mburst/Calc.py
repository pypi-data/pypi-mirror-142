from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calc:
	"""Calc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calc", core, parent)

	def set(self, select_res_range_nr: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:MBURst:CALC \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.mburst.calc.set(select_res_range_nr = 1.0) \n
		Sets the result range to be displayed after a single sweep (e.g. a burst number) . \n
			:param select_res_range_nr: No help available
		"""
		param = Conversions.decimal_value_to_str(select_res_range_nr)
		self._core.io.write(f'SENSe:DDEMod:SEARch:MBURst:CALC {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:MBURst:CALC \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.mburst.calc.get() \n
		Sets the result range to be displayed after a single sweep (e.g. a burst number) . \n
			:return: select_res_range_nr: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:MBURst:CALC?')
		return Conversions.str_to_float(response)
