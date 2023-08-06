from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gexpansion:
	"""Gexpansion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gexpansion", core, parent)

	def set(self, gain_expansion: float) -> None:
		"""SCPI: CONFigure:DDPD:GEXPansion \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.gexpansion.set(gain_expansion = 1.0) \n
		This command sets the gain expansion for Direct DPD. \n
			:param gain_expansion: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(gain_expansion)
		self._core.io.write(f'CONFigure:DDPD:GEXPansion {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DDPD:GEXPansion \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.ddpd.gexpansion.get() \n
		This command sets the gain expansion for Direct DPD. \n
			:return: gain_expansion: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:DDPD:GEXPansion?')
		return Conversions.str_to_float(response)
