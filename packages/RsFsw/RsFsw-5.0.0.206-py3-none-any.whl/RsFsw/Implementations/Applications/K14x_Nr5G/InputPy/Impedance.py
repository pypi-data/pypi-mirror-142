from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impedance:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: float) -> None:
		"""SCPI: INPut:IMPedance \n
		Snippet: driver.applications.k14Xnr5G.inputPy.impedance.set(impedance = 1.0) \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:param impedance: 50 | 75 Unit: OHM
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write(f'INPut:IMPedance {param}')

	def get(self) -> float:
		"""SCPI: INPut:IMPedance \n
		Snippet: value: float = driver.applications.k14Xnr5G.inputPy.impedance.get() \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:return: impedance: 50 | 75 Unit: OHM"""
		response = self._core.io.query_str(f'INPut:IMPedance?')
		return Conversions.str_to_float(response)
