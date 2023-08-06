from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cestimation:
	"""Cestimation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cestimation", core, parent)

	def set(self, state: enums.ChannelEstimation) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CESTimation \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.cestimation.set(state = enums.ChannelEstimation.LINT) \n
		This command selects the channel estimation method. \n
			:param state: LINT Channel estimation by interpolating the missing information. NORMal Channel estimation according to 3GPP. OFF Turns off channel estimation. PILPay Channel estimation by examining both the reference signal and the payload resource elements.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.ChannelEstimation)
		self._core.io.write(f'SENSe:NR5G:DEMod:CESTimation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelEstimation:
		"""SCPI: [SENSe]:NR5G:DEMod:CESTimation \n
		Snippet: value: enums.ChannelEstimation = driver.applications.k14Xnr5G.sense.nr5G.demod.cestimation.get() \n
		This command selects the channel estimation method. \n
			:return: state: LINT Channel estimation by interpolating the missing information. NORMal Channel estimation according to 3GPP. OFF Turns off channel estimation. PILPay Channel estimation by examining both the reference signal and the payload resource elements."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CESTimation?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelEstimation)
