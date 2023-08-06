from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btype:
	"""Btype commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btype", core, parent)

	@property
	def auto(self):
		"""auto commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, ppdu_type: str) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:BTYPe \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.btype.set(ppdu_type = '1') \n
		This remote control command specifies the type of PPDU to be analyzed. Only PPDUs of the specified type take part in
		measurement analysis. \n
			:param ppdu_type: 'LONG' Only long (DSSS) PLCP PPDUs are analyzed. Available for IEEE 802.11b, g. 'SHORT' Only short (DSSS) PLCP PPDUs are analyzed. Available for IEEE 802.11b, g. 'OFDM' Only OFDM PPDUs are analyzed. Available for IEEE 802.11g. 'MM20' IEEE 802.11n, Mixed Mode, 20 MHz sample rate Note that this setting is maintained for compatibility reasons only. Use the specified commands for new remote control programs (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]BANDwidth:CHANnel:AUTO:TYPE) . For new programs use: [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE MMIX [SENSe:]BANDwidth:CHANnel:AUTO:TYPE MB20 'GFM20' IEEE 802.11n Green Field Mode, 20 MHz sample rate Note that this setting is maintained for compatibility reasons only. Use the specified commands for new remote control programs (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]BANDwidth:CHANnel:AUTO:TYPE) . For new programs use: [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE MGRF [SENSe:]BANDwidth:CHANnel:AUTO:TYPE MB20
		"""
		param = Conversions.value_to_quoted_str(ppdu_type)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:BTYPe {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:BTYPe \n
		Snippet: value: str = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.btype.get() \n
		This remote control command specifies the type of PPDU to be analyzed. Only PPDUs of the specified type take part in
		measurement analysis. \n
			:return: ppdu_type: 'LONG' Only long (DSSS) PLCP PPDUs are analyzed. Available for IEEE 802.11b, g. 'SHORT' Only short (DSSS) PLCP PPDUs are analyzed. Available for IEEE 802.11b, g. 'OFDM' Only OFDM PPDUs are analyzed. Available for IEEE 802.11g. 'MM20' IEEE 802.11n, Mixed Mode, 20 MHz sample rate Note that this setting is maintained for compatibility reasons only. Use the specified commands for new remote control programs (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]BANDwidth:CHANnel:AUTO:TYPE) . For new programs use: [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE MMIX [SENSe:]BANDwidth:CHANnel:AUTO:TYPE MB20 'GFM20' IEEE 802.11n Green Field Mode, 20 MHz sample rate Note that this setting is maintained for compatibility reasons only. Use the specified commands for new remote control programs (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]BANDwidth:CHANnel:AUTO:TYPE) . For new programs use: [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE MGRF [SENSe:]BANDwidth:CHANnel:AUTO:TYPE MB20"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:BTYPe?')
		return trim_str_response(response)

	def clone(self) -> 'Btype':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Btype(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
