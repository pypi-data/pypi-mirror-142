from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	def set(self, state: float or bool) -> None:
		"""SCPI: CONFigure[:NR5G]:EVM \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.evm.set(state = 1.0) \n
		This command includes or excludes EVM measurements from combined measurements. \n
			:param state: (float or boolean) ON | OFF | 1 | 0
		"""
		param = Conversions.decimal_or_bool_value_to_str(state)
		self._core.io.write(f'CONFigure:NR5G:EVM {param}')

	def get(self) -> float or bool:
		"""SCPI: CONFigure[:NR5G]:EVM \n
		Snippet: value: float or bool = driver.applications.k14Xnr5G.configure.nr5G.evm.get() \n
		This command includes or excludes EVM measurements from combined measurements. \n
			:return: state: (float or boolean) ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:NR5G:EVM?')
		return Conversions.str_to_float_or_bool(response)
