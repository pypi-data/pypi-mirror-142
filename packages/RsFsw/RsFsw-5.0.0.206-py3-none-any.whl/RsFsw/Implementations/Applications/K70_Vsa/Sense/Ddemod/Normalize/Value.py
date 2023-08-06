from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:NORMalize[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.normalize.value.set(state = False) \n
		This command switches the compensation of the IQ offset and the compensation of amplitude droop on or off. Note that this
		command is maintained for compatibility reasons only. Use the more specific [SENSe:]DDEMod:NORMalize commands for new
		remote control programs (see 'Demodulation settings') . \n
			:param state: OFF | 0 No compensation for amplitude droop nor I/Q offset ON | 1 Compensation for amplitude droop and I/Q offset enabled
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:NORMalize:VALue {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:NORMalize[:VALue] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.normalize.value.get() \n
		This command switches the compensation of the IQ offset and the compensation of amplitude droop on or off. Note that this
		command is maintained for compatibility reasons only. Use the more specific [SENSe:]DDEMod:NORMalize commands for new
		remote control programs (see 'Demodulation settings') . \n
			:return: state: OFF | 0 No compensation for amplitude droop nor I/Q offset ON | 1 Compensation for amplitude droop and I/Q offset enabled"""
		response = self._core.io.query_str(f'SENSe:DDEMod:NORMalize:VALue?')
		return Conversions.str_to_bool(response)
