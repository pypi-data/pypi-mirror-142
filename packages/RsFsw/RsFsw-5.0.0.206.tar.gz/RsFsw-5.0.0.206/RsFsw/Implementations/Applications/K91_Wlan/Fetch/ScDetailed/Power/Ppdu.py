from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ppdu:
	"""Ppdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppdu", core, parent)

	def get(self, sc_detailed_object: enums.ScDetailedObject) -> List[float]:
		"""SCPI: FETCh:SCDetailed:POWer:PPDU \n
		Snippet: value: List[float] = driver.applications.k91Wlan.fetch.scDetailed.power.ppdu.get(sc_detailed_object = enums.ScDetailedObject.DPILot) \n
		Returns the power results for each PPDU for the selected subcarriers. These results are only available if the Signal
		Content Detailed result display is currently active (see method RsFsw.Layout.Add.Window.get_) . \n
			:param sc_detailed_object: HELTf | DPILot | LLTF HELTf Includes long training field (HE-LTF) subcarriers only DPILot Includes data and pilot subcarriers only LLTF Includes legacy long training field (L-LTF) subcarriers only Unit: dBm
			:return: powers: No help available"""
		param = Conversions.enum_scalar_to_str(sc_detailed_object, enums.ScDetailedObject)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:SCDetailed:POWer:PPDU? {param}')
		return response
