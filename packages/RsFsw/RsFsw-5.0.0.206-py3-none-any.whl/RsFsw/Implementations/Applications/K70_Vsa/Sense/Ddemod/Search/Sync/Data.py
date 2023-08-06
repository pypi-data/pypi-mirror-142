from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:DATA \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.data.set(data = '1') \n
		This command defines the sync sequence of a sync pattern. The pattern must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. Important: The value range of a symbol depends on the degree of modulation,e.g. for an
		8PSK modulation the value range is from 0 to 7. The degree of modulation belongs to the pattern and is set using the
		DDEM:SEAR:SYNC:NST command (see [SENSe:]DDEMod:SEARch:SYNC:NSTate) . \n
			:param data: Four values represent a symbol (hexadecimal format) . The value range of a symbol depends on the degree of modulation. With a degree of modulation of 4, all symbols have a value range of: 0000, 0001, 0002, 0003 With a degree of modulation of 8: 0000, 0001, 0002, 0003, 0004, 0005, 0006, 0007
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:DATA {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:DATA \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.data.get() \n
		This command defines the sync sequence of a sync pattern. The pattern must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. Important: The value range of a symbol depends on the degree of modulation,e.g. for an
		8PSK modulation the value range is from 0 to 7. The degree of modulation belongs to the pattern and is set using the
		DDEM:SEAR:SYNC:NST command (see [SENSe:]DDEMod:SEARch:SYNC:NSTate) . \n
			:return: data: Four values represent a symbol (hexadecimal format) . The value range of a symbol depends on the degree of modulation. With a degree of modulation of 4, all symbols have a value range of: 0000, 0001, 0002, 0003 With a degree of modulation of 8: 0000, 0001, 0002, 0003, 0004, 0005, 0006, 0007"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:DATA?')
		return trim_str_response(response)
