from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interpolate:
	"""Interpolate commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interpolate", core, parent)

	@property
	def wiener(self):
		"""wiener commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wiener'):
			from .Wiener import Wiener
			self._wiener = Wiener(self._core, self._cmd_group)
		return self._wiener

	def set(self, interpolation: enums.DemodInterpolation) -> None:
		"""SCPI: [SENSe]:DEMod:INTerpolate \n
		Snippet: driver.applications.k91Wlan.sense.demod.interpolate.set(interpolation = enums.DemodInterpolation.LINear) \n
		No command help available \n
			:param interpolation: WIENer | LINear WIENer The unused subcarriers of the channel estimation fields (1xHE-LTF, 2xHE-LTF) are determined by Wiener interpolation. The estimated channel is smoothed. The Wiener interpolation overwrites the used subcarrier sampling points. In case all subcarriers are used (4xHE-LTF) , sampling points for all subcarriers are available. The channel is smoothed. LINear The unused subcarriers of the channel estimation fields (1xHE-LTF, 2xHE-LTF) are determined by linear interpolation. Linear interpolation preserves the used subcarrier sampling points. In case all subcarriers are used (4xHE-LTF) , the available sampling points for all subcarriers are preserved, and no interpolation is applied.
		"""
		param = Conversions.enum_scalar_to_str(interpolation, enums.DemodInterpolation)
		self._core.io.write(f'SENSe:DEMod:INTerpolate {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DemodInterpolation:
		"""SCPI: [SENSe]:DEMod:INTerpolate \n
		Snippet: value: enums.DemodInterpolation = driver.applications.k91Wlan.sense.demod.interpolate.get() \n
		No command help available \n
			:return: interpolation: WIENer | LINear WIENer The unused subcarriers of the channel estimation fields (1xHE-LTF, 2xHE-LTF) are determined by Wiener interpolation. The estimated channel is smoothed. The Wiener interpolation overwrites the used subcarrier sampling points. In case all subcarriers are used (4xHE-LTF) , sampling points for all subcarriers are available. The channel is smoothed. LINear The unused subcarriers of the channel estimation fields (1xHE-LTF, 2xHE-LTF) are determined by linear interpolation. Linear interpolation preserves the used subcarrier sampling points. In case all subcarriers are used (4xHE-LTF) , the available sampling points for all subcarriers are preserved, and no interpolation is applied."""
		response = self._core.io.query_str(f'SENSe:DEMod:INTerpolate?')
		return Conversions.str_to_scalar_enum(response, enums.DemodInterpolation)

	def clone(self) -> 'Interpolate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Interpolate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
