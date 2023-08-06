from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eauto:
	"""Eauto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eauto", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceSource:
		"""SCPI: [SENSe]:ROSCillator:SOURce:EAUTo \n
		Snippet: value: enums.ReferenceSource = driver.sense.roscillator.source.eauto.get() \n
		This command queries the current reference type in case you have activated an automatic switch to the internal reference
		if the external reference is missing. \n
			:return: reference: INT | EXT INT internal reference EXT external reference"""
		response = self._core.io.query_str(f'SENSe:ROSCillator:SOURce:EAUTo?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceSource)
