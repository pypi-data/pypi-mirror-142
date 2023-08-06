from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Equalized:
	"""Equalized commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("equalized", core, parent)

	def get(self, input_py: enums.InputRf) -> str:
		"""SCPI: TRACe:IQ:EQUalized \n
		Snippet: value: str = driver.applications.k18AmplifierEt.trace.iq.equalized.get(input_py = enums.InputRf.RF) \n
		This command queries the equalized I/Q data.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Equalized data must be available. \n
			:param input_py: RF You have to state this parameter, but it is always 'RF'.
			:return: result: String containing the I/Q data."""
		param = Conversions.enum_scalar_to_str(input_py, enums.InputRf)
		response = self._core.io.query_str(f'TRACe:IQ:EQUalized? {param}')
		return trim_str_response(response)
