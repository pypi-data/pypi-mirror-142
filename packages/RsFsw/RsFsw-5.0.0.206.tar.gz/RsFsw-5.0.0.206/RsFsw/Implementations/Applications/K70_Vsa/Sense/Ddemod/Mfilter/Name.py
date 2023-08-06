from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:DDEMod:MFILter:NAME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.mfilter.name.set(name = '1') \n
		This command selects a measurement filter and automatically sets its state to 'ON'. \n
			:param name: Name of the measurement filter or 'User' for a user-defined filter. An overview of available measurement filters is provided in 'Measurement filters'.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:DDEMod:MFILter:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:MFILter:NAME \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.mfilter.name.get() \n
		This command selects a measurement filter and automatically sets its state to 'ON'. \n
			:return: name: Name of the measurement filter or 'User' for a user-defined filter. An overview of available measurement filters is provided in 'Measurement filters'."""
		response = self._core.io.query_str(f'SENSe:DDEMod:MFILter:NAME?')
		return trim_str_response(response)
