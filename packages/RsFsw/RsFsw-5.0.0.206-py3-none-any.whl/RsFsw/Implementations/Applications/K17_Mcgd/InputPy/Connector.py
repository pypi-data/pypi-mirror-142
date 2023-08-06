from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, input_connectors: enums.InputConnectorC, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:CONNector \n
		Snippet: driver.applications.k17Mcgd.inputPy.connector.set(input_connectors = enums.InputConnectorC.RF, inputIx = repcap.InputIx.Default) \n
		Determines which connector the input for the measurement is taken from. For more information see 'Receiving Data Input
		and Providing Data Output'. \n
			:param input_connectors: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(input_connectors, enums.InputConnectorC)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.InputConnectorC:
		"""SCPI: INPut<Undef>:CONNector \n
		Snippet: value: enums.InputConnectorC = driver.applications.k17Mcgd.inputPy.connector.get(inputIx = repcap.InputIx.Default) \n
		Determines which connector the input for the measurement is taken from. For more information see 'Receiving Data Input
		and Providing Data Output'. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: input_connectors: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.InputConnectorC)
