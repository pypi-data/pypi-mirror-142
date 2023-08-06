from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bstation:
	"""Bstation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bstation", core, parent)

	def set(self, bs_type: enums.BsType) -> None:
		"""SCPI: CONFigure[:NR5G]:BSTation \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.bstation.set(bs_type = enums.BsType.FR1C) \n
		This command selects the base station type. \n
			:param bs_type: FR1C Base station for conducted requirements. FR1H Base station for hybrid requirements. FR1O Base station for over-the-air requirements in FR1. (Only for ACLR and SEM measurements.) FR2O Base station for over-the-air requirements in FR2. (Only for ACLR and SEM measurements.)
		"""
		param = Conversions.enum_scalar_to_str(bs_type, enums.BsType)
		self._core.io.write(f'CONFigure:NR5G:BSTation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BsType:
		"""SCPI: CONFigure[:NR5G]:BSTation \n
		Snippet: value: enums.BsType = driver.applications.k14Xnr5G.configure.nr5G.bstation.get() \n
		This command selects the base station type. \n
			:return: bs_type: FR1C Base station for conducted requirements. FR1H Base station for hybrid requirements. FR1O Base station for over-the-air requirements in FR1. (Only for ACLR and SEM measurements.) FR2O Base station for over-the-air requirements in FR2. (Only for ACLR and SEM measurements.)"""
		response = self._core.io.query_str(f'CONFigure:NR5G:BSTation?')
		return Conversions.str_to_scalar_enum(response, enums.BsType)
