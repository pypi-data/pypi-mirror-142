from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> str:
		"""SCPI: [SENSe]:DEMod:FILTer:CATalog \n
		Snippet: value: str = driver.applications.k91Wlan.sense.demod.filterPy.catalog.get() \n
		This command reads the names of all available filters. \n
			:return: filters: list"""
		response = self._core.io.query_str(f'SENSe:DEMod:FILTer:CATalog?')
		return trim_str_response(response)
