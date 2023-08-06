from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, file_path: str, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:INSert \n
		Snippet: driver.sense.correction.fresponse.baseband.user.slist.insert.set(file_path = '1', touchStone = repcap.TouchStone.Default) \n
		Loads a new Touchstone file for the current configuration. The maximum number of files per configuration is 15. The new
		file is added below the entry specified by the <sli> index. All other entries with a higher suffix are moved down by one
		position. To change the order of the files, use the [SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:MOVE command.
		To determine which files are available, use [SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:CATalog?. \n
			:param file_path: string Path and file name The file extension of the Touchstone file must correspond to the number of ports included in the file. For example, a file containing 4 parameters for S11, S22, S12 and S21 must have the extension .s2p. The default directory for Touchstone files is C:/R_S/INSTR/USER/Fresponse.
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		param = Conversions.value_to_quoted_str(file_path)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:INSert {param}')

	def get(self, touchStone=repcap.TouchStone.Default) -> str:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:INSert \n
		Snippet: value: str = driver.sense.correction.fresponse.baseband.user.slist.insert.get(touchStone = repcap.TouchStone.Default) \n
		Loads a new Touchstone file for the current configuration. The maximum number of files per configuration is 15. The new
		file is added below the entry specified by the <sli> index. All other entries with a higher suffix are moved down by one
		position. To change the order of the files, use the [SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:MOVE command.
		To determine which files are available, use [SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:CATalog?. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:return: file_path: string Path and file name The file extension of the Touchstone file must correspond to the number of ports included in the file. For example, a file containing 4 parameters for S11, S22, S12 and S21 must have the extension .s2p. The default directory for Touchstone files is C:/R_S/INSTR/USER/Fresponse."""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:INSert?')
		return trim_str_response(response)
