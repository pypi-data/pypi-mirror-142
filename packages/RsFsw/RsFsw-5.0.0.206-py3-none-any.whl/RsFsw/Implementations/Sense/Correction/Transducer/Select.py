from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:SELect \n
		Snippet: driver.sense.correction.transducer.select.set(name = '1') \n
		This command selects a transducer factor. \n
			:param name: String containing the name of the transducer factor. If the name does not exist yet, the R&S FSW creates a transducer factor by that name.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:CORRection:TRANsducer:SELect {param}')
