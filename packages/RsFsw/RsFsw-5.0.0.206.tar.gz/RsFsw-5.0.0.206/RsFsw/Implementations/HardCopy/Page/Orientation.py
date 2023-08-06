from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orientation:
	"""Orientation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orientation", core, parent)

	def set(self, orientation: enums.PageOrientation) -> None:
		"""SCPI: HCOPy:PAGE:ORIentation \n
		Snippet: driver.hardCopy.page.orientation.set(orientation = enums.PageOrientation.LANDscape) \n
		The command selects the page orientation of the printout. The command is only available if the output device is a printer
		or a PDF file. \n
			:param orientation: LANDscape | PORTrait
		"""
		param = Conversions.enum_scalar_to_str(orientation, enums.PageOrientation)
		self._core.io.write(f'HCOPy:PAGE:ORIentation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PageOrientation:
		"""SCPI: HCOPy:PAGE:ORIentation \n
		Snippet: value: enums.PageOrientation = driver.hardCopy.page.orientation.get() \n
		The command selects the page orientation of the printout. The command is only available if the output device is a printer
		or a PDF file. \n
			:return: orientation: LANDscape | PORTrait"""
		response = self._core.io.query_str(f'HCOPy:PAGE:ORIentation?')
		return Conversions.str_to_scalar_enum(response, enums.PageOrientation)
