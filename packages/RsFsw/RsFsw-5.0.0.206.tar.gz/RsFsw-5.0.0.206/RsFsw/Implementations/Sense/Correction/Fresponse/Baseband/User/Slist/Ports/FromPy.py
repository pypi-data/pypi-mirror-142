from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FromPy:
	"""FromPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fromPy", core, parent)

	def set(self, port_from: int, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:PORTs:FROM \n
		Snippet: driver.sense.correction.fresponse.baseband.user.slist.ports.fromPy.set(port_from = 1, touchStone = repcap.TouchStone.Default) \n
		SnP files can be defined for a varying number of input and output ports. You must define the ports from the touchstone
		file whose data is to be applied. \n
			:param port_from: No help available
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		param = Conversions.decimal_value_to_str(port_from)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:PORTs:FROM {param}')

	def get(self, touchStone=repcap.TouchStone.Default) -> int:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:PORTs:FROM \n
		Snippet: value: int = driver.sense.correction.fresponse.baseband.user.slist.ports.fromPy.get(touchStone = repcap.TouchStone.Default) \n
		SnP files can be defined for a varying number of input and output ports. You must define the ports from the touchstone
		file whose data is to be applied. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:return: port_from: No help available"""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:PORTs:FROM?')
		return Conversions.str_to_int(response)
