from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:SFIeld:ALL \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.sfield.all.get() \n
		Returns the results of the Signal Fields table, including column headers. The result is a comma-separated list of values
		for the selected PPDU. For details on the provided information see 'Signal Field' This command is only available for the
		IEEE 802.11ax, be standards. For other standards, see method RsFsw.Trace.Data.get_. \n
			:return: result: Signal_field_type[,Occupied_bits,Field_name, Binary_value,Human_readable_value],..."""
		response = self._core.io.query_str(f'FETCh:SFIeld:ALL?')
		return trim_str_response(response)
