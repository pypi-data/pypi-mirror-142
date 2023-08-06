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

	def set(self, guard_interval: enums.GuardInterval) -> None:
		"""SCPI: CONFigure:WLAN:GTIMe:AUTO:TYPE \n
		Snippet: driver.applications.k91Wlan.configure.wlan.gtime.auto.typePy.set(guard_interval = enums.GuardInterval.ALL) \n
		This remote control command specifies which PPDUs are analyzed depending on their guard length if automatic detection is
		used (CONF:WLAN:GTIM:AUTO ON, see method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Auto.set) . This command is
		available for IEEE 802.11ac, ax, n, be standards only. Note: On previous Rohde & Schwarz signal and spectrum analyzers,
		this command configured both the guard interval type and the channel bandwidth. On the R&S FSW, this command only
		configures the guard type. The channel bandwidth of the PPDU to be measured must be configured separately using the
		[SENSe:]BANDwidth:CHANnel:AUTO:TYPE command. \n
			:param guard_interval: FBURst The Guard interval length of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same length (corresponds to 'Auto, same type as first PPDU') ALL All PPDUs are analyzed regardless of their guard length (corresponds to 'Auto, individually for each PPDU') . MS Only PPDUs with short guard interval length are analyzed. (corresponds to 'Meas only Short' in manual operation; MN8 | MN16 parameters in previous Rohde & Schwarz signal and spectrum analyzers) ML Only PPDUs with long guard interval length are analyzed. (corresponds to 'Meas only Long' in manual operation; ML16 | ML32 parameters in previous Rohde & Schwarz signal and spectrum analyzers) DS All PPDUs are demodulated assuming short guard interval length. (corresponds to 'Demod all as short' in manual operation; DN8 | DN16 parameters in previous Rohde & Schwarz signal and spectrum analyzers) DL All PPDUs are demodulated assuming long guard interval length. (corresponds to 'Demod all as long' in manual operation; DL16 | DL32 parameters in previous Rohde & Schwarz signal and spectrum analyzers) L1G1 Only HE/EHT PPDUs with one guard interval (GI) and one long training field (LTF) with the specified length are analyzed. Not available for HE trigger-based PPDUs. (For IEEE 802.11ax, be only; corresponds to 'Meas only 4.0µs (1x HE-LTF + 1x GI1 = 3.2 + 0.8 µs) ' in manual operation.) L1G2 Only HE/EHT PPDUs with one long training field (LTF) and two guard intervals (GI) with the specified length are analyzed. For HE trigger-based PPDUs only. (For IEEE 802.11ax, be only; corresponds to 'Meas only 4.8µs (1x HE-LTF + 2x GI1 = 3.2 + 1.6µs) ' in manual operation.) L2G1 Only HE/EHT PPDUs with two long training field (LTF) and one guard interval (GI) with the specified length are analyzed. (For IEEE 802.11ax, be only; corresponds to 'Meas only 7.2μs (2x HE-LTF + 1x GI1 = 6.4 + 0.8μs) ' in manual operation.) L2G2 Only HE/EHT PPDUs with two long training fields (LTF) and two guard intervals (GI) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 8.0μs (2x HE-LTF + 2x GI1 = 6.4 + 1.6μs) ' in manual operation.) L4G1 Only HE/EHT PPDUs with four long training fields (LTF) and one guard interval (GI) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 13.6μs (4x HE-LTF + 1x GI1 = 12.8 + 0.8μs) ' in manual operation.) L4G4 Only HE/EHT PPDUs with four guard intervals (GI) and four long training fields (LTF) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 16.0µs (4x HE-LTF + 4x GI1 = 12.8 + 3.2µs) ' in manual operation.)
		"""
		param = Conversions.enum_scalar_to_str(guard_interval, enums.GuardInterval)
		self._core.io.write(f'CONFigure:WLAN:GTIMe:AUTO:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GuardInterval:
		"""SCPI: CONFigure:WLAN:GTIMe:AUTO:TYPE \n
		Snippet: value: enums.GuardInterval = driver.applications.k91Wlan.configure.wlan.gtime.auto.typePy.get() \n
		This remote control command specifies which PPDUs are analyzed depending on their guard length if automatic detection is
		used (CONF:WLAN:GTIM:AUTO ON, see method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Auto.set) . This command is
		available for IEEE 802.11ac, ax, n, be standards only. Note: On previous Rohde & Schwarz signal and spectrum analyzers,
		this command configured both the guard interval type and the channel bandwidth. On the R&S FSW, this command only
		configures the guard type. The channel bandwidth of the PPDU to be measured must be configured separately using the
		[SENSe:]BANDwidth:CHANnel:AUTO:TYPE command. \n
			:return: guard_interval: FBURst The Guard interval length of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same length (corresponds to 'Auto, same type as first PPDU') ALL All PPDUs are analyzed regardless of their guard length (corresponds to 'Auto, individually for each PPDU') . MS Only PPDUs with short guard interval length are analyzed. (corresponds to 'Meas only Short' in manual operation; MN8 | MN16 parameters in previous Rohde & Schwarz signal and spectrum analyzers) ML Only PPDUs with long guard interval length are analyzed. (corresponds to 'Meas only Long' in manual operation; ML16 | ML32 parameters in previous Rohde & Schwarz signal and spectrum analyzers) DS All PPDUs are demodulated assuming short guard interval length. (corresponds to 'Demod all as short' in manual operation; DN8 | DN16 parameters in previous Rohde & Schwarz signal and spectrum analyzers) DL All PPDUs are demodulated assuming long guard interval length. (corresponds to 'Demod all as long' in manual operation; DL16 | DL32 parameters in previous Rohde & Schwarz signal and spectrum analyzers) L1G1 Only HE/EHT PPDUs with one guard interval (GI) and one long training field (LTF) with the specified length are analyzed. Not available for HE trigger-based PPDUs. (For IEEE 802.11ax, be only; corresponds to 'Meas only 4.0µs (1x HE-LTF + 1x GI1 = 3.2 + 0.8 µs) ' in manual operation.) L1G2 Only HE/EHT PPDUs with one long training field (LTF) and two guard intervals (GI) with the specified length are analyzed. For HE trigger-based PPDUs only. (For IEEE 802.11ax, be only; corresponds to 'Meas only 4.8µs (1x HE-LTF + 2x GI1 = 3.2 + 1.6µs) ' in manual operation.) L2G1 Only HE/EHT PPDUs with two long training field (LTF) and one guard interval (GI) with the specified length are analyzed. (For IEEE 802.11ax, be only; corresponds to 'Meas only 7.2μs (2x HE-LTF + 1x GI1 = 6.4 + 0.8μs) ' in manual operation.) L2G2 Only HE/EHT PPDUs with two long training fields (LTF) and two guard intervals (GI) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 8.0μs (2x HE-LTF + 2x GI1 = 6.4 + 1.6μs) ' in manual operation.) L4G1 Only HE/EHT PPDUs with four long training fields (LTF) and one guard interval (GI) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 13.6μs (4x HE-LTF + 1x GI1 = 12.8 + 0.8μs) ' in manual operation.) L4G4 Only HE/EHT PPDUs with four guard intervals (GI) and four long training fields (LTF) with the specified length are analyzed. (For IEEE 802.11ax,be only; corresponds to 'Meas only 16.0µs (4x HE-LTF + 4x GI1 = 12.8 + 3.2µs) ' in manual operation.)"""
		response = self._core.io.query_str(f'CONFigure:WLAN:GTIMe:AUTO:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.GuardInterval)
