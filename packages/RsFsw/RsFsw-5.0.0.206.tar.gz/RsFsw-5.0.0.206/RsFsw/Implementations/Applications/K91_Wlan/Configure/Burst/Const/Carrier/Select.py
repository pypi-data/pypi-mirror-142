from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, carriers: int) -> None:
		"""SCPI: CONFigure:BURSt:CONSt:CARRier:SELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.const.carrier.select.set(carriers = 1) \n
		Defines the carriers included in the constellation diagram. \n
			:param carriers: ALL Results for all carriers PILots Results for pilot carriers only integer Specific carrier number only
		"""
		param = Conversions.decimal_value_to_str(carriers)
		self._core.io.write(f'CONFigure:BURSt:CONSt:CARRier:SELect {param}')

	def get(self) -> int:
		"""SCPI: CONFigure:BURSt:CONSt:CARRier:SELect \n
		Snippet: value: int = driver.applications.k91Wlan.configure.burst.const.carrier.select.get() \n
		Defines the carriers included in the constellation diagram. \n
			:return: carriers: ALL Results for all carriers PILots Results for pilot carriers only integer Specific carrier number only"""
		response = self._core.io.query_str(f'CONFigure:BURSt:CONSt:CARRier:SELect?')
		return Conversions.str_to_int(response)
