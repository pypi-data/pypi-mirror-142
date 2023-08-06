from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, connector: enums.InputConnectorB) -> None:
		"""SCPI: INPut:CONNector \n
		Snippet: driver.inputPy.connector.set(connector = enums.InputConnectorB.AIQI) \n
		Determines which connector the input for the measurement is taken from. For more information see 'Receiving Data Input
		and Providing Data Output'. \n
			:param connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.InputConnectorB)
		self._core.io.write_with_opc(f'INPut:CONNector {param}')
