from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Min:
	"""Min commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("min", core, parent)

	def set(self, num_data_bytes: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DBYTes:MIN \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.dbytes.min.set(num_data_bytes = 1.0) \n
		For IEEE 802.11b and g (DSSS) signals only: If the [SENSe:]DEMod:FORMat:BANalyze:DBYTes:EQUal command is set to true,
		then this command specifies the exact number of data bytes a PPDU must have to take part in measurement analysis. If the
		[SENSe:]DEMod:FORMat:BANalyze:DBYTes:EQUal command is set to false, this command specifies the minimum number of data
		bytes required for a PPDU to take part in measurement analysis. \n
			:param num_data_bytes: Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(num_data_bytes)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:DBYTes:MIN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:DBYTes:MIN \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.dbytes.min.get() \n
		For IEEE 802.11b and g (DSSS) signals only: If the [SENSe:]DEMod:FORMat:BANalyze:DBYTes:EQUal command is set to true,
		then this command specifies the exact number of data bytes a PPDU must have to take part in measurement analysis. If the
		[SENSe:]DEMod:FORMat:BANalyze:DBYTes:EQUal command is set to false, this command specifies the minimum number of data
		bytes required for a PPDU to take part in measurement analysis. \n
			:return: num_data_bytes: Unit: bytes"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:DBYTes:MIN?')
		return Conversions.str_to_float(response)
