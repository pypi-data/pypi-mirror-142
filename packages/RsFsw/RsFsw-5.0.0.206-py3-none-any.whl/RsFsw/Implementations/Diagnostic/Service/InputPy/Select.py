from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, signal: enums.DiagnosticSignal) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut[:SELect] \n
		Snippet: driver.diagnostic.service.inputPy.select.set(signal = enums.DiagnosticSignal.AIQ) \n
		This command activates or deactivates the use of an internal calibration signal as input for the R&S FSW. \n
			:param signal: CALibration Uses the calibration signal as RF input. MCALibration Uses the calibration signal for the microwave range as RF input. RF Uses the signal from the RF input. AIQ Uses the Analog Baseband calibration signal as input to the optional Analog Baseband interface. This signal is only available if the R&S FSW-B71 option is installed.
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.DiagnosticSignal)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:SELect {param}')
