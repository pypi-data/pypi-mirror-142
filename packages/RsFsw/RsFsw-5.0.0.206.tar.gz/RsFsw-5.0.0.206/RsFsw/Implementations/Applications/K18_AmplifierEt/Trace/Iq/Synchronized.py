from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronized:
	"""Synchronized commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronized", core, parent)

	def get(self, inp_mode: enums.BbOrRf) -> str:
		"""SCPI: TRACe:IQ:SYNChronized \n
		Snippet: value: str = driver.applications.k18AmplifierEt.trace.iq.synchronized.get(inp_mode = enums.BbOrRf.BB) \n
		This command queries the (measured) synchronized I/Q data (which corresponds to the green bar in the Magnitude Capture
		result display) . \n
			:param inp_mode: BB Queries the data captured on the optional analog baseband input. RF Queries the data captured on the RF input.
			:return: result: String containing the synchronized measurement values."""
		param = Conversions.enum_scalar_to_str(inp_mode, enums.BbOrRf)
		response = self._core.io.query_str(f'TRACe:IQ:SYNChronized? {param}')
		return trim_str_response(response)
