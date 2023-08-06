from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmode:
	"""Pmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmode", core, parent)

	def set(self, result: enums.ResultNr5G) -> None:
		"""SCPI: [SENSe]:NR5G:RSUMmary:PMODe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.rsummary.pmode.set(result = enums.ResultNr5G.AASL) \n
		This command selects the power averaging mode. \n
			:param result: AASL Power avergaing over all symbols in a slot. AASY Power avergaing over all used symbols in a slot.
		"""
		param = Conversions.enum_scalar_to_str(result, enums.ResultNr5G)
		self._core.io.write(f'SENSe:NR5G:RSUMmary:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ResultNr5G:
		"""SCPI: [SENSe]:NR5G:RSUMmary:PMODe \n
		Snippet: value: enums.ResultNr5G = driver.applications.k14Xnr5G.sense.nr5G.rsummary.pmode.get() \n
		This command selects the power averaging mode. \n
			:return: result: AASL Power avergaing over all symbols in a slot. AASY Power avergaing over all used symbols in a slot."""
		response = self._core.io.query_str(f'SENSe:NR5G:RSUMmary:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ResultNr5G)
