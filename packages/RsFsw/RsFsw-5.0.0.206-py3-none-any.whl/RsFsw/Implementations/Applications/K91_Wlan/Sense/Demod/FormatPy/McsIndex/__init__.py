from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsIndex:
	"""McsIndex commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsIndex", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, index: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:MCSindex \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.mcsIndex.set(index = 1.0) \n
		This command specifies the MCS index which controls the data rate, modulation and streams (for IEEE 802.11n, ac standards
		only, see document: IEEE 802.11n/D11.0 June 2009) . This command is required if [SENSe:]DEMod:FORMat:MCSindex:MODE is set
		to MEAS or DEM. \n
			:param index: Range: 0 to 11
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SENSe:DEMod:FORMat:MCSindex {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:MCSindex \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.mcsIndex.get() \n
		This command specifies the MCS index which controls the data rate, modulation and streams (for IEEE 802.11n, ac standards
		only, see document: IEEE 802.11n/D11.0 June 2009) . This command is required if [SENSe:]DEMod:FORMat:MCSindex:MODE is set
		to MEAS or DEM. \n
			:return: index: Range: 0 to 11"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:MCSindex?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'McsIndex':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = McsIndex(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
