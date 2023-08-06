from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tstamp:
	"""Tstamp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tstamp", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: FORMat:DEXPort:TSTamp \n
		Snippet: driver.applications.k6Pulse.formatPy.dexport.tstamp.set(state = False) \n
		Turns on display of absolute time stamp for table export. \n
			:param state: ON | OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'FORMat:DEXPort:TSTamp {param}')

	def get(self) -> bool:
		"""SCPI: FORMat:DEXPort:TSTamp \n
		Snippet: value: bool = driver.applications.k6Pulse.formatPy.dexport.tstamp.get() \n
		Turns on display of absolute time stamp for table export. \n
			:return: state: ON | OFF"""
		response = self._core.io.query_str(f'FORMat:DEXPort:TSTamp?')
		return Conversions.str_to_bool(response)
