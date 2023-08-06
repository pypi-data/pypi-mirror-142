from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcs:
	"""Fcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcs", core, parent)

	def set(self, mac_fcs: enums.MacFcs) -> None:
		"""SCPI: [SENSe]:DEMod:MAC:FCS \n
		Snippet: driver.applications.k149Uwb.sense.demod.mac.fcs.set(mac_fcs = enums.MacFcs.O2) \n
		Enable FCS check of payload either with 2 octet or with 4 octet format. \n
			:param mac_fcs: OFF OFF O2 2 Octets O4 4 Octets
		"""
		param = Conversions.enum_scalar_to_str(mac_fcs, enums.MacFcs)
		self._core.io.write(f'SENSe:DEMod:MAC:FCS {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MacFcs:
		"""SCPI: [SENSe]:DEMod:MAC:FCS \n
		Snippet: value: enums.MacFcs = driver.applications.k149Uwb.sense.demod.mac.fcs.get() \n
		Enable FCS check of payload either with 2 octet or with 4 octet format. \n
			:return: mac_fcs: OFF OFF O2 2 Octets O4 4 Octets"""
		response = self._core.io.query_str(f'SENSe:DEMod:MAC:FCS?')
		return Conversions.str_to_scalar_enum(response, enums.MacFcs)
