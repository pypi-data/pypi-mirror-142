from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdevice:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Conn_State: float: Defines whether a device is connected or not. 0 No device is connected. 1 A device is connected.
			- Device_Name: float: Device ID of the connected device
			- Serial_Number: float: Serial number of the connected device
			- Port_Name: float: Port name used by the connected device
			- Sample_Rate: float: Current data transfer rate of the connected device in Hz
			- Max_Transfer_Rate: float: Maximum data transfer rate of the connected device in Hz
			- Conn_Prot_State: float: State of the connection protocol which is used to identify the connected device. Not Started Has to be Started Started Passed Failed Done"""
		__meta_args_list = [
			ArgStruct.scalar_float('Conn_State'),
			ArgStruct.scalar_float('Device_Name'),
			ArgStruct.scalar_float('Serial_Number'),
			ArgStruct.scalar_float('Port_Name'),
			ArgStruct.scalar_float('Sample_Rate'),
			ArgStruct.scalar_float('Max_Transfer_Rate'),
			ArgStruct.scalar_float('Conn_Prot_State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Conn_State: float = None
			self.Device_Name: float = None
			self.Serial_Number: float = None
			self.Port_Name: float = None
			self.Sample_Rate: float = None
			self.Max_Transfer_Rate: float = None
			self.Conn_Prot_State: float = None

	def get(self, outputConnector=repcap.OutputConnector.Default) -> GetStruct:
		"""SCPI: OUTPut<up>:DIQ:CDEVice \n
		Snippet: value: GetStruct = driver.output.diq.cdevice.get(outputConnector = repcap.OutputConnector.Default) \n
		This command queries the current configuration and the status of the digital I/Q data output to the optional Digital
		Baseband Interface. For details see 'Interface Status Information'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		return self._core.io.query_struct(f'OUTPut{outputConnector_cmd_val}:DIQ:CDEVice?', self.__class__.GetStruct())
