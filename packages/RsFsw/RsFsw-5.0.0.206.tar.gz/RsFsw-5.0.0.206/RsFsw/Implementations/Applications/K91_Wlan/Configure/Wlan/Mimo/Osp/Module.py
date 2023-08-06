from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Module:
	"""Module commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("module", core, parent)

	def set(self, idn: enums.OspIdn) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:OSP:MODule \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.osp.module.set(idn = enums.OspIdn.A11) \n
		Specifies the module of the switch unit to be used for automated sequential MIMO measurements. The supported unit is
		Rohde & Schwarz OSP 1505.3009.03 with module option 1505.5101.02 \n
			:param idn: A11 | A12 | A13
		"""
		param = Conversions.enum_scalar_to_str(idn, enums.OspIdn)
		self._core.io.write(f'CONFigure:WLAN:MIMO:OSP:MODule {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OspIdn:
		"""SCPI: CONFigure:WLAN:MIMO:OSP:MODule \n
		Snippet: value: enums.OspIdn = driver.applications.k91Wlan.configure.wlan.mimo.osp.module.get() \n
		Specifies the module of the switch unit to be used for automated sequential MIMO measurements. The supported unit is
		Rohde & Schwarz OSP 1505.3009.03 with module option 1505.5101.02 \n
			:return: idn: A11 | A12 | A13"""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:OSP:MODule?')
		return Conversions.str_to_scalar_enum(response, enums.OspIdn)
