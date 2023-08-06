from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("add", core, parent)

	def set(self, add_pattern: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:PATTern:ADD \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.pattern.add.set(add_pattern = '1') \n
		This command adds a pattern to the current standard. Using the DDEM:SEAR:SYNC:SEL command, only those patterns can be
		selected which belong to the current standard (see [SENSe:]DDEMod:SEARch:SYNC:SELect) . \n
			:param add_pattern: No help available
		"""
		param = Conversions.value_to_quoted_str(add_pattern)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:PATTern:ADD {param}')
