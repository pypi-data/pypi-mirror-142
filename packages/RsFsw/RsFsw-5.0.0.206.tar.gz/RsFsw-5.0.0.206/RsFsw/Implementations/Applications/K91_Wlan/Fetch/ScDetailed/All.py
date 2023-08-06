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
		"""SCPI: FETCh:SCDetailed:ALL \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.scDetailed.all.get() \n
		Returns detailed signal information for each decoded RU and for each object. The result is a comma-separated list of
		values with 4 rows per RU, in the same order as the Signal Content Detailed result display (see 'Signal Content Detailed
		(IEEE 802.11ax, be) ') . These results are only available if the Signal Content Detailed result display is currently
		active (see method RsFsw.Layout.Add.Window.get_) .
			INTRO_CMD_HELP: The information for each decoded RU is returned in the following object order: \n
			- (As of firmware version 3.20:) Legacy long training field (L-LTF)
			- Long training field (HE-LTF)
			- Long training field (HE-LTF)
			- Data + Pilot
			- Data only
			- Pilot only \n
			:return: result: integer"""
		response = self._core.io.query_str(f'FETCh:SCDetailed:ALL?')
		return trim_str_response(response)
