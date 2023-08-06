from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scd:
	"""Scd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scd", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:UL:FORMat:SCD \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.formatPy.scd.set(state = False) \n
		This command turns detection of the subframe configuration on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off auto demodulation [SENSe:][LTE:]UL:DEMod:ACON \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:UL:FORMat:SCD {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:UL:FORMat:SCD \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.uplink.formatPy.scd.get() \n
		This command turns detection of the subframe configuration on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off auto demodulation [SENSe:][LTE:]UL:DEMod:ACON \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:FORMat:SCD?')
		return Conversions.str_to_bool(response)
