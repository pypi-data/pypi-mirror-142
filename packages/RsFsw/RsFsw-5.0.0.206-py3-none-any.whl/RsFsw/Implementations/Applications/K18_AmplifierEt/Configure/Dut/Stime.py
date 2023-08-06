from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stime:
	"""Stime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stime", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: CONFigure:DUT:STIMe \n
		Snippet: driver.applications.k18AmplifierEt.configure.dut.stime.set(time = 1.0) \n
		This command defines the settling time between generator setting changes and the start of the next measurement. \n
			:param time: numeric value Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:DUT:STIMe {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DUT:STIMe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.dut.stime.get() \n
		This command defines the settling time between generator setting changes and the start of the next measurement. \n
			:return: time: numeric value Unit: s"""
		response = self._core.io.query_str(f'CONFigure:DUT:STIMe?')
		return Conversions.str_to_float(response)
