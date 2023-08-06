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
		"""SCPI: [SENSe]:DDEMod:TFILter:USER \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.tfilter.user.set(filter_name = '1') \n
		This command selects a user-defined transmit filter file. \n
			:param filter_name: The name of the transmit filter file.
		"""
		param = Conversions.value_to_quoted_str(filter_name)
		self._core.io.write(f'SENSe:DDEMod:TFILter:USER {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:TFILter:USER \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.tfilter.user.get() \n
		This command selects a user-defined transmit filter file. \n
			:return: filter_name: The name of the transmit filter file."""
		response = self._core.io.query_str(f'SENSe:DDEMod:TFILter:USER?')
		return trim_str_response(response)
