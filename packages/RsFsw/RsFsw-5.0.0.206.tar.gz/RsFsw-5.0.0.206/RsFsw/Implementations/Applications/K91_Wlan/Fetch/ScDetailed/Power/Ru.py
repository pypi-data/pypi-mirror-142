from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ru:
	"""Ru commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ru", core, parent)

	def get(self, sc_detailed_object: enums.ScDetailedObject) -> List[float]:
		"""SCPI: FETCh:SCDetailed:POWer:RU \n
		Snippet: value: List[float] = driver.applications.k91Wlan.fetch.scDetailed.power.ru.get(sc_detailed_object = enums.ScDetailedObject.DPILot) \n
		Returns the power in all PPDUs for each RU. The result is a comma-separated list of power values, one per RU.
		These results are only available if the Signal Content Detailed result display is currently active (see method RsFsw.
		Layout.Add.Window.get_) . Tip: to obtain the results for an individual subcarrier, use method RsFsw.Applications.K91_Wlan.
		Fetch.ScDetailed.Power.Sc.get_. \n
			:param sc_detailed_object: HELTf | DPILot | LLTF HELTf Includes long training field (HE-LTF) subcarriers only DPILot Includes data and pilot subcarriers only Unit: dBm
			:return: powers: No help available"""
		param = Conversions.enum_scalar_to_str(sc_detailed_object, enums.ScDetailedObject)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:SCDetailed:POWer:RU? {param}')
		return response
