from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rantenna:
	"""Rantenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rantenna", core, parent)

	def set(self, antenna: enums.SignalPath) -> None:
		"""SCPI: [SENSe]:NR5G:RANTenna \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.rantenna.set(antenna = enums.SignalPath.RX1) \n
		No command help available \n
			:param antenna: No help available
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.SignalPath)
		self._core.io.write(f'SENSe:NR5G:RANTenna {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalPath:
		"""SCPI: [SENSe]:NR5G:RANTenna \n
		Snippet: value: enums.SignalPath = driver.applications.k14Xnr5G.sense.nr5G.rantenna.get() \n
		No command help available \n
			:return: antenna: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:RANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPath)
