from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Load:
	"""Load commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("load", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:LOAD \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.load.set(filename = '1') \n
		Loads a user-defined frame structure configuration to be used by the measurement from an xml file. The default storage
		location for such files is C:/R_S/INSTR/USER/vsa/FrameRangeStructure. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param filename: string Path and file name of the xml file. The default storage location for frame structures is C:/R_S/INSTR/USER/vsa/FrameRange_Structure.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:LOAD {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:LOAD \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.frame.load.get() \n
		Loads a user-defined frame structure configuration to be used by the measurement from an xml file. The default storage
		location for such files is C:/R_S/INSTR/USER/vsa/FrameRangeStructure. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: filename: string Path and file name of the xml file. The default storage location for frame structures is C:/R_S/INSTR/USER/vsa/FrameRange_Structure."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:LOAD?')
		return trim_str_response(response)
