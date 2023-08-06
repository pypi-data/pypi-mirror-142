from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitErrorRate:
	"""BitErrorRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitErrorRate", core, parent)

	def get(self, format_py: enums.BerRateFormat, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:BERate \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.bitErrorRate.get(format_py = enums.BerRateFormat.CURRent, window = repcap.Window.Default) \n
		Queries the Bit Error Rate results. The available results are described in 'Bit error rate (BER) '.
		Note that the specified window suffix must refer to a BER result display. \n
			:param format_py: Specifies a particular BER result to be queried. If no parameter is specified, the current bit error rate is returned. The parameters for these results are listed in Table 'Parameters for BER result values'. DSINdex Queries the index of the identified data sequence found in a known data file. The index starts with 0, that is: the first data sequence in the file is returned as '0'.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: results: No help available"""
		param = Conversions.enum_scalar_to_str(format_py, enums.BerRateFormat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:BERate? {param}')
		return Conversions.str_to_float(response)
