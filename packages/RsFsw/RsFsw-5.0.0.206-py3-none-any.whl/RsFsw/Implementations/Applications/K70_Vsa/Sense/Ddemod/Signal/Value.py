from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, signal_type: enums.DdemSignalType) -> None:
		"""SCPI: [SENSe]:DDEMod:SIGNal[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.signal.value.set(signal_type = enums.DdemSignalType.BURSted) \n
		No command help available \n
			:param signal_type: CONTinuous | BURSted
		"""
		param = Conversions.enum_scalar_to_str(signal_type, enums.DdemSignalType)
		self._core.io.write(f'SENSe:DDEMod:SIGNal:VALue {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DdemSignalType:
		"""SCPI: [SENSe]:DDEMod:SIGNal[:VALue] \n
		Snippet: value: enums.DdemSignalType = driver.applications.k70Vsa.sense.ddemod.signal.value.get() \n
		No command help available \n
			:return: signal_type: CONTinuous | BURSted"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SIGNal:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.DdemSignalType)
