from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Src:
	"""Src commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("src", core, parent)

	def set(self, source: enums.PayloadLenSource) -> None:
		"""SCPI: CONFigure:WLAN:PAYLoad:LENGth:SRC \n
		Snippet: driver.applications.k91Wlan.configure.wlan.payload.length.src.set(source = enums.PayloadLenSource.ESTimate) \n
		Defines which payload length is used to determine the minimum or maximum number of required data symbols (IEEE 802.11n,
		ac) . \n
			:param source: ESTimate | HTSignal | LSIGnal | SFIeld ESTimate Uses a length estimated from the input signal HTSignal (IEEE811.02 n) Determines the length of the HT signal (from the signal field) LSIGnal (IEEE811.02 ac) Determines the length of the L signal (from the signal field)
		"""
		param = Conversions.enum_scalar_to_str(source, enums.PayloadLenSource)
		self._core.io.write(f'CONFigure:WLAN:PAYLoad:LENGth:SRC {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PayloadLenSource:
		"""SCPI: CONFigure:WLAN:PAYLoad:LENGth:SRC \n
		Snippet: value: enums.PayloadLenSource = driver.applications.k91Wlan.configure.wlan.payload.length.src.get() \n
		Defines which payload length is used to determine the minimum or maximum number of required data symbols (IEEE 802.11n,
		ac) . \n
			:return: source: ESTimate | HTSignal | LSIGnal | SFIeld ESTimate Uses a length estimated from the input signal HTSignal (IEEE811.02 n) Determines the length of the HT signal (from the signal field) LSIGnal (IEEE811.02 ac) Determines the length of the L signal (from the signal field)"""
		response = self._core.io.query_str(f'CONFigure:WLAN:PAYLoad:LENGth:SRC?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadLenSource)
