from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crate:
	"""Crate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def set(self, chip_rate: float) -> None:
		"""SCPI: CONFigure:EDMG:CRATe \n
		Snippet: driver.applications.k9X11Ad.configure.edmg.crate.set(chip_rate = 1.0) \n
		Chip rate used for transmission; specified in the IEEE 802.11 ay standard as: NCB * 1.76 GHz \n
			:param chip_rate: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(chip_rate)
		self._core.io.write(f'CONFigure:EDMG:CRATe {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:EDMG:CRATe \n
		Snippet: value: float = driver.applications.k9X11Ad.configure.edmg.crate.get() \n
		Chip rate used for transmission; specified in the IEEE 802.11 ay standard as: NCB * 1.76 GHz \n
			:return: chip_rate: Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:EDMG:CRATe?')
		return Conversions.str_to_float(response)
