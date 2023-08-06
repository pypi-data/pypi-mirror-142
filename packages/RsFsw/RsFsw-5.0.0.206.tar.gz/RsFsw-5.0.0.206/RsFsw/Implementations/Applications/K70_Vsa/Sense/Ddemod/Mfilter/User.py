from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def set(self, filter_name: str) -> None:
		"""SCPI: [SENSe]:DDEMod:MFILter:USER \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.mfilter.user.set(filter_name = '1') \n
		This command selects the user-defined measurement filter. For details on user-defined filters, see 'Customized filters'. \n
			:param filter_name: Name of the user-defined filter
		"""
		param = Conversions.value_to_quoted_str(filter_name)
		self._core.io.write(f'SENSe:DDEMod:MFILter:USER {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:MFILter:USER \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.mfilter.user.get() \n
		This command selects the user-defined measurement filter. For details on user-defined filters, see 'Customized filters'. \n
			:return: filter_name: Name of the user-defined filter"""
		response = self._core.io.query_str(f'SENSe:DDEMod:MFILter:USER?')
		return trim_str_response(response)
