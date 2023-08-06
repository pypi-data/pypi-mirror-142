from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccount:
	"""Ccount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccount", core, parent)

	def get(self, relay: enums.Relay) -> int:
		"""SCPI: DIAGnostic:INFO:CCOunt \n
		Snippet: value: int = driver.diagnostic.info.ccount.get(relay = enums.Relay.AC_enable) \n
		This command queries how many switching cycles the individual relays have performed since they were installed. \n
			:param relay: ATT5 Mechanical Attenuation 05 DB ATT10 Mechanical Attenuation 10 DB ATT20 Mechanical Attenuation 20 DB ATT40 Mechanical Attenuation 40 DB CAL Mechanical Calibration Source ACDC Mechanical Attenuation Coupling PREamp Preamplifier Bypass PRES Preselector 1: PRESEL RFAB Preselector 1: RFAB PRE Preselector 1: PREAMP30MHZ ATT Preselector 1: ATTINPUT2 INP Preselector 1: INPUT2 EXT_ Preselector 2: EXT_RELAIS
			:return: cycles: Number of switching cycles."""
		param = Conversions.enum_scalar_to_str(relay, enums.Relay)
		response = self._core.io.query_str(f'DIAGnostic:INFO:CCOunt? {param}')
		return Conversions.str_to_int(response)
