from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, file_path: str, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:SELect \n
		Snippet: driver.sense.correction.fresponse.baseband.user.slist.select.set(file_path = '1', touchStone = repcap.TouchStone.Default) \n
		Selects a Touchstone format file from the specified directory to be loaded to the current configuration for the specified
		input type. If no input type is specified, the currently active input source is assumed. The query returns the currently
		selected file. To determine which files are available, use [SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:CATalog?. \n
			:param file_path: string Path and file name of the selected file. The default directory for Touchstone files is C:/R_S/INSTR/USER/Fresponse.
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		param = Conversions.value_to_quoted_str(file_path)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:SELect {param}')
