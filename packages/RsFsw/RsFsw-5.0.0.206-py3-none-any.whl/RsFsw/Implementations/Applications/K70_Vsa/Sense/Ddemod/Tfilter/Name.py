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
		"""SCPI: [SENSe]:DDEMod:TFILter:NAME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.tfilter.name.set(name = '1') \n
		This command selects a transmit filter and automatically switches it on. For more information on transmit filters, refer
		to 'Transmit filters'. \n
			:param name: string Name of the Transmit filter; an overview of available transmit filters is provided in 'Transmit filters'.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:DDEMod:TFILter:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:TFILter:NAME \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.tfilter.name.get() \n
		This command selects a transmit filter and automatically switches it on. For more information on transmit filters, refer
		to 'Transmit filters'. \n
			:return: name: string Name of the Transmit filter; an overview of available transmit filters is provided in 'Transmit filters'."""
		response = self._core.io.query_str(f'SENSe:DDEMod:TFILter:NAME?')
		return trim_str_response(response)
