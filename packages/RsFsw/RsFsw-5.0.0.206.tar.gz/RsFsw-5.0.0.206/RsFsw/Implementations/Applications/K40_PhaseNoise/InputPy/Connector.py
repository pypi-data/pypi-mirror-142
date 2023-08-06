from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, conn_type: enums.InputConnectorB) -> None:
		"""SCPI: INPut:CONNector \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.connector.set(conn_type = enums.InputConnectorB.AIQI) \n
		Determines which connector the input for the measurement is taken from. For more information see 'Receiving Data Input
		and Providing Data Output'. \n
			:param conn_type: RF RF input connector AIQI Analog Baseband I connector This setting is only available if the Analog Baseband interface (R&S FSW-B71) is installed and active for input. It is not available for the R&S FSW67 or R&S FSW85. RFPRobe Active RF probe
		"""
		param = Conversions.enum_scalar_to_str(conn_type, enums.InputConnectorB)
		self._core.io.write(f'INPut:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputConnectorB:
		"""SCPI: INPut:CONNector \n
		Snippet: value: enums.InputConnectorB = driver.applications.k40PhaseNoise.inputPy.connector.get() \n
		Determines which connector the input for the measurement is taken from. For more information see 'Receiving Data Input
		and Providing Data Output'. \n
			:return: conn_type: RF RF input connector AIQI Analog Baseband I connector This setting is only available if the Analog Baseband interface (R&S FSW-B71) is installed and active for input. It is not available for the R&S FSW67 or R&S FSW85. RFPRobe Active RF probe"""
		response = self._core.io.query_str(f'INPut:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.InputConnectorB)
