from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: SOURce:POWer[:LEVel][:IMMediate]:OFFSet \n
		Snippet: driver.source.power.level.immediate.offset.set(offset = 1.0) \n
		This command is only valid if External Generator Control (R&S FSW-B10) is installed. \n
			:param offset: Range: -200 dB to +200 dB, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce:POWer:LEVel:IMMediate:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: SOURce:POWer[:LEVel][:IMMediate]:OFFSet \n
		Snippet: value: float = driver.source.power.level.immediate.offset.get() \n
		This command is only valid if External Generator Control (R&S FSW-B10) is installed. \n
			:return: offset: Range: -200 dB to +200 dB, Unit: DB"""
		response = self._core.io.query_str(f'SOURce:POWer:LEVel:IMMediate:OFFSet?')
		return Conversions.str_to_float(response)
