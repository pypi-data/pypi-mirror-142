from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdError:
	"""FdError commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdError", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:NORMalize:FDERror \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.normalize.fdError.set(state = False) \n
		This command defines whether the deviation error is compensated for when calculating the frequency error for FSK
		modulation. \n
			:param state: ON | 1 Scales the reference signal to the actual deviation of the measurement signal. OFF | 0 Uses the entered nominal deviation for the reference signal.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:NORMalize:FDERror {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:NORMalize:FDERror \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.normalize.fdError.get() \n
		This command defines whether the deviation error is compensated for when calculating the frequency error for FSK
		modulation. \n
			:return: state: ON | 1 Scales the reference signal to the actual deviation of the measurement signal. OFF | 0 Uses the entered nominal deviation for the reference signal."""
		response = self._core.io.query_str(f'SENSe:DDEMod:NORMalize:FDERror?')
		return Conversions.str_to_bool(response)
