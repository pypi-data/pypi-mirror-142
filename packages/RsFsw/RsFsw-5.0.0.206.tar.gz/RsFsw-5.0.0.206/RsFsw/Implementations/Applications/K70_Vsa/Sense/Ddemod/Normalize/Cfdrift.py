from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfdrift:
	"""Cfdrift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfdrift", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:NORMalize:CFDRift \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.normalize.cfdrift.set(state = False) \n
		This command defines whether the carrier frequency drift is compensated for FSK modulation. \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:NORMalize:CFDRift {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:NORMalize:CFDRift \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.normalize.cfdrift.get() \n
		This command defines whether the carrier frequency drift is compensated for FSK modulation. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:NORMalize:CFDRift?')
		return Conversions.str_to_bool(response)
