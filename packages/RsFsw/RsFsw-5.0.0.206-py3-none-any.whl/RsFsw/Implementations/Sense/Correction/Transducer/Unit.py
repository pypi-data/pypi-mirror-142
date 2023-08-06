from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, unit: str) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:UNIT \n
		Snippet: driver.sense.correction.transducer.unit.set(unit = '1') \n
		This command selects the unit of the transducer factor. Before you can use the command, you have to select and turn on a
		transducer. \n
			:param unit: string as defined in table below
		"""
		param = Conversions.value_to_quoted_str(unit)
		self._core.io.write(f'SENSe:CORRection:TRANsducer:UNIT {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:TRANsducer:UNIT \n
		Snippet: value: str = driver.sense.correction.transducer.unit.get() \n
		This command selects the unit of the transducer factor. Before you can use the command, you have to select and turn on a
		transducer. \n
			:return: unit: string as defined in table below"""
		response = self._core.io.query_str(f'SENSe:CORRection:TRANsducer:UNIT?')
		return trim_str_response(response)
