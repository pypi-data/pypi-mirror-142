from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Header:
	"""Header commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("header", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: FORMat:DEXPort:HEADer \n
		Snippet: driver.applications.k70Vsa.formatPy.dexport.header.set(state = False) \n
		This command defines if a file header (including start frequency, sweep time, detector, etc.) is created or not. A short
		header with the instrument model, the version and the date is always transferred. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'FORMat:DEXPort:HEADer {param}')

	def get(self) -> bool:
		"""SCPI: FORMat:DEXPort:HEADer \n
		Snippet: value: bool = driver.applications.k70Vsa.formatPy.dexport.header.get() \n
		This command defines if a file header (including start frequency, sweep time, detector, etc.) is created or not. A short
		header with the instrument model, the version and the date is always transferred. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'FORMat:DEXPort:HEADer?')
		return Conversions.str_to_bool(response)
