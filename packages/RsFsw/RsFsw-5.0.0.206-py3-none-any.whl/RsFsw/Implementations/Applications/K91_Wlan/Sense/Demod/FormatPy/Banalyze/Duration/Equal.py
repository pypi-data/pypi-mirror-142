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
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DURation:EQUal \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.duration.equal.set(state = False) \n
		For IEEE 802.11b and g (DSSS) signals only: If enabled, only PPDUs with a specific duration are considered for
		measurement analysis. If disabled, only PPDUs whose duration is within a specified range are considered. The duration is
		specified by the [SENSe:]DEMod:FORMat:BANalyze:DURation:MIN command. A duration range is defined as a minimum and maximum
		duration the PPDU may have (see [SENSe:]DEMod:FORMat:BANalyze:DURation:MAX and
		[SENSe:]DEMod:FORMat:BANalyze:DURation:MIN) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:DURation:EQUal {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DURation:EQUal \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.duration.equal.get() \n
		For IEEE 802.11b and g (DSSS) signals only: If enabled, only PPDUs with a specific duration are considered for
		measurement analysis. If disabled, only PPDUs whose duration is within a specified range are considered. The duration is
		specified by the [SENSe:]DEMod:FORMat:BANalyze:DURation:MIN command. A duration range is defined as a minimum and maximum
		duration the PPDU may have (see [SENSe:]DEMod:FORMat:BANalyze:DURation:MAX and
		[SENSe:]DEMod:FORMat:BANalyze:DURation:MIN) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:DURation:EQUal?')
		return Conversions.str_to_bool(response)
