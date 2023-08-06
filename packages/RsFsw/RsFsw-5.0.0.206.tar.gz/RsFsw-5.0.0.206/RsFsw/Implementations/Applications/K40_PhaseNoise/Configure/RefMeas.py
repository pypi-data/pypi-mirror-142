from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefMeas:
	"""RefMeas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refMeas", core, parent)

	def set(self, once: enums.EventOnce) -> None:
		"""SCPI: CONFigure:REFMeas \n
		Snippet: driver.applications.k40PhaseNoise.configure.refMeas.set(once = enums.EventOnce.ONCE) \n
		This command initiates a reference measurement that determines the inherent phase noise of the R&S FSW. \n
			:param once: ONCE
		"""
		param = Conversions.enum_scalar_to_str(once, enums.EventOnce)
		self._core.io.write(f'CONFigure:REFMeas {param}')
