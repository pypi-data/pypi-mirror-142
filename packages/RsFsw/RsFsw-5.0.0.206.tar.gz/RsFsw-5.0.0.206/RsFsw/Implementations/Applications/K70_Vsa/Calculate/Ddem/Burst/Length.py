from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:DDEM:BURSt:LENGth \n
		Snippet: value: int = driver.applications.k70Vsa.calculate.ddem.burst.length.get(window = repcap.Window.Default) \n
		This command queries the length of a detected burst. Note that since the R&S FSW VSA application has no knowledge on the
		ramp length, there is an uncertainty in the burst search algorithm. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: length: integer Number of symbols"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DDEM:BURSt:LENGth?')
		return Conversions.str_to_int(response)
