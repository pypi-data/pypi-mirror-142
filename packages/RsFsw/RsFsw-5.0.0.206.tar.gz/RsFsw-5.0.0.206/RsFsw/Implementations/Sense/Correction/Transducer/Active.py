from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Active:
	"""Active commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:TRANsducer:ACTive \n
		Snippet: value: str = driver.sense.correction.transducer.active.get() \n
		No command help available \n
			:return: transducer_factor: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:TRANsducer:ACTive?')
		return trim_str_response(response)
