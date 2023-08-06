from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, method: enums.MimoAnalyzeMethod) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure:TYPE \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.capture.typePy.set(method = enums.MimoAnalyzeMethod.MANual) \n
		Specifies the method used to analyze MIMO signals. \n
			:param method: SIMultaneous | OSP | MANual SIMultaneous Simultaneous normal MIMO operation OSP Sequential using open switch platform MANual Sequential using manual operation
		"""
		param = Conversions.enum_scalar_to_str(method, enums.MimoAnalyzeMethod)
		self._core.io.write(f'CONFigure:WLAN:MIMO:CAPTure:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MimoAnalyzeMethod:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure:TYPE \n
		Snippet: value: enums.MimoAnalyzeMethod = driver.applications.k91Wlan.configure.wlan.mimo.capture.typePy.get() \n
		Specifies the method used to analyze MIMO signals. \n
			:return: method: SIMultaneous | OSP | MANual SIMultaneous Simultaneous normal MIMO operation OSP Sequential using open switch platform MANual Sequential using manual operation"""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:CAPTure:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.MimoAnalyzeMethod)
