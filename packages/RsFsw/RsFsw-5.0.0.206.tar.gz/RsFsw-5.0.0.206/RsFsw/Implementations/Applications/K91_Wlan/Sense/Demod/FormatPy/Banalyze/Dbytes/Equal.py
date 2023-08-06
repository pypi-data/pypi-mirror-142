from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Equal:
	"""Equal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("equal", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DBYTes:EQUal \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.dbytes.equal.set(state = False) \n
		For IEEE 802.11b and g (DSSS) signals only: If enabled, only PPDUs with a specific payload length are considered for
		measurement analysis. If disabled, only PPDUs whose length is within a specified range are considered. The payload length
		is specified by the [SENSe:]DEMod:FORMat:BANalyze:DBYTes:MIN command. A payload length range is defined as a minimum and
		maximum number of symbols the payload may contain (see [SENSe:]DEMod:FORMat:BANalyze:DBYTes:MAX and
		[SENSe:]DEMod:FORMat:BANalyze:DBYTes:MIN) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:DBYTes:EQUal {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DBYTes:EQUal \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.dbytes.equal.get() \n
		For IEEE 802.11b and g (DSSS) signals only: If enabled, only PPDUs with a specific payload length are considered for
		measurement analysis. If disabled, only PPDUs whose length is within a specified range are considered. The payload length
		is specified by the [SENSe:]DEMod:FORMat:BANalyze:DBYTes:MIN command. A payload length range is defined as a minimum and
		maximum number of symbols the payload may contain (see [SENSe:]DEMod:FORMat:BANalyze:DBYTes:MAX and
		[SENSe:]DEMod:FORMat:BANalyze:DBYTes:MIN) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:DBYTes:EQUal?')
		return Conversions.str_to_bool(response)
