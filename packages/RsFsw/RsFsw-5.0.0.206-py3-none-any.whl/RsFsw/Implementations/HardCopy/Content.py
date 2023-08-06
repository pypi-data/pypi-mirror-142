from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Content:
	"""Content commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("content", core, parent)

	def set(self, arg_0: enums.HardcopyContent) -> None:
		"""SCPI: HCOPy:CONTent \n
		Snippet: driver.hardCopy.content.set(arg_0 = enums.HardcopyContent.HCOPy) \n
		This command determines the type of content included in the printout. This setting is independent of the printing device. \n
			:param arg_0: WINDows | HCOPy WINDows Includes only the selected windows in the printout. All currently active windows for the current channel (or 'MultiView') are available for selection. How many windows are printed on a each page of the printout is defined by method RsFsw.HardCopy.Page.Window.Count.set. This option is not available when copying to the clipboard (HCOP:DEST 'SYST:COMM:CLIP' or an image file (see method RsFsw.HardCopy.Device.Language.set) . If the destination is currently set to an image file or the clipboard, it is automatically changed to be a PDF file for the currently selected printing device. HCOPy Selects all measurement results displayed on the screen for the current channel (or 'MultiView') : diagrams, traces, markers, marker lists, limit lines, etc., including the channel bar and status bar, for printout on a single page. Displayed items belonging to the software user interface (e.g. softkeys) are not included. The size and position of the elements in the printout is identical to the screen display.
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.HardcopyContent)
		self._core.io.write(f'HCOPy:CONTent {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.HardcopyContent:
		"""SCPI: HCOPy:CONTent \n
		Snippet: value: enums.HardcopyContent = driver.hardCopy.content.get() \n
		This command determines the type of content included in the printout. This setting is independent of the printing device. \n
			:return: arg_0: WINDows | HCOPy WINDows Includes only the selected windows in the printout. All currently active windows for the current channel (or 'MultiView') are available for selection. How many windows are printed on a each page of the printout is defined by method RsFsw.HardCopy.Page.Window.Count.set. This option is not available when copying to the clipboard (HCOP:DEST 'SYST:COMM:CLIP' or an image file (see method RsFsw.HardCopy.Device.Language.set) . If the destination is currently set to an image file or the clipboard, it is automatically changed to be a PDF file for the currently selected printing device. HCOPy Selects all measurement results displayed on the screen for the current channel (or 'MultiView') : diagrams, traces, markers, marker lists, limit lines, etc., including the channel bar and status bar, for printout on a single page. Displayed items belonging to the software user interface (e.g. softkeys) are not included. The size and position of the elements in the printout is identical to the screen display."""
		response = self._core.io.query_str(f'HCOPy:CONTent?')
		return Conversions.str_to_scalar_enum(response, enums.HardcopyContent)
