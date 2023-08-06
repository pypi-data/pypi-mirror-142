from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PLENgth \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.continuous.plength.set(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'SENSe:SWEep:EGATe:CONTinuous:PLENgth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PLENgth \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.continuous.plength.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:CONTinuous:PLENgth?')
		return Conversions.str_to_float(response)
