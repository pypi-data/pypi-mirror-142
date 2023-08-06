from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remove:
	"""Remove commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remove", core, parent)

	def set(self, pattern: enums.SelectAll) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:PATTern:REMove \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.pattern.remove.set(pattern = enums.SelectAll.ALL) \n
		This command deletes one or all patterns from the current standard. \n
			:param pattern: (enum or string) No help available
		"""
		param = Conversions.enum_ext_scalar_to_str(pattern, enums.SelectAll)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:PATTern:REMove {param}')
