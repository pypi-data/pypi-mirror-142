from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def set(self, duration: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DURation:MAX \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.duration.max.set(duration = 1.0) \n
		For IEEE 802.11b and g (DSSS) signals only: If the [SENSe:]DEMod:FORMat:BANalyze:DURation:EQUal command is set to false,
		this command specifies the maximum number of symbols allowed for a PPDU to take part in measurement analysis.
		If the [SENSe:]DEMod:FORMat:BANalyze:DURation:EQUal command is set to true, then this command has no effect. \n
			:param duration: Unit: us
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:DURation:MAX {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DURation:MAX \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.duration.max.get() \n
		For IEEE 802.11b and g (DSSS) signals only: If the [SENSe:]DEMod:FORMat:BANalyze:DURation:EQUal command is set to false,
		this command specifies the maximum number of symbols allowed for a PPDU to take part in measurement analysis.
		If the [SENSe:]DEMod:FORMat:BANalyze:DURation:EQUal command is set to true, then this command has no effect. \n
			:return: duration: Unit: us"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:DURation:MAX?')
		return Conversions.str_to_float(response)
