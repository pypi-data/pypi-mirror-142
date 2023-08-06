from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resistor:
	"""Resistor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resistor", core, parent)

	def set(self, resistance: float) -> None:
		"""SCPI: CONFigure:PAE:ICHannel:RESistor \n
		Snippet: driver.applications.k18AmplifierEt.configure.pae.ichannel.resistor.set(resistance = 1.0) \n
		This command defines the characteristics of the shunt resistor used in the test setup. \n
			:param resistance: numeric value Resistance in Ohm.
		"""
		param = Conversions.decimal_value_to_str(resistance)
		self._core.io.write(f'CONFigure:PAE:ICHannel:RESistor {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PAE:ICHannel:RESistor \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.pae.ichannel.resistor.get() \n
		This command defines the characteristics of the shunt resistor used in the test setup. \n
			:return: resistance: numeric value Resistance in Ohm."""
		response = self._core.io.query_str(f'CONFigure:PAE:ICHannel:RESistor?')
		return Conversions.str_to_float(response)
