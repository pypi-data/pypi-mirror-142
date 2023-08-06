from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NstsIndex:
	"""NstsIndex commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstsIndex", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, index: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:NSTSindex \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.nstsIndex.set(index = 1.0) \n
		Defines the PPDUs taking part in the analysis depending on their Nsts. This command is only available for the IEEE 802.11
		ac standard. This command is available for DEM:FORM:NSTS:MODE MEAS or DEM:FORM:NSTS:MODE DEM (see
		[SENSe:]DEMod:FORMat:NSTSindex:MODE) . \n
			:param index: No help available
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SENSe:DEMod:FORMat:NSTSindex {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:NSTSindex \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.nstsIndex.get() \n
		Defines the PPDUs taking part in the analysis depending on their Nsts. This command is only available for the IEEE 802.11
		ac standard. This command is available for DEM:FORM:NSTS:MODE MEAS or DEM:FORM:NSTS:MODE DEM (see
		[SENSe:]DEMod:FORMat:NSTSindex:MODE) . \n
			:return: index: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:NSTSindex?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'NstsIndex':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NstsIndex(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
