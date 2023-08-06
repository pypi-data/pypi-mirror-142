from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:CARRier:OFFSet \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.carrier.offset.get() \n
		Frequency offset of the captured multi-carrier signal compared to the setting given by multi-carrier signal description.
		This frequency offset is estimated and compensated when using carrier estimation modes 'Offset' or 'All Carriers'. \n
			:return: carrier_offset: Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:CARRier:OFFSet?')
		return Conversions.str_to_float(response)
