from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:MACCuracy:IQOFfset:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.maccuracy.iqOffset.current.result.get() \n
		This command queries the I/Q Offset as shown in the Result Summary. \n
			:return: iq_offset: numeric value Minimum, maximum or current I/Q Offset, depending on the command syntax. Unit: dB"""
		response = self._core.io.query_str(f'FETCh:MACCuracy:IQOFfset:CURRent:RESult?')
		return Conversions.str_to_float(response)
