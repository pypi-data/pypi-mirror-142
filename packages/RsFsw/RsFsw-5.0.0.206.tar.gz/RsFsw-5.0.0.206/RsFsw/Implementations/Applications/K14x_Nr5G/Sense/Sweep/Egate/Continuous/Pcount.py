from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcount:
	"""Pcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcount", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PCOunt \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.continuous.pcount.set(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'SENSe:SWEep:EGATe:CONTinuous:PCOunt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PCOunt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.continuous.pcount.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:CONTinuous:PCOunt?')
		return Conversions.str_to_float(response)
