from enum import Enum


# noinspection SpellCheckingInspection
class AccessType(Enum):
	"""2 Members, RO ... RW"""
	RO = 0
	RW = 1


# noinspection SpellCheckingInspection
class AcpLimitEvalMode(Enum):
	"""3 Members, ABSolute ... RELative"""
	ABSolute = 0
	OR = 1
	RELative = 2


# noinspection SpellCheckingInspection
class AcpResult(Enum):
	"""3 Members, ABSolute ... RELative"""
	ABSolute = 0
	ALL = 1
	RELative = 2


# noinspection SpellCheckingInspection
class AdemMeasType(Enum):
	"""5 Members, MIDDle ... RMS"""
	MIDDle = 0
	MPEak = 1
	NPEak = 2
	PPEak = 3
	RMS = 4


# noinspection SpellCheckingInspection
class AdjChannel(Enum):
	"""3 Members, E500 ... U384"""
	E500 = 0
	NOSBw = 1
	U384 = 2


# noinspection SpellCheckingInspection
class AdjChannelBw(Enum):
	"""10 Members, EUTRa ... UTRa768"""
	EUTRa = 0
	N1GSm = 1
	N1UTra = 2
	STANdalone = 3
	U128 = 4
	U384 = 5
	U768 = 6
	UTRa128 = 7
	UTRa384 = 8
	UTRa768 = 9


# noinspection SpellCheckingInspection
class AdjustAlignment(Enum):
	"""3 Members, CENTer ... RIGHt"""
	CENTer = 0
	LEFT = 1
	RIGHt = 2


# noinspection SpellCheckingInspection
class AllocationContent(Enum):
	"""6 Members, NONE ... PUSCh"""
	NONE = 0
	PACC = 1
	PSCC = 2
	PUACh = 3
	PUCCh = 4
	PUSCh = 5


# noinspection SpellCheckingInspection
class AllocMapping(Enum):
	"""19 Members, LC101 ... LC91"""
	LC101 = 0
	LC11 = 1
	LC111 = 2
	LC121 = 3
	LC21 = 4
	LC22 = 5
	LC31 = 6
	LC32 = 7
	LC41 = 8
	LC42 = 9
	LC51 = 10
	LC52 = 11
	LC61 = 12
	LC62 = 13
	LC71 = 14
	LC72 = 15
	LC81 = 16
	LC82 = 17
	LC91 = 18


# noinspection SpellCheckingInspection
class AllocType(Enum):
	"""2 Members, DATA ... UNUSed"""
	DATA = 0
	UNUSed = 1


# noinspection SpellCheckingInspection
class AmPmDef(Enum):
	"""2 Members, MREF ... REFMeas"""
	MREF = 0
	REFMeas = 1


# noinspection SpellCheckingInspection
class AnalysisModeUl(Enum):
	"""4 Members, NPRach ... PUSCh"""
	NPRach = 0
	NPUSch = 1
	PRACh = 2
	PUSCh = 3


# noinspection SpellCheckingInspection
class AngleUnit(Enum):
	"""2 Members, DEG ... RAD"""
	DEG = 0
	RAD = 1


# noinspection SpellCheckingInspection
class AnnotationMode(Enum):
	"""2 Members, CSPan ... SSTop"""
	CSPan = 0
	SSTop = 1


# noinspection SpellCheckingInspection
class AntennaA(Enum):
	"""16 Members, ANT1 ... ANTenna8"""
	ANT1 = 0
	ANT2 = 1
	ANT3 = 2
	ANT4 = 3
	ANT5 = 4
	ANT6 = 5
	ANT7 = 6
	ANT8 = 7
	ANTenna1 = 8
	ANTenna2 = 9
	ANTenna3 = 10
	ANTenna4 = 11
	ANTenna5 = 12
	ANTenna6 = 13
	ANTenna7 = 14
	ANTenna8 = 15


# noinspection SpellCheckingInspection
class AntennaB(Enum):
	"""6 Members, ALL ... NONE"""
	ALL = 0
	ANT1 = 1
	ANT2 = 2
	ANT3 = 3
	ANT4 = 4
	NONE = 5


# noinspection SpellCheckingInspection
class AntennaC(Enum):
	"""9 Members, ALL ... AUTO"""
	ALL = 0
	ANT1 = 1
	ANT2 = 2
	ANT3 = 3
	ANT4 = 4
	AUT1 = 5
	AUT2 = 6
	AUT4 = 7
	AUTO = 8


# noinspection SpellCheckingInspection
class AntennaD(Enum):
	"""5 Members, ALL ... ANT4"""
	ALL = 0
	ANT1 = 1
	ANT2 = 2
	ANT3 = 3
	ANT4 = 4


# noinspection SpellCheckingInspection
class AntennaPortA(Enum):
	"""9 Members, ALL ... AP_9"""
	ALL = 0
	AP_10 = 1
	AP_11 = 2
	AP_12 = 3
	AP_13 = 4
	AP_14 = 5
	AP_5_7 = 6
	AP_8 = 7
	AP_9 = 8


# noinspection SpellCheckingInspection
class AntennaPortB(Enum):
	"""9 Members, ALL ... AP_22"""
	ALL = 0
	AP_15 = 1
	AP_16 = 2
	AP_17 = 3
	AP_18 = 4
	AP_19 = 5
	AP_20 = 6
	AP_21 = 7
	AP_22 = 8


# noinspection SpellCheckingInspection
class AntennaPortC(Enum):
	"""5 Members, ALL ... AP_3"""
	ALL = 0
	AP_0 = 1
	AP_1 = 2
	AP_2 = 3
	AP_3 = 4


# noinspection SpellCheckingInspection
class AntennaPorts(Enum):
	"""3 Members, AP1 ... AP4"""
	AP1 = 0
	AP2 = 1
	AP4 = 2


# noinspection SpellCheckingInspection
class AntennaPortsLte(Enum):
	"""4 Members, TX1 ... TX8"""
	TX1 = 0
	TX2 = 1
	TX4 = 2
	TX8 = 3


# noinspection SpellCheckingInspection
class AntennasCount(Enum):
	"""8 Members, TX1 ... TX8"""
	TX1 = 0
	TX2 = 1
	TX3 = 2
	TX4 = 3
	TX5 = 4
	TX6 = 5
	TX7 = 6
	TX8 = 7


# noinspection SpellCheckingInspection
class AttenuatorMode(Enum):
	"""3 Members, LDIStortion ... NORMal"""
	LDIStortion = 0
	LNOise = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class AutoDemodType(Enum):
	"""3 Members, ALL ... SCON"""
	ALL = 0
	OFF = 1
	SCON = 2


# noinspection SpellCheckingInspection
class AutoFixRange(Enum):
	"""3 Members, LOWer ... UPPer"""
	LOWer = 0
	NONE = 1
	UPPer = 2


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class AutoManualUserMode(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	MANual = 1
	USER = 2


# noinspection SpellCheckingInspection
class AutoMode(Enum):
	"""3 Members, AUTO ... ON"""
	AUTO = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class AutoOrOff(Enum):
	"""2 Members, AUTO ... OFF"""
	AUTO = 0
	OFF = 1


# noinspection SpellCheckingInspection
class AutoscaleMode(Enum):
	"""3 Members, ALL ... ONCE"""
	ALL = 0
	DEFault = 1
	ONCE = 2


# noinspection SpellCheckingInspection
class AverageModeA(Enum):
	"""3 Members, LINear ... POWer"""
	LINear = 0
	LOGarithmic = 1
	POWer = 2


# noinspection SpellCheckingInspection
class AverageModeB(Enum):
	"""6 Members, LINear ... VIDeo"""
	LINear = 0
	LOGarithmic = 1
	MAXimum = 2
	POWer = 3
	SCALar = 4
	VIDeo = 5


# noinspection SpellCheckingInspection
class AverageModeC(Enum):
	"""3 Members, LINear ... VIDeo"""
	LINear = 0
	POWer = 1
	VIDeo = 2


# noinspection SpellCheckingInspection
class AverageModeD(Enum):
	"""5 Members, LINear ... VIDeo"""
	LINear = 0
	MAXimum = 1
	POWer = 2
	SCALar = 3
	VIDeo = 4


# noinspection SpellCheckingInspection
class AveragingMode(Enum):
	"""2 Members, PALL ... TGPP"""
	PALL = 0
	TGPP = 1


# noinspection SpellCheckingInspection
class AxesUnits(Enum):
	"""2 Members, CARRier ... HZ"""
	CARRier = 0
	HZ = 1


# noinspection SpellCheckingInspection
class AxisFmSettling(Enum):
	"""3 Members, FMSLength ... FMSTime"""
	FMSLength = 0
	FMSPoint = 1
	FMSTime = 2


# noinspection SpellCheckingInspection
class AxisFreqFmItems(Enum):
	"""6 Members, AVGFm ... RMSFm"""
	AVGFm = 0
	FMERror = 1
	FREQuency = 2
	MAXFm = 3
	RELFrequency = 4
	RMSFm = 5


# noinspection SpellCheckingInspection
class AxisFreqItems(Enum):
	"""9 Members, AVGFm ... RMSNonlinear"""
	AVGFm = 0
	AVGNonlinear = 1
	BWIDth = 2
	CHERror = 3
	FREQuency = 4
	MAXFm = 5
	MAXNonlinear = 6
	RMSFm = 7
	RMSNonlinear = 8


# noinspection SpellCheckingInspection
class AxisHopState(Enum):
	"""2 Members, INDex ... STAFrequency"""
	INDex = 0
	STAFrequency = 1


# noinspection SpellCheckingInspection
class AxisHopTiming(Enum):
	"""3 Members, BEGin ... SWITching"""
	BEGin = 0
	DWELl = 1
	SWITching = 2


# noinspection SpellCheckingInspection
class AxisIndex(Enum):
	"""1 Members, INDex ... INDex"""
	INDex = 0


# noinspection SpellCheckingInspection
class AxisPhase(Enum):
	"""3 Members, AVPHm ... RMSPm"""
	AVPHm = 0
	MXPHm = 1
	RMSPm = 2


# noinspection SpellCheckingInspection
class AxisPower(Enum):
	"""4 Members, AVGPower ... PWRRipple"""
	AVGPower = 0
	MAXPower = 1
	MINPower = 2
	PWRRipple = 3


# noinspection SpellCheckingInspection
class AxisTimingItems(Enum):
	"""3 Members, BEGin ... RATE"""
	BEGin = 0
	LENGth = 1
	RATE = 2


# noinspection SpellCheckingInspection
class Band(Enum):
	"""14 Members, A ... Y"""
	A = 0
	D = 1
	E = 2
	F = 3
	G = 4
	J = 5
	K = 6
	KA = 7
	Q = 8
	U = 9
	USER = 10
	V = 11
	W = 12
	Y = 13


# noinspection SpellCheckingInspection
class BandB(Enum):
	"""12 Members, D ... Y"""
	D = 0
	E = 1
	F = 2
	G = 3
	J = 4
	KA = 5
	Q = 6
	U = 7
	USER = 8
	V = 9
	W = 10
	Y = 11


# noinspection SpellCheckingInspection
class BandwidthChRaster(Enum):
	"""2 Members, C100 ... C15"""
	C100 = 0
	C15 = 1


# noinspection SpellCheckingInspection
class BandwidthLteA(Enum):
	"""9 Members, B1010 ... USER"""
	B1010 = 0
	B1015 = 1
	B1020 = 2
	B1515 = 3
	B1520 = 4
	B2020 = 5
	B510 = 6
	B520 = 7
	USER = 8


# noinspection SpellCheckingInspection
class BandwidthLteB(Enum):
	"""6 Members, BW1_40 ... BW5_00"""
	BW1_40 = 0
	BW10_00 = 1
	BW15_00 = 2
	BW20_00 = 3
	BW3_00 = 4
	BW5_00 = 5


# noinspection SpellCheckingInspection
class BandwidthLteC(Enum):
	"""8 Members, BW1_40 ... NB_6rb"""
	BW1_40 = 0
	BW10_00 = 1
	BW15_00 = 2
	BW20_00 = 3
	BW3_00 = 4
	BW5_00 = 5
	NB_1rb = 6
	NB_6rb = 7


# noinspection SpellCheckingInspection
class BandwidthNr5G(Enum):
	"""20 Members, BW10 ... BW90"""
	BW10 = 0
	BW100 = 1
	BW15 = 2
	BW1600 = 3
	BW20 = 4
	BW200 = 5
	BW2000 = 6
	BW25 = 7
	BW30 = 8
	BW35 = 9
	BW40 = 10
	BW400 = 11
	BW45 = 12
	BW5 = 13
	BW50 = 14
	BW60 = 15
	BW70 = 16
	BW80 = 17
	BW800 = 18
	BW90 = 19


# noinspection SpellCheckingInspection
class BbInputSource(Enum):
	"""4 Members, AIQ ... RF"""
	AIQ = 0
	DIQ = 1
	FIQ = 2
	RF = 3


# noinspection SpellCheckingInspection
class BbOrRf(Enum):
	"""2 Members, BB ... RF"""
	BB = 0
	RF = 1


# noinspection SpellCheckingInspection
class BerRateFormat(Enum):
	"""17 Members, CURRent ... TTOTal"""
	CURRent = 0
	DSINdex = 1
	MAX = 2
	MIN = 3
	SECurrent = 4
	SEMax = 5
	SEMin = 6
	SETotal = 7
	TCURrent = 8
	TECurrent = 9
	TEMax = 10
	TEMin = 11
	TETotal = 12
	TMAX = 13
	TMIN = 14
	TOTal = 15
	TTOTal = 16


# noinspection SpellCheckingInspection
class BitstreamFormat(Enum):
	"""2 Members, HEXadecimal ... OCTet"""
	HEXadecimal = 0
	OCTet = 1


# noinspection SpellCheckingInspection
class BitstreamUnit(Enum):
	"""4 Members, BIT ... SYMBols"""
	BIT = 0
	BITS = 1
	SYM = 2
	SYMBols = 3


# noinspection SpellCheckingInspection
class BstreamUnit(Enum):
	"""2 Members, BIT ... SYM"""
	BIT = 0
	SYM = 1


# noinspection SpellCheckingInspection
class BsType(Enum):
	"""4 Members, FR1C ... FR2O"""
	FR1C = 0
	FR1H = 1
	FR1O = 2
	FR2O = 3


# noinspection SpellCheckingInspection
class BurstMode(Enum):
	"""2 Members, BURS ... MEAS"""
	BURS = 0
	MEAS = 1


# noinspection SpellCheckingInspection
class BurstSetPeriodicity(Enum):
	"""7 Members, AUTO ... MS80"""
	AUTO = 0
	MS05 = 1
	MS10 = 2
	MS160 = 3
	MS20 = 4
	MS40 = 5
	MS80 = 6


# noinspection SpellCheckingInspection
class BurstUnit(Enum):
	"""2 Members, SAMPle ... SYMBol"""
	SAMPle = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class CalculationLteEvm(Enum):
	"""2 Members, OTP ... TGPP"""
	OTP = 0
	TGPP = 1


# noinspection SpellCheckingInspection
class CalibrationScope(Enum):
	"""4 Members, ACLear ... ON"""
	ACLear = 0
	ALL = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class CalibrationState(Enum):
	"""3 Members, EXPired ... OK"""
	EXPired = 0
	NAN = 1
	OK = 2


# noinspection SpellCheckingInspection
class CarriersAnalyze(Enum):
	"""2 Members, ALL ... VIEWed"""
	ALL = 0
	VIEWed = 1


# noinspection SpellCheckingInspection
class CcSlot(Enum):
	"""4 Members, ALL ... SINGle"""
	ALL = 0
	S0 = 1
	S1 = 2
	SINGle = 3


# noinspection SpellCheckingInspection
class CdmType(Enum):
	"""4 Members, CDM4 ... NOCDm"""
	CDM4 = 0
	CDM8 = 1
	FDCDm2 = 2
	NOCDm = 3


# noinspection SpellCheckingInspection
class CestMode(Enum):
	"""3 Members, CARRiers ... OFFSet"""
	CARRiers = 0
	OFF = 1
	OFFSet = 2


# noinspection SpellCheckingInspection
class CestTransmType(Enum):
	"""2 Members, OWAY ... TWAY"""
	OWAY = 0
	TWAY = 1


# noinspection SpellCheckingInspection
class ChannelBandwidth(Enum):
	"""8 Members, BW10 ... BW80"""
	BW10 = 0
	BW160 = 1
	BW2_5 = 2
	BW20 = 3
	BW320 = 4
	BW40 = 5
	BW5 = 6
	BW80 = 7


# noinspection SpellCheckingInspection
class ChannelEstDl(Enum):
	"""4 Members, OFF ... TGPP"""
	OFF = 0
	PIL = 1
	PILPay = 2
	TGPP = 3


# noinspection SpellCheckingInspection
class ChannelEstimation(Enum):
	"""5 Members, LINT ... TGPP"""
	LINT = 0
	NORMal = 1
	OFF = 2
	PILPay = 3
	TGPP = 4


# noinspection SpellCheckingInspection
class ChannelEstUl(Enum):
	"""2 Members, PIL ... PILPay"""
	PIL = 0
	PILPay = 1


# noinspection SpellCheckingInspection
class ChannelNumber(Enum):
	"""16 Members, C0 ... C9"""
	C0 = 0
	C1 = 1
	C10 = 2
	C11 = 3
	C12 = 4
	C13 = 5
	C14 = 6
	C15 = 7
	C2 = 8
	C3 = 9
	C4 = 10
	C5 = 11
	C6 = 12
	C7 = 13
	C8 = 14
	C9 = 15


# noinspection SpellCheckingInspection
class ChannelType(Enum):
	"""31 Members, IqAnalyzer ... SpectrumAnalyzer"""
	IqAnalyzer = "IQ"
	K10_Gsm = "GSM"
	K106_NbIot = "NIOT"
	K10x_Lte = "LTE"
	K118_Verizon5G = "V5GT"
	K14x_5GnewRadio = "NR5G"
	K15_Avionics = "AVIonics"
	K17_MultiCarrierGroupDelay = "MCGD"
	K18_AmplifierMeas = "AMPLifier"
	K192_193_Docsis31 = "DOCSis"
	K201_OneWeb = "OWEB"
	K30_Noise = "NOISE"
	K40_PhaseNoise = "PNOISE"
	K50_FastSpurSearch = "SPUR"
	K6_PulseAnalysis = "PULSE"
	K60_TransientAnalysis = "TA"
	K7_AnalogModulation = "ADEM"
	K70_VectorSignalAnalyzer = "DDEM"
	K72_3GppFddBts = "BWCD"
	K73_3GppFddUe = "MWCD"
	K76_TdScdmaBts = "BTDS"
	K77_TdScdmaUe = "MTDS"
	K82_Cdma2000Bts = "BC2K"
	K83_Cdma2000Ms = "MC2K"
	K84_EvdoBts = "BDO"
	K85_EvdoMs = "MDO"
	K91_Wlan = "WLAN"
	K95_80211ad = "WIGIG"
	K97_80211ay = "EDMG"
	RealTimeSpectrum = "RTIM"
	SpectrumAnalyzer = "SANALYZER"


# noinspection SpellCheckingInspection
class ChannelTypeResults(Enum):
	"""2 Members, EFFective ... PHYSical"""
	EFFective = 0
	PHYSical = 1


# noinspection SpellCheckingInspection
class CheckResult(Enum):
	"""2 Members, FAILED ... PASSED"""
	FAILED = 0
	PASSED = 1


# noinspection SpellCheckingInspection
class ChirpXaxisItems(Enum):
	"""23 Members, AVGFm ... RMSPm"""
	AVGFm = 0
	AVGNonlinear = 1
	AVGPower = 2
	AVPHm = 3
	BEGin = 4
	CHERror = 5
	FMSLength = 6
	FMSPoint = 7
	FMSTime = 8
	FREQuency = 9
	INDex = 10
	MAXFm = 11
	MAXNonlinear = 12
	MAXPower = 13
	MINPower = 14
	MXPHm = 15
	PMSLength = 16
	PMSPoint = 17
	PMSTime = 18
	PWRRipple = 19
	RMSFm = 20
	RMSNonlinear = 21
	RMSPm = 22


# noinspection SpellCheckingInspection
class ChrTableHeaders(Enum):
	"""27 Members, ALL ... STATe"""
	ALL = 0
	AVGFm = 1
	AVGNonlinear = 2
	AVGPower = 3
	AVPHm = 4
	BEGin = 5
	BWIDth = 6
	CHERror = 7
	FMSLength = 8
	FMSPoint = 9
	FMSTime = 10
	FREQuency = 11
	LENGth = 12
	MAXFm = 13
	MAXNonlinear = 14
	MAXPower = 15
	MINPower = 16
	MXPHm = 17
	PMSLength = 18
	PMSPoint = 19
	PMSTime = 20
	PWRRipple = 21
	RATE = 22
	RMSFm = 23
	RMSNonlinear = 24
	RMSPm = 25
	STATe = 26


# noinspection SpellCheckingInspection
class Color(Enum):
	"""16 Members, BLACk ... YELLow"""
	BLACk = 0
	BLUE = 1
	BROWn = 2
	CYAN = 3
	DGRay = 4
	GREen = 5
	LBLue = 6
	LCYan = 7
	LGRay = 8
	LGReen = 9
	LMAGenta = 10
	LRED = 11
	MAGenta = 12
	RED = 13
	WHITe = 14
	YELLow = 15


# noinspection SpellCheckingInspection
class ColorSchemeA(Enum):
	"""5 Members, COLD ... RADar"""
	COLD = 0
	COLor = 1
	GRAYscale = 2
	HOT = 3
	RADar = 4


# noinspection SpellCheckingInspection
class ColorSchemeB(Enum):
	"""4 Members, COLD ... RADar"""
	COLD = 0
	GRAYscale = 1
	HOT = 2
	RADar = 3


# noinspection SpellCheckingInspection
class CompatibilityMode(Enum):
	"""9 Members, ATT ... FSW"""
	ATT = 0
	DEFault = 1
	FSET = 2
	FSL = 3
	FSP = 4
	FSQ = 5
	FSU = 6
	FSV = 7
	FSW = 8


# noinspection SpellCheckingInspection
class Complexity(Enum):
	"""2 Members, ENHanced ... SIMPle"""
	ENHanced = 0
	SIMPle = 1


# noinspection SpellCheckingInspection
class ComponentType(Enum):
	"""4 Members, AMPLifier ... MULTiplier"""
	AMPLifier = 0
	DIVider = 1
	MIXer = 2
	MULTiplier = 3


# noinspection SpellCheckingInspection
class ConfigMode(Enum):
	"""2 Members, DEFault ... USER"""
	DEFault = 0
	USER = 1


# noinspection SpellCheckingInspection
class ControlState(Enum):
	"""3 Members, ERRor ... SUCCessful"""
	ERRor = 0
	OFF = 1
	SUCCessful = 2


# noinspection SpellCheckingInspection
class CopyLogicMode(Enum):
	"""2 Members, CUSTom ... SLOTs"""
	CUSTom = 0
	SLOTs = 1


# noinspection SpellCheckingInspection
class CorrectionMeasType(Enum):
	"""2 Members, OPEN ... THRough"""
	OPEN = 0
	THRough = 1


# noinspection SpellCheckingInspection
class CorrectionMethod(Enum):
	"""2 Members, REFLexion ... TRANsmission"""
	REFLexion = 0
	TRANsmission = 1


# noinspection SpellCheckingInspection
class CorrectionMode(Enum):
	"""2 Members, SPOT ... TABLe"""
	SPOT = 0
	TABLe = 1


# noinspection SpellCheckingInspection
class CorsetDataSelect(Enum):
	"""3 Members, ALL0 ... PN23"""
	ALL0 = 0
	AUTO = 1
	PN23 = 2


# noinspection SpellCheckingInspection
class Counter(Enum):
	"""2 Members, CAPTure ... STATistics"""
	CAPTure = 0
	STATistics = 1


# noinspection SpellCheckingInspection
class CouplingAmplitude(Enum):
	"""4 Members, AUTO ... PRIMary"""
	AUTO = 0
	MASTer = 1
	OFF = 2
	PRIMary = 3


# noinspection SpellCheckingInspection
class CouplingRlevel(Enum):
	"""3 Members, MANual ... PRIMary"""
	MANual = 0
	MASTer = 1
	PRIMary = 2


# noinspection SpellCheckingInspection
class CouplingRosc(Enum):
	"""3 Members, AUTO ... OFF"""
	AUTO = 0
	EXTernal = 1
	OFF = 2


# noinspection SpellCheckingInspection
class CouplingTypeA(Enum):
	"""2 Members, AC ... DC"""
	AC = 0
	DC = 1


# noinspection SpellCheckingInspection
class CouplingTypeB(Enum):
	"""3 Members, AC ... DCLimit"""
	AC = 0
	DC = 1
	DCLimit = 2


# noinspection SpellCheckingInspection
class CsdSyncMethod(Enum):
	"""2 Members, APPLy ... IGNore"""
	APPLy = 0
	IGNore = 1


# noinspection SpellCheckingInspection
class CycPrefixType(Enum):
	"""3 Members, EXT ... NORM"""
	EXT = 0
	MNEM = 1
	NORM = 2


# noinspection SpellCheckingInspection
class DataExportMode(Enum):
	"""2 Members, RAW ... TRACe"""
	RAW = 0
	TRACe = 1


# noinspection SpellCheckingInspection
class DataFormat(Enum):
	"""10 Members, ASCii ... UINT_cma_64"""
	ASCii = 0
	MATLAB_cma_16 = 1
	MATLAB_cma_32 = 2
	MATLAB_cma_64 = 3
	Real16 = "REAL,16"
	Real32 = "REAL,32"
	Real64 = "REAL,64"
	UINT_cma_16 = 7
	UINT_cma_32 = 8
	UINT_cma_64 = 9


# noinspection SpellCheckingInspection
class DataSourceLocation(Enum):
	"""2 Members, AMD ... BMD"""
	AMD = 0
	BMD = 1


# noinspection SpellCheckingInspection
class DciField(Enum):
	"""73 Members, AINDicator ... ZCRTrigger"""
	AINDicator = 0
	APORts = 1
	ARBSet = 2
	BOINdicator = 3
	BPINdicator = 4
	CACPext = 5
	CAPC = 6
	CARRier = 7
	CBGFi = 8
	CBGTi = 9
	CINDication = 10
	CLINdicator = 11
	COTDuration = 12
	CSIRequest = 13
	DAI1 = 14
	DAI2 = 15
	DFIFlag = 16
	DSINit = 17
	FDRassign = 18
	FHFLag = 19
	HABitmap = 20
	HPNumber = 21
	IFDFormats = 22
	ISPindicator = 23
	LOSFn = 24
	M = 25
	MASoffset = 26
	MCS1 = 27
	MCS2 = 28
	MGFLag = 29
	N = 30
	N1 = 31
	N2 = 32
	NDI1 = 33
	NDI2 = 34
	NFINdicator = 35
	NRPGroup = 36
	OHARequest = 37
	OPCParam = 38
	PBITs = 39
	PBSindicator = 40
	PDASso = 41
	PEINdication = 42
	PGINdex = 43
	PHFTiming = 44
	PINDicator = 45
	PINLayers = 46
	PMINdex = 47
	PRINdicator = 48
	RAPindex = 49
	RBITs = 50
	RMINdicator = 51
	RV1 = 52
	RV2 = 53
	SDINdication = 54
	SDINdicator = 55
	SFINdicator = 56
	SIINdicator = 57
	SMESsage = 58
	SMINdicator = 59
	SPINdex = 60
	SRINdicator = 61
	SRSRequest = 62
	TBSCaling = 63
	TCINdication = 64
	TCSPusch = 65
	TDRassign = 66
	TPCCommand = 67
	USCH = 68
	USUL = 69
	VTPMapping = 70
	WUINdication = 71
	ZCRTrigger = 72


# noinspection SpellCheckingInspection
class DciScope(Enum):
	"""2 Members, ICDF ... SPUS"""
	ICDF = 0
	SPUS = 1


# noinspection SpellCheckingInspection
class DdemGroup(Enum):
	"""8 Members, APSK ... UQAM"""
	APSK = 0
	ASK = 1
	FSK = 2
	MSK = 3
	PSK = 4
	QAM = 5
	QPSK = 6
	UQAM = 7


# noinspection SpellCheckingInspection
class DdemodFilter(Enum):
	"""13 Members, A25Fm ... RRCosine"""
	A25Fm = 0
	B22 = 1
	B25 = 2
	B44 = 3
	EMES = 4
	EREF = 5
	GAUSsian = 6
	QFM = 7
	QFR = 8
	QRM = 9
	QRR = 10
	RCOSine = 11
	RRCosine = 12


# noinspection SpellCheckingInspection
class DdemResultType(Enum):
	"""20 Members, ADR ... RHO"""
	ADR = 0
	DEV = 1
	DTTS = 2
	EVPK = 3
	EVPS = 4
	EVRM = 5
	FEPK = 6
	FERR = 7
	FSPK = 8
	FSPS = 9
	FSRM = 10
	IQIM = 11
	IQOF = 12
	MEPK = 13
	MEPS = 14
	MERM = 15
	PEPK = 16
	PEPS = 17
	PERM = 18
	RHO = 19


# noinspection SpellCheckingInspection
class DdemSignalType(Enum):
	"""2 Members, BURSted ... CONTinuous"""
	BURSted = 0
	CONTinuous = 1


# noinspection SpellCheckingInspection
class DdpdResult(Enum):
	"""4 Members, ACB1 ... EVM"""
	ACB1 = 0
	ACL1 = 1
	ACU1 = 2
	EVM = 3


# noinspection SpellCheckingInspection
class DemodDataSelect(Enum):
	"""3 Members, ADEScramble ... DPData"""
	ADEScramble = 0
	BDEScramble = 1
	DPData = 2


# noinspection SpellCheckingInspection
class DemodInterpolation(Enum):
	"""2 Members, LINear ... WIENer"""
	LINear = 0
	WIENer = 1


# noinspection SpellCheckingInspection
class DensityConf(Enum):
	"""4 Members, DEN1 ... ODD"""
	DEN1 = 0
	DEN3 = 1
	EVEN = 2
	ODD = 3


# noinspection SpellCheckingInspection
class DeploymentFrange(Enum):
	"""4 Members, EHIGh ... MIDDle"""
	EHIGh = 0
	HIGH = 1
	LOW = 2
	MIDDle = 3


# noinspection SpellCheckingInspection
class Detect(Enum):
	"""2 Members, DETected ... NDETected"""
	DETected = 0
	NDETected = 1


# noinspection SpellCheckingInspection
class Detector(Enum):
	"""7 Members, APEak ... SAMPle"""
	APEak = 0
	AVERage = 1
	NEGative = 2
	POSitive = 3
	QPEak = 4
	RMS = 5
	SAMPle = 6


# noinspection SpellCheckingInspection
class DetectorA(Enum):
	"""8 Members, ACSine ... QPEak"""
	ACSine = 0
	ACVideo = 1
	AVERage = 2
	CAVerage = 3
	CRMS = 4
	OFF = 5
	POSitive = 6
	QPEak = 7


# noinspection SpellCheckingInspection
class DetectorB(Enum):
	"""13 Members, ACSine ... SMP"""
	ACSine = 0
	ACVideo = 1
	APEak = 2
	AVERage = 3
	CAVerage = 4
	CRMS = 5
	NEGative = 6
	NRM = 7
	POSitive = 8
	QPEak = 9
	RMS = 10
	SAMPle = 11
	SMP = 12


# noinspection SpellCheckingInspection
class DetectorC(Enum):
	"""8 Members, ACSine ... SAMPle"""
	ACSine = 0
	ACVideo = 1
	APEak = 2
	AVERage = 3
	NEGative = 4
	POSitive = 5
	RMS = 6
	SAMPle = 7


# noinspection SpellCheckingInspection
class DetectorD(Enum):
	"""5 Members, AVERage ... SAMPle"""
	AVERage = 0
	NEGative = 1
	POSitive = 2
	RMS = 3
	SAMPle = 4


# noinspection SpellCheckingInspection
class DetectorE(Enum):
	"""4 Members, AVERage ... POSitive"""
	AVERage = 0
	NEGative = 1
	NONE = 2
	POSitive = 3


# noinspection SpellCheckingInspection
class DetectorF(Enum):
	"""5 Members, APE ... SAMPle"""
	APE = 0
	AVERage = 1
	NEGative = 2
	POSitive = 3
	SAMPle = 4


# noinspection SpellCheckingInspection
class DetectReference(Enum):
	"""4 Members, ABSolute ... RLEVel"""
	ABSolute = 0
	NOISe = 1
	PEAK = 2
	RLEVel = 3


# noinspection SpellCheckingInspection
class DetectReferenceB(Enum):
	"""4 Members, ABSolute ... REFLevel"""
	ABSolute = 0
	NOISe = 1
	PEAK = 2
	REFLevel = 3


# noinspection SpellCheckingInspection
class DiagnosticSignal(Enum):
	"""8 Members, AIQ ... WBCal"""
	AIQ = 0
	CALibration = 1
	EMI = 2
	MCALibration = 3
	RF = 4
	SYNThtwo = 5
	TG = 6
	WBCal = 7


# noinspection SpellCheckingInspection
class DiqUnit(Enum):
	"""8 Members, AMPere ... WATT"""
	AMPere = 0
	DBM = 1
	DBMV = 2
	DBPW = 3
	DBUA = 4
	DBUV = 5
	VOLT = 6
	WATT = 7


# noinspection SpellCheckingInspection
class DisplayFormat(Enum):
	"""2 Members, SINGle ... SPLit"""
	SINGle = 0
	SPLit = 1


# noinspection SpellCheckingInspection
class DisplayPosition(Enum):
	"""3 Members, BOTTom ... TOP"""
	BOTTom = 0
	OFF = 1
	TOP = 2


# noinspection SpellCheckingInspection
class DisplayType(Enum):
	"""4 Members, BOTH ... TIME"""
	BOTH = 0
	NONE = 1
	SPECtrum = 2
	TIME = 3


# noinspection SpellCheckingInspection
class DlUlDirection(Enum):
	"""2 Members, DL ... UL"""
	DL = 0
	UL = 1


# noinspection SpellCheckingInspection
class DmrsReference(Enum):
	"""2 Members, CSTart ... RPA"""
	CSTart = 0
	RPA = 1


# noinspection SpellCheckingInspection
class DmrsReferencePoint(Enum):
	"""2 Members, BWPStart ... RPA"""
	BWPStart = 0
	RPA = 1


# noinspection SpellCheckingInspection
class DmRsSeqGenMethod(Enum):
	"""3 Members, NIDCell ... NIDPusch"""
	NIDCell = 0
	NIDDmrs = 1
	NIDPusch = 2


# noinspection SpellCheckingInspection
class DmRsSeqGenMethodB(Enum):
	"""3 Members, NIDCell ... NIDPusch"""
	NIDCell = 0
	NIDNscid = 1
	NIDPusch = 2


# noinspection SpellCheckingInspection
class DotStyle(Enum):
	"""4 Members, AUTO ... LINes"""
	AUTO = 0
	DLINes = 1
	DOTS = 2
	LINes = 3


# noinspection SpellCheckingInspection
class DpdMethod(Enum):
	"""2 Members, GENerator ... WFILe"""
	GENerator = 0
	WFILe = 1


# noinspection SpellCheckingInspection
class DpdOrder(Enum):
	"""2 Members, AMFirst ... PMFirst"""
	AMFirst = 0
	PMFirst = 1


# noinspection SpellCheckingInspection
class DuplexingLte(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	LAA = 1
	TDD = 2


# noinspection SpellCheckingInspection
class Duration(Enum):
	"""3 Members, LONG ... SHORt"""
	LONG = 0
	NORMal = 1
	SHORt = 2


# noinspection SpellCheckingInspection
class DutSize(Enum):
	"""3 Members, DUT15 ... NONE"""
	DUT15 = 0
	DUT30 = 1
	NONE = 2


# noinspection SpellCheckingInspection
class DutType(Enum):
	"""4 Members, AMPLifier ... UPConv"""
	AMPLifier = 0
	DDOWnconv = 1
	DOWNconv = 2
	UPConv = 3


# noinspection SpellCheckingInspection
class EgateType(Enum):
	"""2 Members, EDGE ... LEVel"""
	EDGE = 0
	LEVel = 1


# noinspection SpellCheckingInspection
class EnrType(Enum):
	"""3 Members, DIODe ... SMARt"""
	DIODe = 0
	RESistor = 1
	SMARt = 2


# noinspection SpellCheckingInspection
class ErrorType(Enum):
	"""2 Members, FREQuency ... PHASe"""
	FREQuency = 0
	PHASe = 1


# noinspection SpellCheckingInspection
class EspectrumRtype(Enum):
	"""2 Members, CPOWer ... PEAK"""
	CPOWer = 0
	PEAK = 1


# noinspection SpellCheckingInspection
class EvaluateDsp(Enum):
	"""4 Members, CHIRp ... REGion"""
	CHIRp = 0
	FULL = 1
	HOP = 2
	REGion = 3


# noinspection SpellCheckingInspection
class EvaluateType(Enum):
	"""2 Members, ITIMe ... QTIMe"""
	ITIMe = 0
	QTIMe = 1


# noinspection SpellCheckingInspection
class EvaluationFormat(Enum):
	"""8 Members, CCDF ... VECTor"""
	CCDF = 0
	FREQuency = 1
	MAGNitude = 2
	PHASe = 3
	RIMag = 4
	STATistic = 5
	UPHase = 6
	VECTor = 7


# noinspection SpellCheckingInspection
class EvaluationMode(Enum):
	"""3 Members, FDOMain ... TDOMain"""
	FDOMain = 0
	IQ = 1
	TDOMain = 2


# noinspection SpellCheckingInspection
class EventFilterCondition(Enum):
	"""4 Members, FAILed ... PASSed"""
	FAILed = 0
	GTEQual = 1
	LTEQual = 2
	PASSed = 3


# noinspection SpellCheckingInspection
class EventOnce(Enum):
	"""1 Members, ONCE ... ONCE"""
	ONCE = 0


# noinspection SpellCheckingInspection
class EvmCalc(Enum):
	"""4 Members, MACPower ... SYMBol"""
	MACPower = 0
	MECPower = 1
	SIGNal = 2
	SYMBol = 3


# noinspection SpellCheckingInspection
class EvmCalcState(Enum):
	"""5 Members, AOTP ... TGPP"""
	AOTP = 0
	CUSTom = 1
	HPOS = 2
	LPOS = 3
	TGPP = 4


# noinspection SpellCheckingInspection
class Factory(Enum):
	"""3 Members, ALL ... STANdard"""
	ALL = 0
	PATTern = 1
	STANdard = 2


# noinspection SpellCheckingInspection
class FdrAssignment(Enum):
	"""2 Members, ALL ... CUSTom"""
	ALL = 0
	CUSTom = 1


# noinspection SpellCheckingInspection
class FftFilterMode(Enum):
	"""3 Members, AUTO ... WIDE"""
	AUTO = 0
	NARRow = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class FftOffsetMode(Enum):
	"""3 Members, AUTO ... PEAK"""
	AUTO = 0
	GICenter = 1
	PEAK = 2


# noinspection SpellCheckingInspection
class FftWindowType(Enum):
	"""7 Members, BLACkharris ... RECTangular"""
	BLACkharris = 0
	FLATtop = 1
	GAUSsian = 2
	HAMMing = 3
	HANNing = 4
	KAISerbessel = 5
	RECTangular = 6


# noinspection SpellCheckingInspection
class FftWindowTypeK60(Enum):
	"""7 Members, BLACkharris ... RECTangular"""
	BLACkharris = 0
	CHEByshev = 1
	FLATtop = 2
	GAUSsian = 3
	HAMMing = 4
	HANNing = 5
	RECTangular = 6


# noinspection SpellCheckingInspection
class FileFormat(Enum):
	"""2 Members, CSV ... DAT"""
	CSV = 0
	DAT = 1


# noinspection SpellCheckingInspection
class FileFormatDdem(Enum):
	"""2 Members, FRES ... VAE"""
	FRES = 0
	VAE = 1


# noinspection SpellCheckingInspection
class FileFormatSource(Enum):
	"""2 Members, CSV ... FRES"""
	CSV = 0
	FRES = 1


# noinspection SpellCheckingInspection
class FileSeparator(Enum):
	"""3 Members, COMMa ... TAB"""
	COMMa = 0
	SEMicolon = 1
	TAB = 2


# noinspection SpellCheckingInspection
class FilterTypeA(Enum):
	"""2 Members, FLAT ... GAUSs"""
	FLAT = 0
	GAUSs = 1


# noinspection SpellCheckingInspection
class FilterTypeB(Enum):
	"""9 Members, CFILter ... RRC"""
	CFILter = 0
	CISPr = 1
	FFT = 2
	MIL = 3
	NOISe = 4
	NORMal = 5
	P5 = 6
	PULSe = 7
	RRC = 8


# noinspection SpellCheckingInspection
class FilterTypeC(Enum):
	"""7 Members, CFILter ... RRC"""
	CFILter = 0
	CISPr = 1
	MIL = 2
	NORMal = 3
	P5 = 4
	PULSe = 5
	RRC = 6


# noinspection SpellCheckingInspection
class FilterTypeK91(Enum):
	"""5 Members, CFILter ... RRC"""
	CFILter = 0
	NORMal = 1
	P5 = 2
	PULSe = 3
	RRC = 4


# noinspection SpellCheckingInspection
class FilterTypeNr5G(Enum):
	"""7 Members, CFILter ... RRC"""
	CFILter = 0
	FFT = 1
	NOISe = 2
	NORMal = 3
	P5 = 4
	PULSe = 5
	RRC = 6


# noinspection SpellCheckingInspection
class FineSync(Enum):
	"""3 Members, DDATa ... PATTern"""
	DDATa = 0
	KDATa = 1
	PATTern = 2


# noinspection SpellCheckingInspection
class FlatnessUnit(Enum):
	"""2 Members, DB ... DBM"""
	DB = 0
	DBM = 1


# noinspection SpellCheckingInspection
class FmVideoFilterType(Enum):
	"""6 Members, LP01 ... NONE"""
	LP01 = 0
	LP1 = 1
	LP10 = 2
	LP25 = 3
	LP5 = 4
	NONE = 5


# noinspection SpellCheckingInspection
class FormatCoductor(Enum):
	"""2 Members, CONDucted ... OTA"""
	CONDucted = 0
	OTA = 1


# noinspection SpellCheckingInspection
class FormatDci(Enum):
	"""15 Members, F00 ... F31"""
	F00 = 0
	F01 = 1
	F02 = 2
	F10 = 3
	F11 = 4
	F12 = 5
	F20 = 6
	F21 = 7
	F22 = 8
	F23 = 9
	F24 = 10
	F25 = 11
	F26 = 12
	F30 = 13
	F31 = 14


# noinspection SpellCheckingInspection
class FormatMHelper(Enum):
	"""3 Members, MANual ... MULTisiso"""
	MANual = 0
	MIMO = 1
	MULTisiso = 2


# noinspection SpellCheckingInspection
class FpeaksSortMode(Enum):
	"""2 Members, X ... Y"""
	X = 0
	Y = 1


# noinspection SpellCheckingInspection
class FrameModulation(Enum):
	"""3 Members, AUTO ... PATTern"""
	AUTO = 0
	DATA = 1
	PATTern = 2


# noinspection SpellCheckingInspection
class FrameModulationB(Enum):
	"""2 Members, DATA ... PATTern"""
	DATA = 0
	PATTern = 1


# noinspection SpellCheckingInspection
class FrameOptimize(Enum):
	"""2 Members, DYNamic ... SPEed"""
	DYNamic = 0
	SPEed = 1


# noinspection SpellCheckingInspection
class FramesScope(Enum):
	"""2 Members, ALL ... CHANnel"""
	ALL = 0
	CHANnel = 1


# noinspection SpellCheckingInspection
class FrameTriggerSource(Enum):
	"""3 Members, AVAilable ... RSLots"""
	AVAilable = 0
	NAVailable = 1
	RSLots = 2


# noinspection SpellCheckingInspection
class FrCharReference(Enum):
	"""2 Members, LRB ... RTCF"""
	LRB = 0
	RTCF = 1


# noinspection SpellCheckingInspection
class FreqhopingMode(Enum):
	"""3 Members, DISable ... INTRa"""
	DISable = 0
	INTer = 1
	INTRa = 2


# noinspection SpellCheckingInspection
class FreqHoppingMode(Enum):
	"""3 Members, INTer ... NONE"""
	INTer = 0
	INTRa = 1
	NONE = 2


# noinspection SpellCheckingInspection
class FreqOffsetMode(Enum):
	"""2 Members, ARBitrary ... EQUidistant"""
	ARBitrary = 0
	EQUidistant = 1


# noinspection SpellCheckingInspection
class FreqReference(Enum):
	"""2 Members, CENTer ... EDGE"""
	CENTer = 0
	EDGE = 1


# noinspection SpellCheckingInspection
class FreqTimeScaling(Enum):
	"""4 Members, GHZ_us ... MHZ_us"""
	GHZ_us = 0
	HZ_us = 1
	KHZ_us = 2
	MHZ_us = 3


# noinspection SpellCheckingInspection
class FrequencyCouplingLinkA(Enum):
	"""3 Members, OFF ... SPAN"""
	OFF = 0
	RBW = 1
	SPAN = 2


# noinspection SpellCheckingInspection
class FrequencyCouplingLinkB(Enum):
	"""2 Members, OFF ... SPAN"""
	OFF = 0
	SPAN = 1


# noinspection SpellCheckingInspection
class FrequencyScaling(Enum):
	"""4 Members, GHZ ... MHZ"""
	GHZ = 0
	HZ = 1
	KHZ = 2
	MHZ = 3


# noinspection SpellCheckingInspection
class FrequencyType(Enum):
	"""3 Members, IF ... RF"""
	IF = 0
	LO = 1
	RF = 2


# noinspection SpellCheckingInspection
class FullScaleLevelUnit(Enum):
	"""2 Members, DBM ... VOLT"""
	DBM = 0
	VOLT = 1


# noinspection SpellCheckingInspection
class FunctionA(Enum):
	"""2 Members, MAX ... OFF"""
	MAX = 0
	OFF = 1


# noinspection SpellCheckingInspection
class FunctionB(Enum):
	"""3 Members, MAX ... SUM"""
	MAX = 0
	NONE = 1
	SUM = 2


# noinspection SpellCheckingInspection
class GatedSourceK30(Enum):
	"""3 Members, EXT2 ... EXTernal"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2


# noinspection SpellCheckingInspection
class GatedSourceLte(Enum):
	"""7 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	PSENsor = 4
	RFPower = 5
	VIDeo = 6


# noinspection SpellCheckingInspection
class GatedSourceNr5G(Enum):
	"""10 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	IMMediate = 4
	IQPower = 5
	PSENsor = 6
	RFPower = 7
	TIME = 8
	VIDeo = 9


# noinspection SpellCheckingInspection
class GeneratorIntf(Enum):
	"""2 Members, GPIB ... TCPip"""
	GPIB = 0
	TCPip = 1


# noinspection SpellCheckingInspection
class GeneratorIntfType(Enum):
	"""3 Members, GPIB ... TCPip"""
	GPIB = 0
	PEXPress = 1
	TCPip = 2


# noinspection SpellCheckingInspection
class GeneratorLink(Enum):
	"""2 Members, GPIB ... TTL"""
	GPIB = 0
	TTL = 1


# noinspection SpellCheckingInspection
class GpibTerminator(Enum):
	"""2 Members, EOI ... LFEoi"""
	EOI = 0
	LFEoi = 1


# noinspection SpellCheckingInspection
class GprdMeasMethod(Enum):
	"""2 Members, FLATtop ... ORTHogonal"""
	FLATtop = 0
	ORTHogonal = 1


# noinspection SpellCheckingInspection
class GrouphopingMode(Enum):
	"""3 Members, DISable ... NEITher"""
	DISable = 0
	ENABle = 1
	NEITher = 2


# noinspection SpellCheckingInspection
class GrpdRelRefType(Enum):
	"""3 Members, AVERage ... MANual"""
	AVERage = 0
	CENTer = 1
	MANual = 2


# noinspection SpellCheckingInspection
class GuardInterval(Enum):
	"""20 Members, ALL ... MS"""
	ALL = 0
	DL = 1
	DL16 = 2
	DL32 = 3
	DN16 = 4
	DN8 = 5
	DS = 6
	FBURst = 7
	L1G1 = 8
	L1G2 = 9
	L2G1 = 10
	L2G2 = 11
	L4G1 = 12
	L4G4 = 13
	ML = 14
	ML16 = 15
	ML32 = 16
	MN16 = 17
	MN8 = 18
	MS = 19


# noinspection SpellCheckingInspection
class GuardTime(Enum):
	"""2 Members, NORMal ... SHORt"""
	NORMal = 0
	SHORt = 1


# noinspection SpellCheckingInspection
class HalfFrame(Enum):
	"""2 Members, ONE ... ZERO"""
	ONE = 0
	ZERO = 1


# noinspection SpellCheckingInspection
class HardcopyContent(Enum):
	"""2 Members, HCOPy ... WINDows"""
	HCOPy = 0
	WINDows = 1


# noinspection SpellCheckingInspection
class HardcopyHeader(Enum):
	"""5 Members, ALWays ... SECTion"""
	ALWays = 0
	GLOBal = 1
	NEVer = 2
	ONCE = 3
	SECTion = 4


# noinspection SpellCheckingInspection
class HardcopyLogo(Enum):
	"""3 Members, ALWays ... NEVer"""
	ALWays = 0
	GLOBal = 1
	NEVer = 2


# noinspection SpellCheckingInspection
class HardcopyMode(Enum):
	"""2 Members, REPort ... SCReen"""
	REPort = 0
	SCReen = 1


# noinspection SpellCheckingInspection
class HardcopyPageSize(Enum):
	"""2 Members, A4 ... US"""
	A4 = 0
	US = 1


# noinspection SpellCheckingInspection
class HeadersK50(Enum):
	"""9 Members, ALL ... STOP"""
	ALL = 0
	DELTa = 1
	FREQuency = 2
	IDENt = 3
	POWer = 4
	RBW = 5
	SID = 6
	STARt = 7
	STOP = 8


# noinspection SpellCheckingInspection
class HidGenMethod(Enum):
	"""2 Members, NID ... NIDCell"""
	NID = 0
	NIDCell = 1


# noinspection SpellCheckingInspection
class HoppingMode(Enum):
	"""3 Members, GROup ... SEQuence"""
	GROup = 0
	NONE = 1
	SEQuence = 2


# noinspection SpellCheckingInspection
class HopTableHeaders(Enum):
	"""25 Members, ALL ... SWITching"""
	ALL = 0
	AVGFm = 1
	AVGPower = 2
	AVPHm = 3
	BEGin = 4
	DWELl = 5
	FMERror = 6
	FMSLength = 7
	FMSPoint = 8
	FMSTime = 9
	FREQuency = 10
	MAXFm = 11
	MAXPower = 12
	MINPower = 13
	MXPHm = 14
	PMSLength = 15
	PMSPoint = 16
	PMSTime = 17
	PWRRipple = 18
	RELFrequency = 19
	RMSFm = 20
	RMSPm = 21
	STAFrequency = 22
	STATe = 23
	SWITching = 24


# noinspection SpellCheckingInspection
class HopXaxisItems(Enum):
	"""24 Members, AVGFm ... SWITching"""
	AVGFm = 0
	AVGPower = 1
	AVPHm = 2
	BEGin = 3
	DWELl = 4
	FMERror = 5
	FMSLength = 6
	FMSPoint = 7
	FMSTime = 8
	FREQuency = 9
	INDex = 10
	MAXFm = 11
	MAXPower = 12
	MINPower = 13
	MXPHm = 14
	PMSLength = 15
	PMSPoint = 16
	PMSTime = 17
	PWRRipple = 18
	RELFrequency = 19
	RMSFm = 20
	RMSPm = 21
	STAFrequency = 22
	SWITching = 23


# noinspection SpellCheckingInspection
class HumsFileFormat(Enum):
	"""2 Members, JSON ... XML"""
	JSON = 0
	XML = 1


# noinspection SpellCheckingInspection
class IdnFormat(Enum):
	"""3 Members, FSL ... NEW"""
	FSL = 0
	LEGacy = 1
	NEW = 2


# noinspection SpellCheckingInspection
class IfGainMode(Enum):
	"""2 Members, NORMal ... PULSe"""
	NORMal = 0
	PULSe = 1


# noinspection SpellCheckingInspection
class IfGainModeDdem(Enum):
	"""5 Members, AVERaging ... USER"""
	AVERaging = 0
	FREeze = 1
	NORMal = 2
	TRACking = 3
	USER = 4


# noinspection SpellCheckingInspection
class IfSource(Enum):
	"""4 Members, HVIDeo ... VIDeo"""
	HVIDeo = 0
	IF = 1
	IF2 = 2
	VIDeo = 3


# noinspection SpellCheckingInspection
class InOutDirection(Enum):
	"""2 Members, INPut ... OUTPut"""
	INPut = 0
	OUTPut = 1


# noinspection SpellCheckingInspection
class InputConnector(Enum):
	"""2 Members, AIQI ... RF"""
	AIQI = 0
	RF = 1


# noinspection SpellCheckingInspection
class InputConnectorB(Enum):
	"""3 Members, AIQI ... RFPRobe"""
	AIQI = 0
	RF = 1
	RFPRobe = 2


# noinspection SpellCheckingInspection
class InputConnectorC(Enum):
	"""2 Members, RF ... RFPRobe"""
	RF = 0
	RFPRobe = 1


# noinspection SpellCheckingInspection
class InputRf(Enum):
	"""1 Members, RF ... RF"""
	RF = 0


# noinspection SpellCheckingInspection
class InputSelect(Enum):
	"""2 Members, INPut1 ... INPut2"""
	INPut1 = 0
	INPut2 = 1


# noinspection SpellCheckingInspection
class InputSource(Enum):
	"""7 Members, ABBand ... RFAiq"""
	ABBand = 0
	AIQ = 1
	DIQ = 2
	FIQ = 3
	OBBand = 4
	RF = 5
	RFAiq = 6


# noinspection SpellCheckingInspection
class InputSourceB(Enum):
	"""2 Members, FIQ ... RF"""
	FIQ = 0
	RF = 1


# noinspection SpellCheckingInspection
class InputSourceC(Enum):
	"""4 Members, BARKer ... PFM"""
	BARKer = 0
	EBARker = 1
	FIQ = 2
	PFM = 3


# noinspection SpellCheckingInspection
class InputSourceLte(Enum):
	"""4 Members, AIQ ... RF"""
	AIQ = 0
	DIQ = 1
	FILE = 2
	RF = 3


# noinspection SpellCheckingInspection
class InstrumentMode(Enum):
	"""3 Members, MSRanalyzer ... SANalyzer"""
	MSRanalyzer = 0
	RTMStandard = 1
	SANalyzer = 2


# noinspection SpellCheckingInspection
class IqBandwidthMode(Enum):
	"""3 Members, AUTO ... MANual"""
	AUTO = 0
	FFT = 1
	MANual = 2


# noinspection SpellCheckingInspection
class IqBandwidthModeNr5G(Enum):
	"""2 Members, CF ... MANual"""
	CF = 0
	MANual = 1


# noinspection SpellCheckingInspection
class IqDataFormat(Enum):
	"""4 Members, FloatComplex ... IntegerReal"""
	FloatComplex = "FLOat32,COMPlex"
	FloatReal = "FLOat32,REAL"
	IntegerComplex = "INT32,COMPlex"
	IntegerReal = "INT32,REAL"


# noinspection SpellCheckingInspection
class IqDataFormatDdem(Enum):
	"""10 Members, FloatComplex ... IntegerReal"""
	FloatComplex = "FLOat32,COMPlex"
	FloatIiQq = "FLOat32,IIQQ"
	FloatIqIq = "FLOat32,IQIQ"
	FloatPolar = "FLOat32,POLar"
	FloatReal = "FLOat32,REAL"
	IntegerComplex = "INT32,COMPlex"
	IntegerIiQq = "INT32,IIQQ"
	IntegerIqIq = "INT32,IQIQ"
	IntegerPolar = "INT32,POLar"
	IntegerReal = "INT32,REAL"


# noinspection SpellCheckingInspection
class IqFftWindowType(Enum):
	"""7 Members, BLACkman ... RECTangle"""
	BLACkman = 0
	CHEByshev = 1
	FLATtop = 2
	GAUSs = 3
	HAMMing = 4
	HANNing = 5
	RECTangle = 6


# noinspection SpellCheckingInspection
class IqRangeType(Enum):
	"""2 Members, CAPTure ... RRANge"""
	CAPTure = 0
	RRANge = 1


# noinspection SpellCheckingInspection
class IqResultDataFormat(Enum):
	"""3 Members, COMPatible ... IQPair"""
	COMPatible = 0
	IQBLock = 1
	IQPair = 2


# noinspection SpellCheckingInspection
class IqType(Enum):
	"""3 Members, Ipart ... Qpart"""
	Ipart = "I"
	IQpart = "IQ"
	Qpart = "Q"


# noinspection SpellCheckingInspection
class LayerMappingDl(Enum):
	"""11 Members, LC11 ... LC82"""
	LC11 = 0
	LC21 = 1
	LC22 = 2
	LC31 = 3
	LC32 = 4
	LC41 = 5
	LC42 = 6
	LC52 = 7
	LC62 = 8
	LC72 = 9
	LC82 = 10


# noinspection SpellCheckingInspection
class LayerMappingUl(Enum):
	"""5 Members, LC11 ... LC42"""
	LC11 = 0
	LC21 = 1
	LC22 = 2
	LC32 = 3
	LC42 = 4


# noinspection SpellCheckingInspection
class LedState(Enum):
	"""3 Members, GREen ... RED"""
	GREen = 0
	GREY = 1
	RED = 2


# noinspection SpellCheckingInspection
class LeftRightDirection(Enum):
	"""2 Members, LEFT ... RIGHt"""
	LEFT = 0
	RIGHt = 1


# noinspection SpellCheckingInspection
class LimitCheck(Enum):
	"""2 Members, FAILed ... PASS"""
	FAILed = 0
	PASS = 1


# noinspection SpellCheckingInspection
class LimitShape(Enum):
	"""6 Members, FC1 ... NONE"""
	FC1 = 0
	FC2 = 1
	FC3 = 2
	FC4 = 3
	FC5 = 4
	NONE = 5


# noinspection SpellCheckingInspection
class LimitState(Enum):
	"""4 Members, ABSolute ... RELative"""
	ABSolute = 0
	AND = 1
	OR = 2
	RELative = 3


# noinspection SpellCheckingInspection
class LimitUnit(Enum):
	"""27 Members, A ... WATT"""
	A = 0
	AMPere = 1
	DB = 2
	DBM = 3
	DBM_mhz = 4
	DBMV = 5
	DBMV_mhz = 6
	DBPT = 7
	DBPT_mhz = 8
	DBPW = 9
	DBPW_mhz = 10
	DBUA = 11
	DBUa_m = 12
	DBUa_mhz = 13
	DBUa_mmhz = 14
	DBUV = 15
	DBUV_m = 16
	DBUV_mhz = 17
	DBUV_mmhz = 18
	DEG = 19
	HZ = 20
	PCT = 21
	RAD = 22
	S = 23
	UNITless = 24
	VOLT = 25
	WATT = 26


# noinspection SpellCheckingInspection
class LimitUnitB(Enum):
	"""22 Members, AMPere ... WATT"""
	AMPere = 0
	DB = 1
	DBM = 2
	DBMV = 3
	DBMV_mhz = 4
	DBPW = 5
	DBUA = 6
	DBUa_m = 7
	DBUa_mhz = 8
	DBUa_mmhz = 9
	DBUV = 10
	DBUV_m = 11
	DBUV_mhz = 12
	DBUV_mmhz = 13
	DEG = 14
	HZ = 15
	PCT = 16
	RAD = 17
	S = 18
	UNITless = 19
	VOLT = 20
	WATT = 21


# noinspection SpellCheckingInspection
class LimitUnitLte(Enum):
	"""2 Members, CARR ... HZ"""
	CARR = 0
	HZ = 1


# noinspection SpellCheckingInspection
class LisnPhase(Enum):
	"""4 Members, L1 ... N"""
	L1 = 0
	L2 = 1
	L3 = 2
	N = 3


# noinspection SpellCheckingInspection
class LisnType(Enum):
	"""8 Members, ENV216 ... TWOPhase"""
	ENV216 = 0
	ENV4200 = 1
	ENV432 = 2
	ESH2z5 = 3
	ESH3z5 = 4
	FOURphase = 5
	OFF = 6
	TWOPhase = 7


# noinspection SpellCheckingInspection
class LoadType(Enum):
	"""2 Members, NEW ... REPLace"""
	NEW = 0
	REPLace = 1


# noinspection SpellCheckingInspection
class LogicalFnc(Enum):
	"""2 Members, AND ... OR"""
	AND = 0
	OR = 1


# noinspection SpellCheckingInspection
class LoscLocation(Enum):
	"""3 Members, CACB ... USER"""
	CACB = 0
	CCC = 1
	USER = 2


# noinspection SpellCheckingInspection
class LoType(Enum):
	"""2 Members, FIXed ... VARiable"""
	FIXed = 0
	VARiable = 1


# noinspection SpellCheckingInspection
class LowerLimit(Enum):
	"""6 Members, ACLR ... SEM"""
	ACLR = 0
	ALL = 1
	CRT = 2
	EVM = 3
	GEN = 4
	SEM = 5


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class LteCarrResourceBlocks(Enum):
	"""6 Members, N100 ... N75"""
	N100 = 0
	N15 = 1
	N25 = 2
	N50 = 3
	N6 = 4
	N75 = 5


# noinspection SpellCheckingInspection
class MacFcs(Enum):
	"""3 Members, O2 ... OFF"""
	O2 = 0
	O4 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class MarkerDemodMode(Enum):
	"""5 Members, AC ... PM"""
	AC = 0
	AM = 1
	AUDio = 2
	FM = 3
	PM = 4


# noinspection SpellCheckingInspection
class MarkerFunctionA(Enum):
	"""15 Members, ACPower ... TPOWer"""
	ACPower = 0
	AOBandwidth = 1
	AOBWidth = 2
	CN = 3
	CN0 = 4
	COBandwidth = 5
	COBWidth = 6
	CPOWer = 7
	GACLr = 8
	MACM = 9
	MCACpower = 10
	OBANdwidth = 11
	OBWidth = 12
	PPOWer = 13
	TPOWer = 14


# noinspection SpellCheckingInspection
class MarkerFunctionB(Enum):
	"""8 Members, ACPower ... OBWidth"""
	ACPower = 0
	AOBWidth = 1
	CN = 2
	CN0 = 3
	CPOWer = 4
	MCACpower = 5
	OBANdwidth = 6
	OBWidth = 7


# noinspection SpellCheckingInspection
class MarkerMode(Enum):
	"""3 Members, DENSity ... RPOWer"""
	DENSity = 0
	POWer = 1
	RPOWer = 2


# noinspection SpellCheckingInspection
class MarkerRealImag(Enum):
	"""3 Members, IMAG ... REAL"""
	IMAG = 0
	MAGNitude = 1
	REAL = 2


# noinspection SpellCheckingInspection
class MarkerRealImagB(Enum):
	"""2 Members, IMAG ... REAL"""
	IMAG = 0
	REAL = 1


# noinspection SpellCheckingInspection
class MaskCondition(Enum):
	"""4 Members, ENTer ... OUTSide"""
	ENTer = 0
	INSide = 1
	LEAVe = 2
	OUTSide = 3


# noinspection SpellCheckingInspection
class McsTable(Enum):
	"""3 Members, Q256 ... Q64L"""
	Q256 = 0
	Q64 = 1
	Q64L = 2


# noinspection SpellCheckingInspection
class MdpdWaveformType(Enum):
	"""2 Members, DDPD ... MDPD"""
	DDPD = 0
	MDPD = 1


# noinspection SpellCheckingInspection
class MeasurementK91(Enum):
	"""5 Members, ACPower ... OBWidth"""
	ACPower = 0
	CPOWer = 1
	MCACpower = 2
	OBANdwidth = 3
	OBWidth = 4


# noinspection SpellCheckingInspection
class MeasurementLte(Enum):
	"""12 Members, ACLR ... TPOO"""
	ACLR = 0
	CACLr = 1
	CDECoder = 2
	ESPectrum = 3
	EVM = 4
	MCAClr = 5
	MCESpectrum = 6
	RAA = 7
	SPECtrum = 8
	TAERror = 9
	TAL = 10
	TPOO = 11


# noinspection SpellCheckingInspection
class MeasurementLteResult(Enum):
	"""6 Members, ACPower ... PPOWer"""
	ACPower = 0
	CPOWer = 1
	GACLr = 2
	MACM = 3
	MCACpower = 4
	PPOWer = 5


# noinspection SpellCheckingInspection
class MeasurementNr5G(Enum):
	"""10 Members, ACLR ... TPOO"""
	ACLR = 0
	CACLr = 1
	CMEasurement = 2
	ESPectrum = 3
	EVM = 4
	MCAClr = 5
	MCESpectrum = 6
	PRACh = 7
	TAERror = 8
	TPOO = 9


# noinspection SpellCheckingInspection
class MeasurementStep(Enum):
	"""4 Members, NESTimate ... SPOTstep"""
	NESTimate = 0
	SDETection = 1
	SOVerview = 2
	SPOTstep = 3


# noinspection SpellCheckingInspection
class MeasurementType(Enum):
	"""2 Members, DIRected ... WIDE"""
	DIRected = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class MeasurementTypeK91(Enum):
	"""2 Members, FLATness ... GRDelay"""
	FLATness = 0
	GRDelay = 1


# noinspection SpellCheckingInspection
class MessageType(Enum):
	"""2 Members, REMote ... SMSG"""
	REMote = 0
	SMSG = 1


# noinspection SpellCheckingInspection
class MimoAnalyzeMethod(Enum):
	"""3 Members, MANual ... SIMultaneous"""
	MANual = 0
	OSP = 1
	SIMultaneous = 2


# noinspection SpellCheckingInspection
class MixerIdentifier(Enum):
	"""2 Members, CLOCk ... LO"""
	CLOCk = 0
	LO = 1


# noinspection SpellCheckingInspection
class ModulationDl(Enum):
	"""5 Members, Q1K ... QPSK"""
	Q1K = 0
	QAM16 = 1
	QAM256 = 2
	QAM64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class ModulationUl(Enum):
	"""6 Members, PSK8 ... QPSK"""
	PSK8 = 0
	Q1K = 1
	QAM16 = 2
	QAM256 = 3
	QAM64 = 4
	QPSK = 5


# noinspection SpellCheckingInspection
class MpowerDetector(Enum):
	"""2 Members, MEAN ... PEAK"""
	MEAN = 0
	PEAK = 1


# noinspection SpellCheckingInspection
class MskFormat(Enum):
	"""4 Members, DIFFerential ... TYPe2"""
	DIFFerential = 0
	NORMal = 1
	TYPe1 = 2
	TYPe2 = 3


# noinspection SpellCheckingInspection
class MsSyncMode(Enum):
	"""5 Members, MASTer ... SLAVe"""
	MASTer = 0
	NONE = 1
	PRIMary = 2
	SECondary = 3
	SLAVe = 4


# noinspection SpellCheckingInspection
class NgMethod(Enum):
	"""6 Members, AUTO ... NGCustom"""
	AUTO = 0
	NG1 = 1
	NG1_2 = 2
	NG1_6 = 3
	NG2 = 4
	NGCustom = 5


# noinspection SpellCheckingInspection
class NoiseFigureLimit(Enum):
	"""7 Members, ENR ... YFACtor"""
	ENR = 0
	GAIN = 1
	NOISe = 2
	PCOLd = 3
	PHOT = 4
	TEMPerature = 5
	YFACtor = 6


# noinspection SpellCheckingInspection
class NoiseFigureResult(Enum):
	"""11 Members, CPCold ... YFACtor"""
	CPCold = 0
	CPHot = 1
	CYFactor = 2
	ENR = 3
	GAIN = 4
	NOISe = 5
	NUNCertainty = 6
	PCOLd = 7
	PHOT = 8
	TEMPerature = 9
	YFACtor = 10


# noinspection SpellCheckingInspection
class NoiseFigureResultCustom(Enum):
	"""10 Members, CPCold ... YFACtor"""
	CPCold = 0
	CPHot = 1
	CYFactor = 2
	ENR = 3
	GAIN = 4
	NOISe = 5
	PCOLd = 6
	PHOT = 7
	TEMPerature = 8
	YFACtor = 9


# noinspection SpellCheckingInspection
class NoOfMimoAntennas(Enum):
	"""3 Members, TX1 ... TX4"""
	TX1 = 0
	TX2 = 1
	TX4 = 2


# noinspection SpellCheckingInspection
class NormalInverted(Enum):
	"""2 Members, INVerted ... NORMal"""
	INVerted = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class NpRatioMode(Enum):
	"""2 Members, DENSity ... POWer"""
	DENSity = 0
	POWer = 1


# noinspection SpellCheckingInspection
class OddEven(Enum):
	"""3 Members, EODD ... ODD"""
	EODD = 0
	EVEN = 1
	ODD = 2


# noinspection SpellCheckingInspection
class OffPowerUnit(Enum):
	"""2 Members, DBM ... DMHZ"""
	DBM = 0
	DMHZ = 1


# noinspection SpellCheckingInspection
class OffsetToSubcarrier(Enum):
	"""5 Members, NONE ... OS11"""
	NONE = 0
	OS00 = 1
	OS01 = 2
	OS10 = 3
	OS11 = 4


# noinspection SpellCheckingInspection
class OffState(Enum):
	"""1 Members, OFF ... OFF"""
	OFF = 0


# noinspection SpellCheckingInspection
class OperatingBandNr5G(Enum):
	"""51 Members, N1 ... N95"""
	N1 = 0
	N12 = 1
	N14 = 2
	N18 = 3
	N2 = 4
	N20 = 5
	N25 = 6
	N257 = 7
	N258 = 8
	N26 = 9
	N260 = 10
	N261 = 11
	N28 = 12
	N29 = 13
	N3 = 14
	N30 = 15
	N34 = 16
	N38 = 17
	N39 = 18
	N40 = 19
	N41 = 20
	N48 = 21
	N5 = 22
	N50 = 23
	N51 = 24
	N53 = 25
	N65 = 26
	N66 = 27
	N7 = 28
	N70 = 29
	N71 = 30
	N74 = 31
	N75 = 32
	N76 = 33
	N77 = 34
	N78 = 35
	N79 = 36
	N8 = 37
	N80 = 38
	N81 = 39
	N82 = 40
	N83 = 41
	N84 = 42
	N86 = 43
	N89 = 44
	N90 = 45
	N91 = 46
	N92 = 47
	N93 = 48
	N94 = 49
	N95 = 50


# noinspection SpellCheckingInspection
class OptimizationCriterion(Enum):
	"""2 Members, EVMMin ... RMSMin"""
	EVMMin = 0
	RMSMin = 1


# noinspection SpellCheckingInspection
class OptionState(Enum):
	"""3 Members, OCCupy ... ON"""
	OCCupy = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class OspIdn(Enum):
	"""3 Members, A11 ... A13"""
	A11 = 0
	A12 = 1
	A13 = 2


# noinspection SpellCheckingInspection
class OutputIfSource(Enum):
	"""3 Members, IF ... VIDeo"""
	IF = 0
	IF2 = 1
	VIDeo = 2


# noinspection SpellCheckingInspection
class OutputType(Enum):
	"""4 Members, DEVice ... UDEFined"""
	DEVice = 0
	TARMed = 1
	TOFF = 2
	UDEFined = 3


# noinspection SpellCheckingInspection
class OversampleFactor(Enum):
	"""5 Members, OV10 ... OV8"""
	OV10 = 0
	OV12 = 1
	OV4 = 2
	OV6 = 3
	OV8 = 4


# noinspection SpellCheckingInspection
class PadType(Enum):
	"""2 Members, MLPad ... SRESistor"""
	MLPad = 0
	SRESistor = 1


# noinspection SpellCheckingInspection
class PageMarginUnit(Enum):
	"""2 Members, IN ... MM"""
	IN = 0
	MM = 1


# noinspection SpellCheckingInspection
class PageOrientation(Enum):
	"""2 Members, LANDscape ... PORTrait"""
	LANDscape = 0
	PORTrait = 1


# noinspection SpellCheckingInspection
class PasteLogicMode(Enum):
	"""4 Members, CUSTom ... UNUSed"""
	CUSTom = 0
	DATA = 1
	SLOTs = 2
	UNUSed = 3


# noinspection SpellCheckingInspection
class Path(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class PayloadLenSource(Enum):
	"""4 Members, ESTimate ... SFIeld"""
	ESTimate = 0
	HTSignal = 1
	LSIGnal = 2
	SFIeld = 3


# noinspection SpellCheckingInspection
class PayloadMax(Enum):
	"""3 Members, S0 ... S2"""
	S0 = 0
	S1 = 1
	S2 = 2


# noinspection SpellCheckingInspection
class PdschDmRsSeqGenMethod(Enum):
	"""3 Members, DSID ... NIDDmrs"""
	DSID = 0
	NIDCell = 1
	NIDDmrs = 2


# noinspection SpellCheckingInspection
class PdschFormat(Enum):
	"""3 Members, OFF ... PHYDet"""
	OFF = 0
	PDCCh = 1
	PHYDet = 2


# noinspection SpellCheckingInspection
class PdschSeqGenMethod(Enum):
	"""2 Members, DSID ... NIDCell"""
	DSID = 0
	NIDCell = 1


# noinspection SpellCheckingInspection
class PeriodMode(Enum):
	"""2 Members, APERiodic ... PERiodic"""
	APERiodic = 0
	PERiodic = 1


# noinspection SpellCheckingInspection
class PhaseTrackingMethod(Enum):
	"""3 Members, OFF ... PILPay"""
	OFF = 0
	PIL = 1
	PILPay = 2


# noinspection SpellCheckingInspection
class PhrRate(Enum):
	"""4 Members, BMHP ... HMLR"""
	BMHP = 0
	BMLP = 1
	HMHR = 2
	HMLR = 3


# noinspection SpellCheckingInspection
class PictureFormat(Enum):
	"""11 Members, BMP ... WMF"""
	BMP = 0
	DOC = 1
	EWMF = 2
	GDI = 3
	JPEG = 4
	JPG = 5
	PDF = 6
	PNG = 7
	RTF = 8
	SVG = 9
	WMF = 10


# noinspection SpellCheckingInspection
class PilotSeqMode(Enum):
	"""2 Members, DETected ... STANdard"""
	DETected = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class PmeterFreqLink(Enum):
	"""3 Members, CENTer ... OFF"""
	CENTer = 0
	MARKer1 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class PmRpointMode(Enum):
	"""2 Members, MANual ... RIGHt"""
	MANual = 0
	RIGHt = 1


# noinspection SpellCheckingInspection
class Port(Enum):
	"""4 Members, PORT1 ... PORT4"""
	PORT1 = 0
	PORT2 = 1
	PORT3 = 2
	PORT4 = 3


# noinspection SpellCheckingInspection
class PowerCategory(Enum):
	"""4 Members, A ... MED"""
	A = 0
	B = 1
	LARE = 2
	MED = 3


# noinspection SpellCheckingInspection
class PowerCategoryB(Enum):
	"""2 Members, OPT1 ... OPT2"""
	OPT1 = 0
	OPT2 = 1


# noinspection SpellCheckingInspection
class PowerClass(Enum):
	"""3 Members, PC1 ... PC3"""
	PC1 = 0
	PC2 = 1
	PC3 = 2


# noinspection SpellCheckingInspection
class PowerClassB(Enum):
	"""4 Members, PC1 ... PC4"""
	PC1 = 0
	PC2 = 1
	PC3 = 2
	PC4 = 3


# noinspection SpellCheckingInspection
class PowerMeasFunction(Enum):
	"""7 Members, ACPower ... OBWidth"""
	ACPower = 0
	CN = 1
	CN0 = 2
	CPOWer = 3
	MCACpower = 4
	OBANdwidth = 5
	OBWidth = 6


# noinspection SpellCheckingInspection
class PowerMeasFunctionB(Enum):
	"""3 Members, ACPower ... MCACpower"""
	ACPower = 0
	CPOWer = 1
	MCACpower = 2


# noinspection SpellCheckingInspection
class PowerMeterUnit(Enum):
	"""3 Members, DBM ... WATT"""
	DBM = 0
	W = 1
	WATT = 2


# noinspection SpellCheckingInspection
class PowerSource(Enum):
	"""2 Members, VSUPply ... VTUNe"""
	VSUPply = 0
	VTUNe = 1


# noinspection SpellCheckingInspection
class PowerUnit(Enum):
	"""25 Members, A ... WATT"""
	A = 0
	AMPere = 1
	DB = 2
	DBM = 3
	DBM_mhz = 4
	DBMV = 5
	DBMV_mhz = 6
	DBPT = 7
	DBPT_mhz = 8
	DBPW = 9
	DBPW_mhz = 10
	DBUA = 11
	DBUa_m = 12
	DBUa_mhz = 13
	DBUa_mmhz = 14
	DBUV = 15
	DBUV_m = 16
	DBUV_mhz = 17
	DBUV_mmhz = 18
	PCT = 19
	UNITless = 20
	V = 21
	VOLT = 22
	W = 23
	WATT = 24


# noinspection SpellCheckingInspection
class PowerUnitDdem(Enum):
	"""3 Members, DBM ... DBUV"""
	DBM = 0
	DBMV = 1
	DBUV = 2


# noinspection SpellCheckingInspection
class PowerUnitK9x(Enum):
	"""11 Members, A ... WATT"""
	A = 0
	AMPere = 1
	DBM = 2
	DBMV = 3
	DBPW = 4
	DBUA = 5
	DBUV = 6
	V = 7
	VOLT = 8
	W = 9
	WATT = 10


# noinspection SpellCheckingInspection
class PowerUnitNr5G(Enum):
	"""24 Members, A ... WATT"""
	A = 0
	AMPere = 1
	DB = 2
	DBM = 3
	DBMV = 4
	DBMV_mhz = 5
	DBPT = 6
	DBPT_mhz = 7
	DBPW = 8
	DBPW_mhz = 9
	DBUA = 10
	DBUa_m = 11
	DBUa_mhz = 12
	DBUa_mmhz = 13
	DBUV = 14
	DBUV_m = 15
	DBUV_mhz = 16
	DBUV_mmhz = 17
	PCT = 18
	UNITless = 19
	V = 20
	VOLT = 21
	W = 22
	WATT = 23


# noinspection SpellCheckingInspection
class PowerVectorErrorMode(Enum):
	"""2 Members, ALL ... PSDU"""
	ALL = 0
	PSDU = 1


# noinspection SpellCheckingInspection
class PpduFormat(Enum):
	"""23 Members, AIEM ... MVHT"""
	AIEM = 0
	AIES = 1
	AIET = 2
	AIHM = 3
	AIHS = 4
	AIHT = 5
	ALL = 6
	DEHTppdu = 7
	DGRF = 8
	DHEP = 9
	DMIX = 10
	DNHT = 11
	DVHT = 12
	FAMA = 13
	FAMM = 14
	FBURst = 15
	FMMA = 16
	FMMD = 17
	FMMM = 18
	MGRF = 19
	MMIX = 20
	MNHT = 21
	MVHT = 22


# noinspection SpellCheckingInspection
class PpduSelectMode(Enum):
	"""4 Members, ALL ... MEASure"""
	ALL = 0
	DEMod = 1
	FBURst = 2
	MEASure = 3


# noinspection SpellCheckingInspection
class PpduType(Enum):
	"""10 Members, ALL ... M3"""
	ALL = 0
	D0 = 1
	D1 = 2
	D2 = 3
	D3 = 4
	FBURst = 5
	M0 = 6
	M1 = 7
	M2 = 8
	M3 = 9


# noinspection SpellCheckingInspection
class PpduTypeB(Enum):
	"""8 Members, ALL ... M2"""
	ALL = 0
	D0 = 1
	D1 = 2
	D2 = 3
	FBURst = 4
	M0 = 5
	M1 = 6
	M2 = 7


# noinspection SpellCheckingInspection
class PreambeTrackMode(Enum):
	"""2 Members, PAYLoad ... VHT"""
	PAYLoad = 0
	VHT = 1


# noinspection SpellCheckingInspection
class PreambleUnit(Enum):
	"""2 Members, HZ ... PCT"""
	HZ = 0
	PCT = 1


# noinspection SpellCheckingInspection
class PreampOption(Enum):
	"""2 Members, B23 ... B24"""
	B23 = 0
	B24 = 1


# noinspection SpellCheckingInspection
class PrecodGrnMethod(Enum):
	"""2 Members, ACRBs ... REGBundle"""
	ACRBs = 0
	REGBundle = 1


# noinspection SpellCheckingInspection
class PrecodingScheme(Enum):
	"""4 Members, BF ... TXD"""
	BF = 0
	NONE = 1
	SPM = 2
	TXD = 3


# noinspection SpellCheckingInspection
class PrefixLength(Enum):
	"""3 Members, AUTO ... NORM"""
	AUTO = 0
	EXT = 1
	NORM = 2


# noinspection SpellCheckingInspection
class PresetCompatible(Enum):
	"""8 Members, MRECeiver ... VNA"""
	MRECeiver = 0
	MSRA = 1
	OFF = 2
	PNOise = 3
	RECeiver = 4
	RTMS = 5
	SANalyzer = 6
	VNA = 7


# noinspection SpellCheckingInspection
class Probability(Enum):
	"""4 Members, P0_01 ... P10"""
	P0_01 = 0
	P0_1 = 1
	P1 = 2
	P10 = 3


# noinspection SpellCheckingInspection
class ProbeMode(Enum):
	"""4 Members, CM ... PM"""
	CM = 0
	DM = 1
	NM = 2
	PM = 3


# noinspection SpellCheckingInspection
class ProbeSetupMode(Enum):
	"""2 Members, NOACtion ... RSINgle"""
	NOACtion = 0
	RSINgle = 1


# noinspection SpellCheckingInspection
class PskFormat(Enum):
	"""7 Members, DIFFerential ... PI8D8psk"""
	DIFFerential = 0
	DPI2 = 1
	MNPi2 = 2
	N3Pi8 = 3
	NORMal = 4
	NPI2 = 5
	PI8D8psk = 6


# noinspection SpellCheckingInspection
class PsweepSetting(Enum):
	"""4 Members, BIAS ... POWer"""
	BIAS = 0
	DELay = 1
	FREQuency = 2
	POWer = 3


# noinspection SpellCheckingInspection
class PucchFormat(Enum):
	"""14 Members, F1 ... SUBF"""
	F1 = 0
	F1A = 1
	F1AN = 2
	F1AS = 3
	F1B = 4
	F1BN = 5
	F1BS = 6
	F1N = 7
	F1S = 8
	F2 = 9
	F2A = 10
	F2B = 11
	F3 = 12
	SUBF = 13


# noinspection SpellCheckingInspection
class PulseAxisItems(Enum):
	"""11 Members, DCYCle ... TSTamp"""
	DCYCle = 0
	DRATio = 1
	FALL = 2
	OFF = 3
	PNUMber = 4
	PRF = 5
	PRI = 6
	PWIDth = 7
	RISE = 8
	SETTling = 9
	TSTamp = 10


# noinspection SpellCheckingInspection
class PulseEmodelItems(Enum):
	"""18 Members, FBPTime ... RTPTime"""
	FBPTime = 0
	FHPLevel = 1
	FHPTime = 2
	FLPLevel = 3
	FLPTime = 4
	FMPLevel = 5
	FMPTime = 6
	FTPLevel = 7
	FTPTime = 8
	RBPTime = 9
	RHPLevel = 10
	RHPTime = 11
	RLPLevel = 12
	RLPTime = 13
	RMPLevel = 14
	RMPTime = 15
	RTPLevel = 16
	RTPTime = 17


# noinspection SpellCheckingInspection
class PulseFreqItems(Enum):
	"""6 Members, CRATe ... RERRor"""
	CRATe = 0
	DEViation = 1
	PERRor = 2
	POINt = 3
	PPFRequency = 4
	RERRor = 5


# noinspection SpellCheckingInspection
class PulsePhaseItems(Enum):
	"""5 Members, DEViation ... RERRor"""
	DEViation = 0
	PERRor = 1
	POINt = 2
	PPPHase = 3
	RERRor = 4


# noinspection SpellCheckingInspection
class PulsePowerItems(Enum):
	"""20 Members, ADDB ... TOP"""
	ADDB = 0
	ADPercent = 1
	AMPLitude = 2
	AVG = 3
	BASE = 4
	I = 5
	MAX = 6
	MIN = 7
	ODB = 8
	ON = 9
	OPERcent = 10
	PAVG = 11
	PMIN = 12
	POINt = 13
	PON = 14
	PPRatio = 15
	Q = 16
	RDB = 17
	RPERcent = 18
	TOP = 19


# noinspection SpellCheckingInspection
class PulseSidelobeItems(Enum):
	"""10 Members, AMPower ... SDELay"""
	AMPower = 0
	CRATio = 1
	IMPower = 2
	ISLevel = 3
	MFRequency = 4
	MPHase = 5
	MWIDth = 6
	PCORrelation = 7
	PSLevel = 8
	SDELay = 9


# noinspection SpellCheckingInspection
class PulseTimingItems(Enum):
	"""10 Members, DCYCle ... TSTamp"""
	DCYCle = 0
	DRATio = 1
	FALL = 2
	OFF = 3
	PRF = 4
	PRI = 5
	PWIDth = 6
	RISE = 7
	SETTling = 8
	TSTamp = 9


# noinspection SpellCheckingInspection
class PulseYaxisItem(Enum):
	"""5 Members, AMPLitude ... TOTal"""
	AMPLitude = 0
	BURSt = 1
	PHASe = 2
	PIBurst = 3
	TOTal = 4


# noinspection SpellCheckingInspection
class PuschModulation(Enum):
	"""9 Members, DMRS ... QPSK"""
	DMRS = 0
	PITBpsk = 1
	Q1K = 2
	Q2K = 3
	Q4K = 4
	QAM16 = 5
	QAM256 = 6
	QAM64 = 7
	QPSK = 8


# noinspection SpellCheckingInspection
class PuschModulationB(Enum):
	"""8 Members, DMRS ... QPSK"""
	DMRS = 0
	Q1K = 1
	Q2K = 2
	Q4K = 3
	QAM16 = 4
	QAM256 = 5
	QAM64 = 6
	QPSK = 7


# noinspection SpellCheckingInspection
class PushSeqGenMethod(Enum):
	"""2 Members, NIDCell ... NIDPusch"""
	NIDCell = 0
	NIDPusch = 1


# noinspection SpellCheckingInspection
class PvTmode(Enum):
	"""4 Members, EDGE ... RISE"""
	EDGE = 0
	FALL = 1
	FULL = 2
	RISE = 3


# noinspection SpellCheckingInspection
class PvtRefPower(Enum):
	"""2 Members, MAXimum ... MEAN"""
	MAXimum = 0
	MEAN = 1


# noinspection SpellCheckingInspection
class PwrLevelMode(Enum):
	"""2 Members, CURRent ... VOLTage"""
	CURRent = 0
	VOLTage = 1


# noinspection SpellCheckingInspection
class PwrMeasUnit(Enum):
	"""3 Members, ABS ... PMHZ"""
	ABS = 0
	PHZ = 1
	PMHZ = 2


# noinspection SpellCheckingInspection
class QamFormat(Enum):
	"""4 Members, DIFFerential ... NPI4"""
	DIFFerential = 0
	MNPi4 = 1
	NORMal = 2
	NPI4 = 3


# noinspection SpellCheckingInspection
class QpskFormat(Enum):
	"""7 Members, DIFFerential ... SOFFset"""
	DIFFerential = 0
	DPI4 = 1
	N3Pi4 = 2
	NORMal = 3
	NPI4 = 4
	OFFSet = 5
	SOFFset = 6


# noinspection SpellCheckingInspection
class RangeClass(Enum):
	"""3 Members, LOCal ... WIDE"""
	LOCal = 0
	MEDium = 1
	WIDE = 2


# noinspection SpellCheckingInspection
class RangeParam(Enum):
	"""12 Members, ARBW ... TSTR"""
	ARBW = 0
	LOFFset = 1
	MFRBw = 2
	NFFT = 3
	PAValue = 4
	PEXCursion = 5
	RBW = 6
	RFATtenuation = 7
	RLEVel = 8
	SNRatio = 9
	TSTP = 10
	TSTR = 11


# noinspection SpellCheckingInspection
class RealtimeMeasType(Enum):
	"""2 Members, HRESolution ... MDOMain"""
	HRESolution = 0
	MDOMain = 1


# noinspection SpellCheckingInspection
class RefChannel(Enum):
	"""3 Members, LHIGhest ... MINimum"""
	LHIGhest = 0
	MAXimum = 1
	MINimum = 2


# noinspection SpellCheckingInspection
class Reference(Enum):
	"""3 Members, ALL0 ... PS23"""
	ALL0 = 0
	AUTO = 1
	PS23 = 2


# noinspection SpellCheckingInspection
class ReferenceDataNr5G(Enum):
	"""4 Members, ALL0 ... PS23"""
	ALL0 = 0
	AUTO = 1
	PN23 = 2
	PS23 = 3


# noinspection SpellCheckingInspection
class ReferenceMode(Enum):
	"""2 Members, ABSolute ... RELative"""
	ABSolute = 0
	RELative = 1


# noinspection SpellCheckingInspection
class ReferenceSource(Enum):
	"""2 Members, EXT ... INT"""
	EXT = 0
	INT = 1


# noinspection SpellCheckingInspection
class ReferenceSourceA(Enum):
	"""11 Members, E10 ... SYNC"""
	E10 = 0
	E100 = 1
	E1000 = 2
	EAUTo = 3
	EXT1 = 4
	EXT2 = 5
	EXTernal = 6
	EXTernal1 = 7
	EXTernal2 = 8
	INTernal = 9
	SYNC = 10


# noinspection SpellCheckingInspection
class ReferenceSourceB(Enum):
	"""3 Members, EAUTo ... INTernal"""
	EAUTo = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class ReferenceSourceC(Enum):
	"""7 Members, EXT2 ... RFPower"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	IMMediate = 4
	IQPower = 5
	RFPower = 6


# noinspection SpellCheckingInspection
class ReferenceSourceD(Enum):
	"""4 Members, EXT2 ... IMMediate"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IMMediate = 3


# noinspection SpellCheckingInspection
class RefPointMode(Enum):
	"""2 Members, CC1 ... GMCFreq"""
	CC1 = 0
	GMCFreq = 1


# noinspection SpellCheckingInspection
class Relay(Enum):
	"""84 Members, AC_enable ... SWRF1in"""
	AC_enable = 0
	ACDC = 1
	AMPSw_2 = 2
	AMPSw_4 = 3
	ATT10 = 4
	ATT10db = 5
	ATT1db = 6
	ATT20 = 7
	ATT20db = 8
	ATT2db = 9
	ATT40 = 10
	ATT40db = 11
	ATT4db_a = 12
	ATT4db_b = 13
	ATT5 = 14
	ATTinput2 = 15
	CAL = 16
	CAL_enable = 17
	EATT = 18
	EMIMatt10 = 19
	EXT_relais = 20
	HP_Bypass = 21
	HP_Bypass_2 = 22
	HP_Hp100khz = 23
	HP_Hp1khz = 24
	HP_Hp1mhz = 25
	HP_Hp200khz = 26
	HP_Hp20khz = 27
	HP_Hp50khz = 28
	HP_Hp5mhz = 29
	HP_Hp9khz = 30
	HP_Sw = 31
	IFSW = 32
	INP2matt10r1 = 33
	INP2matt10r2 = 34
	INPut2 = 35
	LFMatt10 = 36
	LNA20db_1 = 37
	LNA20db_2 = 38
	LP_Lp100khz = 39
	LP_Lp14mhz = 40
	LP_Lp1mhz = 41
	LP_Lp20khz = 42
	LP_Lp40mhz = 43
	LP_Lp500khz = 44
	LP_Lp5mhz = 45
	LP_Sw = 46
	PREamp = 47
	PREamp30mhz = 48
	PRESab_bypr1 = 49
	PRESab_bypr2 = 50
	PRESab_swir1 = 51
	PRESab_swir2 = 52
	PRESel = 53
	RFAB = 54
	SATT10 = 55
	SATT20 = 56
	SATT40 = 57
	SCAL = 58
	SIGSourout = 59
	SP6T = 60
	SPAByp = 61
	SPDTinput = 62
	SPDTmwcamp = 63
	SWAMp1 = 64
	SWAMp1amp2 = 65
	SWAMp1toamp4 = 66
	SWAMp2 = 67
	SWAMp3 = 68
	SWAMp3amp4 = 69
	SWAMp4 = 70
	SWAMp5 = 71
	SWAMp6 = 72
	SWAMp7 = 73
	SWF1f2in = 74
	SWF1f2out = 75
	SWF1tof4out = 76
	SWF3f4out = 77
	SWF3in = 78
	SWF4in = 79
	SWF5in = 80
	SWF6f7in = 81
	SWFE = 82
	SWRF1in = 83


# noinspection SpellCheckingInspection
class RestrictedPrachSet(Enum):
	"""3 Members, A ... NONE"""
	A = 0
	B = 1
	NONE = 2


# noinspection SpellCheckingInspection
class ResultDevReference(Enum):
	"""4 Members, CENTer ... PMSettling"""
	CENTer = 0
	EDGE = 1
	FMSettling = 2
	PMSettling = 3


# noinspection SpellCheckingInspection
class ResultItemK18(Enum):
	"""21 Members, ACB1 ... VICC"""
	ACB1 = 0
	ACB2 = 1
	ACB3 = 2
	ACBM = 3
	ACL1 = 4
	ACP = 5
	ACU1 = 6
	AMWidth = 7
	CFACtor = 8
	EVM = 9
	GAIN = 10
	ICC = 11
	P1DB = 12
	P2DB = 13
	P3DB = 14
	PAE = 15
	PMWidth = 16
	POUT = 17
	RMS = 18
	VCC = 19
	VICC = 20


# noinspection SpellCheckingInspection
class ResultNr5G(Enum):
	"""2 Members, AASL ... AASY"""
	AASL = 0
	AASY = 1


# noinspection SpellCheckingInspection
class ResultReference(Enum):
	"""3 Members, CENTer ... RISE"""
	CENTer = 0
	FALL = 1
	RISE = 2


# noinspection SpellCheckingInspection
class ResultTypeA(Enum):
	"""4 Members, ALL ... NPRatio"""
	ALL = 0
	CPOWer = 1
	NPOWer = 2
	NPRatio = 3


# noinspection SpellCheckingInspection
class ResultTypeB(Enum):
	"""4 Members, ALL ... PEAK"""
	ALL = 0
	CFACtor = 1
	MEAN = 2
	PEAK = 3


# noinspection SpellCheckingInspection
class ResultTypeC(Enum):
	"""2 Members, AVERage ... IMMediate"""
	AVERage = 0
	IMMediate = 1


# noinspection SpellCheckingInspection
class ResultTypeD(Enum):
	"""1 Members, TOTal ... TOTal"""
	TOTal = 0


# noinspection SpellCheckingInspection
class ResultTypeE(Enum):
	"""3 Members, ALL ... RISing"""
	ALL = 0
	FALLing = 1
	RISing = 2


# noinspection SpellCheckingInspection
class ResultTypeNr5G(Enum):
	"""52 Members, AAPFail ... USTS"""
	AAPFail = 0
	APFail = 1
	ARPFail = 2
	CRESt = 3
	CSIPower = 4
	DS1K = 5
	DS4K = 6
	DSQP = 7
	DSSF = 8
	DSST = 9
	DSTS = 10
	EVM = 11
	EVMPeak = 12
	FERRor = 13
	FSOFfset = 14
	GIMBalance = 15
	IQOFfset = 16
	MID = 17
	MODulation = 18
	NORB = 19
	OSTP = 20
	OVLD = 21
	PCHannel = 22
	POWer = 23
	PPRE = 24
	PSIGnal = 25
	QUADrature = 26
	RSSI = 27
	RSTP = 28
	SD1K = 29
	SD4K = 30
	SDPB = 31
	SDQP = 32
	SDSF = 33
	SDST = 34
	SDTS = 35
	SERRor = 36
	SPFail = 37
	SSPower = 38
	SSTate = 39
	TSDelta = 40
	TSTamp = 41
	UCCD = 42
	UCCH = 43
	UPRach = 44
	US1K = 45
	US4K = 46
	USPB = 47
	USQP = 48
	USSF = 49
	USST = 50
	USTS = 51


# noinspection SpellCheckingInspection
class ResultTypeReference(Enum):
	"""2 Members, PINPut ... POUTput"""
	PINPut = 0
	POUTput = 1


# noinspection SpellCheckingInspection
class ResultTypeStat(Enum):
	"""9 Members, AVG ... TPEak"""
	AVG = 0
	PAVG = 1
	PCTL = 2
	PEAK = 3
	PPCTl = 4
	PSDev = 5
	RPEak = 6
	SDEV = 7
	TPEak = 8


# noinspection SpellCheckingInspection
class RuConfigNheLtf(Enum):
	"""6 Members, S1 ... STA"""
	S1 = 0
	S2 = 1
	S4 = 2
	S6 = 3
	S8 = 4
	STA = 5


# noinspection SpellCheckingInspection
class RuConfigPpdu(Enum):
	"""4 Members, ESU ... TRIG"""
	ESU = 0
	MU = 1
	SU = 2
	TRIG = 3


# noinspection SpellCheckingInspection
class RuSize(Enum):
	"""18 Members, S0 ... SU"""
	S0 = 0
	S106 = 1
	S106s26 = 2
	S242 = 3
	S26 = 4
	S2X996 = 5
	S2X996s484 = 6
	S3X996 = 7
	S3X996s484 = 8
	S484 = 9
	S484s242 = 10
	S4X996 = 11
	S52 = 12
	S52S26 = 13
	S996 = 14
	S996s484 = 15
	S996s484s242 = 16
	SU = 17


# noinspection SpellCheckingInspection
class ScaleScope(Enum):
	"""3 Members, HDECades ... MRANge"""
	HDECades = 0
	MANual = 1
	MRANge = 2


# noinspection SpellCheckingInspection
class ScaleYaxisUnit(Enum):
	"""2 Members, ABS ... PCT"""
	ABS = 0
	PCT = 1


# noinspection SpellCheckingInspection
class ScalingManualMode(Enum):
	"""4 Members, BRANge ... TRANge"""
	BRANge = 0
	OFF = 1
	TBOTtom = 2
	TRANge = 3


# noinspection SpellCheckingInspection
class ScalingMode(Enum):
	"""2 Members, LINear ... LOGarithmic"""
	LINear = 0
	LOGarithmic = 1


# noinspection SpellCheckingInspection
class ScDetailedObject(Enum):
	"""3 Members, DPILot ... LLTF"""
	DPILot = 0
	HELTf = 1
	LLTF = 2


# noinspection SpellCheckingInspection
class SearchArea(Enum):
	"""2 Members, MEMory ... VISible"""
	MEMory = 0
	VISible = 1


# noinspection SpellCheckingInspection
class SearchMode(Enum):
	"""2 Members, FAST ... POPTimzed"""
	FAST = 0
	POPTimzed = 1


# noinspection SpellCheckingInspection
class Section(Enum):
	"""4 Members, DATA ... STS"""
	DATA = 0
	PHR = 1
	SHR = 2
	STS = 3


# noinspection SpellCheckingInspection
class SelectAll(Enum):
	"""1 Members, ALL ... ALL"""
	ALL = 0


# noinspection SpellCheckingInspection
class SelectionRange(Enum):
	"""3 Members, ALL ... SELected"""
	ALL = 0
	CURRent = 1
	SELected = 2


# noinspection SpellCheckingInspection
class SelectionRangeB(Enum):
	"""2 Members, ALL ... CURRent"""
	ALL = 0
	CURRent = 1


# noinspection SpellCheckingInspection
class SelectionScope(Enum):
	"""2 Members, ALL ... SINGle"""
	ALL = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class SelectNone(Enum):
	"""1 Members, NONE ... NONE"""
	NONE = 0


# noinspection SpellCheckingInspection
class SemPowerCategory(Enum):
	"""8 Members, A ... WARE"""
	A = 0
	B = 1
	B1 = 2
	B2 = 3
	HOME = 4
	LARE = 5
	MED = 6
	WARE = 7


# noinspection SpellCheckingInspection
class SemRequirement(Enum):
	"""6 Members, GEN ... NS67"""
	GEN = 0
	NS27 = 1
	NS3 = 2
	NS35 = 3
	NS4 = 4
	NS67 = 5


# noinspection SpellCheckingInspection
class Separator(Enum):
	"""2 Members, COMMa ... POINt"""
	COMMa = 0
	POINt = 1


# noinspection SpellCheckingInspection
class SequencerMode(Enum):
	"""4 Members, CDEFined ... SINGle"""
	CDEFined = 0
	CONTinous = 1
	CONTinuous = 2
	SINGle = 3


# noinspection SpellCheckingInspection
class ServiceBandwidth(Enum):
	"""2 Members, BROadband ... NARRowband"""
	BROadband = 0
	NARRowband = 1


# noinspection SpellCheckingInspection
class ServiceState(Enum):
	"""4 Members, DEViations ... REQired"""
	DEViations = 0
	NAN = 1
	OK = 2
	REQired = 3


# noinspection SpellCheckingInspection
class ShapingMethod(Enum):
	"""2 Members, POLYnomial ... TABLe"""
	POLYnomial = 0
	TABLe = 1


# noinspection SpellCheckingInspection
class ShiftIndex(Enum):
	"""2 Members, NIDCell ... NSHift"""
	NIDCell = 0
	NSHift = 1


# noinspection SpellCheckingInspection
class SidebandPos(Enum):
	"""2 Members, INVerse ... NORMal"""
	INVerse = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class SignalLevel(Enum):
	"""3 Members, HIGH ... OFF"""
	HIGH = 0
	LOW = 1
	OFF = 2


# noinspection SpellCheckingInspection
class SignalModel(Enum):
	"""2 Members, CHIRp ... HOP"""
	CHIRp = 0
	HOP = 1


# noinspection SpellCheckingInspection
class SignalPath(Enum):
	"""8 Members, RX1 ... RX8"""
	RX1 = 0
	RX2 = 1
	RX3 = 2
	RX4 = 3
	RX5 = 4
	RX6 = 5
	RX7 = 6
	RX8 = 7


# noinspection SpellCheckingInspection
class SignalSource(Enum):
	"""2 Members, INSTrument ... SIMulation"""
	INSTrument = 0
	SIMulation = 1


# noinspection SpellCheckingInspection
class SignalSourceB(Enum):
	"""5 Members, ABBand ... RF"""
	ABBand = 0
	AIQ = 1
	DIQ = 2
	FIQ = 3
	RF = 4


# noinspection SpellCheckingInspection
class SignalType(Enum):
	"""3 Members, AC ... DCZero"""
	AC = 0
	DC = 1
	DCZero = 2


# noinspection SpellCheckingInspection
class SingleValue(Enum):
	"""13 Members, ALL ... RHO"""
	ALL = 0
	CFER = 1
	EVMP = 2
	EVMR = 3
	FDER = 4
	FEP = 5
	FERM = 6
	IQOF = 7
	MEP = 8
	MERM = 9
	PEP = 10
	PERM = 11
	RHO = 12


# noinspection SpellCheckingInspection
class Size(Enum):
	"""2 Members, LARGe ... SMALl"""
	LARGe = 0
	SMALl = 1


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class Slot(Enum):
	"""13 Members, S160 ... SL80"""
	S160 = 0
	S320 = 1
	S640 = 2
	SL10 = 3
	SL16 = 4
	SL20 = 5
	SL32 = 6
	SL4 = 7
	SL40 = 8
	SL5 = 9
	SL64 = 10
	SL8 = 11
	SL80 = 12


# noinspection SpellCheckingInspection
class SnmpVersion(Enum):
	"""5 Members, DEFault ... V3"""
	DEFault = 0
	OFF = 1
	V12 = 2
	V123 = 3
	V3 = 4


# noinspection SpellCheckingInspection
class Source(Enum):
	"""13 Members, AM ... VIDeo"""
	AM = 0
	FM = 1
	FOCus = 2
	HVIDeo = 3
	IF = 4
	IF2 = 5
	IQ = 6
	OFF = 7
	OUT1 = 8
	OUT2 = 9
	PM = 10
	SSB = 11
	VIDeo = 12


# noinspection SpellCheckingInspection
class SourceFilePrbs(Enum):
	"""2 Members, FILE ... PRBS"""
	FILE = 0
	PRBS = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class SourceSequence(Enum):
	"""4 Members, CLOop ... PERiodic"""
	CLOop = 0
	MANual = 1
	OLOop = 2
	PERiodic = 3


# noinspection SpellCheckingInspection
class SourceType(Enum):
	"""2 Members, CUSTom ... STANdard"""
	CUSTom = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class SpacingY(Enum):
	"""4 Members, LDB ... PERCent"""
	LDB = 0
	LINear = 1
	LOGarithmic = 2
	PERCent = 3


# noinspection SpellCheckingInspection
class SpanSetting(Enum):
	"""2 Members, FREQuency ... TIME"""
	FREQuency = 0
	TIME = 1


# noinspection SpellCheckingInspection
class SpecialMappingMode(Enum):
	"""3 Members, DIRect ... USER"""
	DIRect = 0
	SEXPansion = 1
	USER = 2


# noinspection SpellCheckingInspection
class SpectrumMaskStandard(Enum):
	"""2 Members, ETSI ... IEEE"""
	ETSI = 0
	IEEE = 1


# noinspection SpellCheckingInspection
class SpectrumWindowType(Enum):
	"""5 Members, BARTlett ... RECTangle"""
	BARTlett = 0
	BLACkman = 1
	HAMMing = 2
	HANNing = 3
	RECTangle = 4


# noinspection SpellCheckingInspection
class SrsPeriodicity(Enum):
	"""12 Members, SL1 ... SL80"""
	SL1 = 0
	SL10 = 1
	SL16 = 2
	SL2 = 3
	SL20 = 4
	SL32 = 5
	SL4 = 6
	SL40 = 7
	SL5 = 8
	SL64 = 9
	SL8 = 10
	SL80 = 11


# noinspection SpellCheckingInspection
class StandardK91(Enum):
	"""3 Members, ETSI ... USER"""
	ETSI = 0
	IEEE = 1
	USER = 2


# noinspection SpellCheckingInspection
class StandardNr5G(Enum):
	"""9 Members, GSM ... WCDMa"""
	GSM = 0
	LTE_1_40 = 1
	LTE_10_00 = 2
	LTE_15_00 = 3
	LTE_20_00 = 4
	LTE_3_00 = 5
	LTE_5_00 = 6
	USER = 7
	WCDMa = 8


# noinspection SpellCheckingInspection
class StandardNr5GExt(Enum):
	"""57 Members, AWLan ... WIMax"""
	AWLan = 0
	BWLan = 1
	CDPD = 2
	D2CDma = 3
	EUTRa = 4
	F19Cdma = 5
	F1D100nr5g = 6
	F1D20nr5g = 7
	F1U100nr5g = 8
	F1U20nr5g = 9
	F2D100nr5g = 10
	F2D200nr5g = 11
	F2U100nr5g = 12
	F2U200nr5g = 13
	F8CDma = 14
	FIS95a = 15
	FIS95c0 = 16
	FIS95c1 = 17
	FJ008 = 18
	FTCDma = 19
	FW3Gppcdma = 20
	FWCDma = 21
	GSM = 22
	L03S = 23
	L05R = 24
	L10R = 25
	L10S = 26
	L14S = 27
	L15R = 28
	L15S = 29
	L20R = 30
	L20S = 31
	M2CDma = 32
	MSR = 33
	NONE = 34
	NR5G = 35
	NR5Glte = 36
	PAPCo25 = 37
	PDC = 38
	PHS = 39
	R19Cdma = 40
	R8CDma = 41
	REUTra = 42
	RFID14443 = 43
	RIS95a = 44
	RIS95c0 = 45
	RIS95c1 = 46
	RJ008 = 47
	RTCDma = 48
	RW3Gppcdma = 49
	RWCDma = 50
	S2CDma = 51
	TCDMa = 52
	TETRa = 53
	USER = 54
	WIBRo = 55
	WIMax = 56


# noinspection SpellCheckingInspection
class State(Enum):
	"""4 Members, ALL ... ON"""
	ALL = 0
	AUTO = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class StaticsticsRange(Enum):
	"""2 Members, CAPTure ... COUNt"""
	CAPTure = 0
	COUNt = 1


# noinspection SpellCheckingInspection
class StatisticMode(Enum):
	"""2 Members, INFinite ... SONLy"""
	INFinite = 0
	SONLy = 1


# noinspection SpellCheckingInspection
class StatisticType(Enum):
	"""2 Members, ALL ... SELected"""
	ALL = 0
	SELected = 1


# noinspection SpellCheckingInspection
class Stepsize(Enum):
	"""2 Members, POINts ... STANdard"""
	POINts = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class StoreType(Enum):
	"""2 Members, CHANnel ... INSTrument"""
	CHANnel = 0
	INSTrument = 1


# noinspection SpellCheckingInspection
class StsFormat(Enum):
	"""4 Members, F0 ... F3"""
	F0 = 0
	F1 = 1
	F2 = 2
	F3 = 3


# noinspection SpellCheckingInspection
class StsLength(Enum):
	"""5 Members, L128 ... L64"""
	L128 = 0
	L16 = 1
	L256 = 2
	L32 = 3
	L64 = 4


# noinspection SpellCheckingInspection
class StsSegments(Enum):
	"""4 Members, S1 ... S4"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class SubBlockGaps(Enum):
	"""7 Members, AB ... GH"""
	AB = 0
	BC = 1
	CD = 2
	DE = 3
	EF = 4
	FG = 5
	GH = 6


# noinspection SpellCheckingInspection
class SubcarrierSpacing(Enum):
	"""8 Members, SS120 ... X60"""
	SS120 = 0
	SS15 = 1
	SS240 = 2
	SS30 = 3
	SS480 = 4
	SS60 = 5
	SS960 = 6
	X60 = 7


# noinspection SpellCheckingInspection
class SubCarrSpacingOref(Enum):
	"""3 Members, CSIRs ... TRS"""
	CSIRs = 0
	NONE = 1
	TRS = 2


# noinspection SpellCheckingInspection
class SubCarrSpacingPrach(Enum):
	"""6 Members, SS1_25 ... SS60"""
	SS1_25 = 0
	SS120 = 1
	SS15 = 2
	SS30 = 3
	SS5 = 4
	SS60 = 5


# noinspection SpellCheckingInspection
class SubwindowSize(Enum):
	"""2 Members, FULL ... SPLit"""
	FULL = 0
	SPLit = 1


# noinspection SpellCheckingInspection
class SummaryMode(Enum):
	"""2 Members, AVERage ... SINGle"""
	AVERage = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class SweepMode(Enum):
	"""2 Members, AUTO ... SINGle"""
	AUTO = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class SweepModeB(Enum):
	"""2 Members, AUTO ... ESPectrum"""
	AUTO = 0
	ESPectrum = 1


# noinspection SpellCheckingInspection
class SweepModeC(Enum):
	"""3 Members, AUTO ... LIST"""
	AUTO = 0
	ESPectrum = 1
	LIST = 2


# noinspection SpellCheckingInspection
class SweepModeHalfDec(Enum):
	"""3 Members, FFT ... NORMal"""
	FFT = 0
	IQFFt = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class SweepModePhNoise(Enum):
	"""4 Members, AVERaged ... NORMal"""
	AVERaged = 0
	FAST = 1
	MANual = 2
	NORMal = 3


# noinspection SpellCheckingInspection
class SweepOptimize(Enum):
	"""3 Members, AUTO ... SPEed"""
	AUTO = 0
	DYNamic = 1
	SPEed = 2


# noinspection SpellCheckingInspection
class SweepStatisticMode(Enum):
	"""2 Members, IQAVeraging ... TRACe"""
	IQAVeraging = 0
	TRACe = 1


# noinspection SpellCheckingInspection
class SweepType(Enum):
	"""3 Members, AUTO ... SWEep"""
	AUTO = 0
	FFT = 1
	SWEep = 2


# noinspection SpellCheckingInspection
class SweepTypeNr5G(Enum):
	"""2 Members, AUTO ... FFT"""
	AUTO = 0
	FFT = 1


# noinspection SpellCheckingInspection
class SymbolSelection(Enum):
	"""3 Members, ALL ... PATTern"""
	ALL = 0
	DATA = 1
	PATTern = 2


# noinspection SpellCheckingInspection
class SyncDomain(Enum):
	"""4 Members, IQDirect ... TRIGger"""
	IQDirect = 0
	IQPDiff = 1
	MAGNitude = 2
	TRIGger = 3


# noinspection SpellCheckingInspection
class Synchronization(Enum):
	"""2 Members, ALL ... NONE"""
	ALL = 0
	NONE = 1


# noinspection SpellCheckingInspection
class SyncMode(Enum):
	"""2 Members, MEAS ... SYNC"""
	MEAS = 0
	SYNC = 1


# noinspection SpellCheckingInspection
class SyncSignalOffsetReference(Enum):
	"""2 Members, RPA ... TXBW"""
	RPA = 0
	TXBW = 1


# noinspection SpellCheckingInspection
class SyncSignalPattern(Enum):
	"""5 Members, A ... E"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4


# noinspection SpellCheckingInspection
class SystemStatus(Enum):
	"""3 Members, ERR ... WARN"""
	ERR = 0
	OK = 1
	WARN = 2


# noinspection SpellCheckingInspection
class TableItemK18(Enum):
	"""35 Members, ADRoop ... VCC"""
	ADRoop = 0
	AMWidth = 1
	APAE = 2
	BBIVoltage = 3
	BBPower = 4
	BBQVoltage = 5
	CFIN = 6
	CFOU = 7
	FERRor = 8
	GAIN = 9
	GIMBalance = 10
	ICC = 11
	IQIMbalance = 12
	IQOFfset = 13
	MERRor = 14
	OBW = 15
	OUTP1db = 16
	OUTP2db = 17
	OUTP3db = 18
	P1DB = 19
	P2DB = 20
	P3DB = 21
	PC = 22
	PCPA = 23
	PERRor = 24
	PINPut = 25
	PISensor = 26
	PMWidth = 27
	POSensor = 28
	POUTput = 29
	QERRor = 30
	REVM = 31
	RMEVm = 32
	SRERror = 33
	VCC = 34


# noinspection SpellCheckingInspection
class TableItemK91(Enum):
	"""38 Members, BPILot ... TPPower"""
	BPILot = 0
	CCERror = 1
	CFERror = 2
	EACarriers = 3
	EDCarriers = 4
	EPCarriers = 5
	FTIMe = 6
	GCFactor = 7
	GCFerror = 8
	GGIMbalance = 9
	GIMBalance = 10
	GIOFfset = 11
	IOFFset = 12
	IQSKew = 13
	MPOWer = 14
	PBERate = 15
	PEVM = 16
	PPOWer = 17
	PVERror = 18
	QERRor = 19
	QOFFset = 20
	RALL = 21
	RCFactor = 22
	RCFerror = 23
	RCPerror = 24
	RMCHpower = 25
	RMCPower = 26
	RPPower = 27
	RSCerror = 28
	RTIMe = 29
	SALL = 30
	SCERror = 31
	SEACarriers = 32
	SEDCarriers = 33
	SEPCarriers = 34
	TALL = 35
	TCFactor = 36
	TPPower = 37


# noinspection SpellCheckingInspection
class TableItemK9X(Enum):
	"""35 Members, RxAll_CenterFreqError ... TxAll_QuadratureOffset"""
	RxAll_CenterFreqError = "RCFerror"
	RxAll_CommonPhaseError = "RCPerror"
	RxAll_CrestFactor = "RCFactor"
	RxAll_MimoChannelPower = "RMCHpower"
	RxAll_MimoCrossPower = "RMCPower"
	RxAll_PpduPower = "RPPower"
	RxAll_SymbolClockError = "RSCerror"
	StreamAll_CenterFreqError = "GCFerror"
	StreamAll_ChipClockError = "CCERror"
	StreamAll_CrestFactor = "GCFactor"
	StreamAll_EvmAllCarriers = "SEACarriers"
	StreamAll_EvmDataCarriers = "SEDCarriers"
	StreamAll_EvmPilotCarriers = "SEPCarriers"
	StreamAll_FallTime = "FTIMe"
	StreamAll_GainImbalance = "GGIMbalance"
	StreamAll_IqOffset = "GIOFfset"
	StreamAll_MeanPower = "MPOWer"
	StreamAll_PeakPower = "PPOWer"
	StreamAll_PeakVectorError = "PVERror"
	StreamAll_PilotBitErrorRate = "BPILot"
	StreamAll_PpduEvm = "PEVM"
	StreamAll_QuadratureError = "QERRor"
	StreamAll_RiseTime = "RTIMe"
	SumGlobal_CenterFreqError = "CFERror"
	SumGlobal_EvmAllCarriers = "EACarriers"
	SumGlobal_EvmDataCarriers = "EDCarriers"
	SumGlobal_EvmPilotCarriers = "EPCarriers"
	SumGlobal_PilotBitErrorRate = "PBERate"
	SumGlobal_SymbolClockError = "SCERror"
	TxAll_CrestFactor = "TCFactor"
	TxAll_GainImbalance = "GIMBalance"
	TxAll_IqOffset = "IOFSset"
	TxAll_IqSkew = "IQSKew"
	TxAll_PpduPower = "TPPower"
	TxAll_QuadratureOffset = "QOFFset"


# noinspection SpellCheckingInspection
class TechnologyStandardA(Enum):
	"""26 Members, GSM ... WCDMa"""
	GSM = 0
	LTE_1_40 = 1
	LTE_10_00 = 2
	LTE_15_00 = 3
	LTE_20_00 = 4
	LTE_3_00 = 5
	LTE_5_00 = 6
	NR5G_fr1_10 = 7
	NR5G_fr1_100 = 8
	NR5G_fr1_15 = 9
	NR5G_fr1_20 = 10
	NR5G_fr1_25 = 11
	NR5G_fr1_30 = 12
	NR5G_fr1_40 = 13
	NR5G_fr1_5 = 14
	NR5G_fr1_50 = 15
	NR5G_fr1_60 = 16
	NR5G_fr1_70 = 17
	NR5G_fr1_80 = 18
	NR5G_fr1_90 = 19
	NR5G_fr2_100 = 20
	NR5G_fr2_200 = 21
	NR5G_fr2_400 = 22
	NR5G_fr2_50 = 23
	USER = 24
	WCDMa = 25


# noinspection SpellCheckingInspection
class TechnologyStandardB(Enum):
	"""60 Members, AWLan ... WIMax"""
	AWLan = 0
	BWLan = 1
	CDPD = 2
	D2CDma = 3
	EUTRa = 4
	F19Cdma = 5
	F1D100nr5g = 6
	F1D20nr5g = 7
	F1U100nr5g = 8
	F1U20nr5g = 9
	F2D100nr5g = 10
	F2D200nr5g = 11
	F2U100nr5g = 12
	F2U200nr5g = 13
	F8CDma = 14
	FIS95a = 15
	FIS95c0 = 16
	FIS95c1 = 17
	FJ008 = 18
	FTCDma = 19
	FW3Gppcdma = 20
	FWCDma = 21
	GSM = 22
	L03R = 23
	L03S = 24
	L05R = 25
	L05S = 26
	L10R = 27
	L10S = 28
	L14R = 29
	L14S = 30
	L15R = 31
	L15S = 32
	L20R = 33
	L20S = 34
	M2CDma = 35
	MSR = 36
	NONE = 37
	NR5G = 38
	NR5Glte = 39
	PAPCo25 = 40
	PDC = 41
	PHS = 42
	R19Cdma = 43
	R8CDma = 44
	REUTra = 45
	RFID14443 = 46
	RIS95a = 47
	RIS95c0 = 48
	RIS95c1 = 49
	RJ008 = 50
	RTCDma = 51
	RW3Gppcdma = 52
	RWCDma = 53
	S2CDma = 54
	TCDMa = 55
	TETRa = 56
	USER = 57
	WIBRo = 58
	WIMax = 59


# noinspection SpellCheckingInspection
class TechnologyStandardDdem(Enum):
	"""3 Members, DECT ... GSM"""
	DECT = 0
	EDGE = 1
	GSM = 2


# noinspection SpellCheckingInspection
class Temperature(Enum):
	"""2 Members, COLD ... HOT"""
	COLD = 0
	HOT = 1


# noinspection SpellCheckingInspection
class TestCaseNr5G(Enum):
	"""14 Members, NONE ... OT9"""
	NONE = 0
	OT1 = 1
	OT10 = 2
	OT11 = 3
	OT12 = 4
	OT13 = 5
	OT2 = 6
	OT3 = 7
	OT4 = 8
	OT5 = 9
	OT6 = 10
	OT7 = 11
	OT8 = 12
	OT9 = 13


# noinspection SpellCheckingInspection
class TimeFormat(Enum):
	"""2 Members, DE ... US"""
	DE = 0
	US = 1


# noinspection SpellCheckingInspection
class TimeLimitUnit(Enum):
	"""2 Members, S ... SYM"""
	S = 0
	SYM = 1


# noinspection SpellCheckingInspection
class TimeOrder(Enum):
	"""2 Members, AFTer ... BEFore"""
	AFTer = 0
	BEFore = 1


# noinspection SpellCheckingInspection
class TimeScaling(Enum):
	"""4 Members, MS ... US"""
	MS = 0
	NS = 1
	S = 2
	US = 3


# noinspection SpellCheckingInspection
class TouchscreenState(Enum):
	"""3 Members, FRAMe ... ON"""
	FRAMe = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class TraceAutoMode(Enum):
	"""2 Members, HYSTeresis ... MEMory"""
	HYSTeresis = 0
	MEMory = 1


# noinspection SpellCheckingInspection
class TraceChannel(Enum):
	"""4 Members, CHANnel1 ... CHANnel4"""
	CHANnel1 = 0
	CHANnel2 = 1
	CHANnel3 = 2
	CHANnel4 = 3


# noinspection SpellCheckingInspection
class TraceDetector(Enum):
	"""6 Members, APEak ... SAMPle"""
	APEak = 0
	AVERage = 1
	NEGative = 2
	POSitive = 3
	RMS = 4
	SAMPle = 5


# noinspection SpellCheckingInspection
class TraceFormat(Enum):
	"""22 Members, BERate ... UPHase"""
	BERate = 0
	BINary = 1
	COMP = 2
	CONF = 3
	CONS = 4
	COVF = 5
	DECimal = 6
	FEYE = 7
	FREQuency = 8
	GDELay = 9
	HEXadecimal = 10
	IEYE = 11
	MAGNitude = 12
	MOVerview = 13
	NONE = 14
	OCTal = 15
	PHASe = 16
	QEYE = 17
	RCONstell = 18
	RIMag = 19
	RSUMmary = 20
	UPHase = 21


# noinspection SpellCheckingInspection
class TraceModeA(Enum):
	"""6 Members, AVERage ... WRITe"""
	AVERage = 0
	MAXHold = 1
	MINHold = 2
	OFF = 3
	VIEW = 4
	WRITe = 5


# noinspection SpellCheckingInspection
class TraceModeB(Enum):
	"""4 Members, AVERage ... WRITe"""
	AVERage = 0
	MAXHold = 1
	MINHold = 2
	WRITe = 3


# noinspection SpellCheckingInspection
class TraceModeC(Enum):
	"""6 Members, AVERage ... WRITe"""
	AVERage = 0
	BLANk = 1
	MAXHold = 2
	MINHold = 3
	VIEW = 4
	WRITe = 5


# noinspection SpellCheckingInspection
class TraceModeD(Enum):
	"""2 Members, MAXHold ... WRITe"""
	MAXHold = 0
	WRITe = 1


# noinspection SpellCheckingInspection
class TraceModeE(Enum):
	"""3 Members, AVERage ... WRITe"""
	AVERage = 0
	MAXHold = 1
	WRITe = 2


# noinspection SpellCheckingInspection
class TraceModeF(Enum):
	"""7 Members, AVERage ... WRITe"""
	AVERage = 0
	BLANk = 1
	DENSity = 2
	MAXHold = 3
	MINHold = 4
	VIEW = 5
	WRITe = 6


# noinspection SpellCheckingInspection
class TraceModeG(Enum):
	"""5 Members, AVERage ... WRITe"""
	AVERage = 0
	MAXHold = 1
	MINHold = 2
	VIEW = 3
	WRITe = 4


# noinspection SpellCheckingInspection
class TraceModeH(Enum):
	"""3 Members, BLANk ... WRITe"""
	BLANk = 0
	VIEW = 1
	WRITe = 2


# noinspection SpellCheckingInspection
class TraceModeJ(Enum):
	"""6 Members, AVER ... WRIT"""
	AVER = 0
	BLANk = 1
	MAXH = 2
	MINH = 3
	VIEW = 4
	WRIT = 5


# noinspection SpellCheckingInspection
class TraceModeK(Enum):
	"""9 Members, AVERage ... WRITe"""
	AVERage = 0
	BLANk = 1
	BURSt = 2
	MAXHold = 3
	MINHold = 4
	PPAVerage = 5
	SELPos = 6
	VIEW = 7
	WRITe = 8


# noinspection SpellCheckingInspection
class TraceNormalizeMode(Enum):
	"""3 Members, MEASured ... REFerence"""
	MEASured = 0
	OFF = 1
	REFerence = 2


# noinspection SpellCheckingInspection
class TraceNumber(Enum):
	"""15 Members, BTOBits ... TRACe6"""
	BTOBits = 0
	BTOFm = 1
	ESPLine = 2
	HMAXhold = 3
	LIST = 4
	PSPectrum = 5
	SGRam = 6
	SPECtrogram = 7
	SPURious = 8
	TRACe1 = 9
	TRACe2 = 10
	TRACe3 = 11
	TRACe4 = 12
	TRACe5 = 13
	TRACe6 = 14


# noinspection SpellCheckingInspection
class TracePresetType(Enum):
	"""3 Members, ALL ... MCM"""
	ALL = 0
	MAM = 1
	MCM = 2


# noinspection SpellCheckingInspection
class TraceReference(Enum):
	"""3 Members, BURSt ... TRIGger"""
	BURSt = 0
	PATTern = 1
	TRIGger = 2


# noinspection SpellCheckingInspection
class TraceRefType(Enum):
	"""4 Members, ERRor ... TCAP"""
	ERRor = 0
	MEAS = 1
	REF = 2
	TCAP = 3


# noinspection SpellCheckingInspection
class TraceResultK18(Enum):
	"""7 Members, BBI ... RF"""
	BBI = 0
	BBPower = 1
	BBQ = 2
	MEAS = 3
	MODel = 4
	REFerence = 5
	RF = 6


# noinspection SpellCheckingInspection
class TraceSmoothing(Enum):
	"""3 Members, LINear ... MEDian"""
	LINear = 0
	LOGarithmic = 1
	MEDian = 2


# noinspection SpellCheckingInspection
class TraceStatistic(Enum):
	"""2 Members, ALL ... SEL"""
	ALL = 0
	SEL = 1


# noinspection SpellCheckingInspection
class TraceStyleSymbol(Enum):
	"""2 Members, DOTS ... VECTor"""
	DOTS = 0
	VECTor = 1


# noinspection SpellCheckingInspection
class TraceSymbols(Enum):
	"""4 Members, BARS ... ON"""
	BARS = 0
	DOTS = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class TraceTypeDdem(Enum):
	"""15 Members, MSTRace ... TRACe6"""
	MSTRace = 0
	PSTRace = 1
	STRace = 2
	TRACe1 = 3
	TRACe1i = 4
	TRACe1r = 5
	TRACe2 = 6
	TRACe2i = 7
	TRACe2r = 8
	TRACe3 = 9
	TRACe3i = 10
	TRACe3r = 11
	TRACe4 = 12
	TRACe5 = 13
	TRACe6 = 14


# noinspection SpellCheckingInspection
class TraceTypeIxNone(Enum):
	"""7 Members, NONE ... TRACe6"""
	NONE = 0
	TRACe1 = 1
	TRACe2 = 2
	TRACe3 = 3
	TRACe4 = 4
	TRACe5 = 5
	TRACe6 = 6


# noinspection SpellCheckingInspection
class TraceTypeK10X(Enum):
	"""24 Members, FAL1 ... TRACe8"""
	FAL1 = 0
	FAL2 = 1
	FALLing1 = 2
	FALLing2 = 3
	LIST = 4
	OFF1 = 5
	OFF2 = 6
	PBCH = 7
	PCFich = 8
	PDCCh = 9
	PDSCh = 10
	PHICh = 11
	RIS1 = 12
	RIS2 = 13
	RISing1 = 14
	RISing2 = 15
	TRACe1 = 16
	TRACe2 = 17
	TRACe3 = 18
	TRACe4 = 19
	TRACe5 = 20
	TRACe6 = 21
	TRACe7 = 22
	TRACe8 = 23


# noinspection SpellCheckingInspection
class TraceTypeK30(Enum):
	"""4 Members, TRACe1 ... TRACe4"""
	TRACe1 = 0
	TRACe2 = 1
	TRACe3 = 2
	TRACe4 = 3


# noinspection SpellCheckingInspection
class TraceTypeK60(Enum):
	"""8 Members, SGRam ... TRACe6"""
	SGRam = 0
	SPECtrogram = 1
	TRACe1 = 2
	TRACe2 = 3
	TRACe3 = 4
	TRACe4 = 5
	TRACe5 = 6
	TRACe6 = 7


# noinspection SpellCheckingInspection
class TraceTypeList(Enum):
	"""7 Members, LIST ... TRACe6"""
	LIST = 0
	TRACe1 = 1
	TRACe2 = 2
	TRACe3 = 3
	TRACe4 = 4
	TRACe5 = 5
	TRACe6 = 6


# noinspection SpellCheckingInspection
class TraceTypeNr5G(Enum):
	"""22 Members, COReset ... TRACe9"""
	COReset = 0
	FALLing = 1
	LIST = 2
	OFF = 3
	PBCH = 4
	RISing = 5
	TRACe1 = 6
	TRACe10 = 7
	TRACe11 = 8
	TRACe12 = 9
	TRACe13 = 10
	TRACe14 = 11
	TRACe15 = 12
	TRACe16 = 13
	TRACe2 = 14
	TRACe3 = 15
	TRACe4 = 16
	TRACe5 = 17
	TRACe6 = 18
	TRACe7 = 19
	TRACe8 = 20
	TRACe9 = 21


# noinspection SpellCheckingInspection
class TraceTypeNumeric(Enum):
	"""6 Members, TRACe1 ... TRACe6"""
	TRACe1 = 0
	TRACe2 = 1
	TRACe3 = 2
	TRACe4 = 3
	TRACe5 = 4
	TRACe6 = 5


# noinspection SpellCheckingInspection
class TrBlockScaleFactor(Enum):
	"""3 Members, HALF ... QUAR"""
	HALF = 0
	ONE = 1
	QUAR = 2


# noinspection SpellCheckingInspection
class TriggerOutType(Enum):
	"""3 Members, DEVice ... UDEFined"""
	DEVice = 0
	TARMed = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class TriggerPort(Enum):
	"""4 Members, EXT1 ... OFF"""
	EXT1 = 0
	EXT2 = 1
	HOST = 2
	OFF = 3


# noinspection SpellCheckingInspection
class TriggerSeqSource(Enum):
	"""40 Members, ACVideo ... VIDeo"""
	ACVideo = 0
	AF = 1
	AM = 2
	AMRelative = 3
	BBPower = 4
	EXT2 = 5
	EXT3 = 6
	EXT4 = 7
	EXTernal = 8
	FM = 9
	GP0 = 10
	GP1 = 11
	GP2 = 12
	GP3 = 13
	GP4 = 14
	GP5 = 15
	IFPower = 16
	IMMediate = 17
	INTernal = 18
	IQPower = 19
	LXI = 20
	MAGNitude = 21
	MAIT = 22
	MANual = 23
	MASK = 24
	PM = 25
	PMTRigger = 26
	PSENsor = 27
	RFPower = 28
	SLEFt = 29
	SMONo = 30
	SMPX = 31
	SPILot = 32
	SRDS = 33
	SRIGht = 34
	SSTereo = 35
	TDTRigger = 36
	TIME = 37
	TV = 38
	VIDeo = 39


# noinspection SpellCheckingInspection
class TriggerSourceB(Enum):
	"""30 Members, ACVideo ... TV"""
	ACVideo = 0
	AF = 1
	AM = 2
	AMRelative = 3
	BBPower = 4
	EXT2 = 5
	EXT3 = 6
	EXT4 = 7
	EXTernal = 8
	FM = 9
	GP0 = 10
	GP1 = 11
	GP2 = 12
	GP3 = 13
	GP4 = 14
	GP5 = 15
	IFPower = 16
	IMMediate = 17
	IQPower = 18
	MAGNitude = 19
	PM = 20
	RFPower = 21
	SLEFt = 22
	SMONo = 23
	SMPX = 24
	SPILot = 25
	SRDS = 26
	SRIGht = 27
	SSTereo = 28
	TV = 29


# noinspection SpellCheckingInspection
class TriggerSourceC(Enum):
	"""9 Members, EXT2 ... TIME"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	IMMediate = 4
	IQPower = 5
	PSENsor = 6
	RFPower = 7
	TIME = 8


# noinspection SpellCheckingInspection
class TriggerSourceD(Enum):
	"""10 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXT4 = 2
	EXTernal = 3
	IFPower = 4
	IMMediate = 5
	IQPower = 6
	PSENsor = 7
	RFPower = 8
	VIDeo = 9


# noinspection SpellCheckingInspection
class TriggerSourceE(Enum):
	"""8 Members, EXT2 ... RFPower"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	IMMediate = 4
	IQPower = 5
	MANual = 6
	RFPower = 7


# noinspection SpellCheckingInspection
class TriggerSourceF(Enum):
	"""3 Members, EXTernal ... IMMediate"""
	EXTernal = 0
	IFPower = 1
	IMMediate = 2


# noinspection SpellCheckingInspection
class TriggerSourceG(Enum):
	"""11 Members, EXT2 ... TIME"""
	EXT2 = 0
	EXT3 = 1
	EXTernal = 2
	IFPower = 3
	IMMediate = 4
	INTernal = 5
	IQPower = 6
	MANual = 7
	PSENsor = 8
	RFPower = 9
	TIME = 10


# noinspection SpellCheckingInspection
class TriggerSourceH(Enum):
	"""29 Members, AF ... VIDeo"""
	AF = 0
	AM = 1
	AMRelative = 2
	BBPower = 3
	EXT2 = 4
	EXT3 = 5
	EXTernal = 6
	FM = 7
	IFPower = 8
	IMMediate = 9
	IQPower = 10
	LXI = 11
	MANual = 12
	MASK = 13
	PM = 14
	PSENsor = 15
	RFPower = 16
	SLEFt = 17
	SMONo = 18
	SMPX = 19
	SPILot = 20
	SRDS = 21
	SRIGht = 22
	SSTereo = 23
	TDTRigger = 24
	TIME = 25
	TUNit = 26
	TV = 27
	VIDeo = 28


# noinspection SpellCheckingInspection
class TriggerSourceJ(Enum):
	"""13 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXT4 = 2
	EXTernal = 3
	IFPower = 4
	IMMediate = 5
	IQPower = 6
	MANual = 7
	PSENsor = 8
	RFPower = 9
	TIME = 10
	TUNit = 11
	VIDeo = 12


# noinspection SpellCheckingInspection
class TriggerSourceListPower(Enum):
	"""10 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXT4 = 2
	EXTernal = 3
	IFPower = 4
	IMMediate = 5
	LINE = 6
	LXI = 7
	RFPower = 8
	VIDeo = 9


# noinspection SpellCheckingInspection
class TriggerSourceLte(Enum):
	"""13 Members, BBPower ... TUNit"""
	BBPower = 0
	EXT2 = 1
	EXT3 = 2
	EXT4 = 3
	EXTernal = 4
	IFPower = 5
	IMMediate = 6
	IQPower = 7
	MANual = 8
	PSENsor = 9
	RFPower = 10
	TIME = 11
	TUNit = 12


# noinspection SpellCheckingInspection
class TriggerSourceMpower(Enum):
	"""7 Members, EXT2 ... VIDeo"""
	EXT2 = 0
	EXT3 = 1
	EXT4 = 2
	EXTernal = 3
	IFPower = 4
	RFPower = 5
	VIDeo = 6


# noinspection SpellCheckingInspection
class TuningRange(Enum):
	"""2 Members, SMALl ... WIDE"""
	SMALl = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class TypeLte(Enum):
	"""2 Members, ANCHor ... NANChor"""
	ANCHor = 0
	NANChor = 1


# noinspection SpellCheckingInspection
class UnitMode(Enum):
	"""2 Members, DB ... PCT"""
	DB = 0
	PCT = 1


# noinspection SpellCheckingInspection
class UnitReference(Enum):
	"""2 Members, ABS ... REL"""
	ABS = 0
	REL = 1


# noinspection SpellCheckingInspection
class UpDownDirection(Enum):
	"""2 Members, DOWN ... UP"""
	DOWN = 0
	UP = 1


# noinspection SpellCheckingInspection
class UsagePdcch(Enum):
	"""17 Members, AIRN ... TSRN"""
	AIRN = 0
	CIRN = 1
	CRNT = 2
	CSRN = 3
	INTR = 4
	MCSC = 5
	MSGB = 6
	PRNT = 7
	PSRN = 8
	RNRN = 9
	SFIR = 10
	SIRN = 11
	SPCR = 12
	TCRN = 13
	TPUC = 14
	TPUS = 15
	TSRN = 16


# noinspection SpellCheckingInspection
class UserLevel(Enum):
	"""3 Members, AUTH ... PRIV"""
	AUTH = 0
	NOAuth = 1
	PRIV = 2


# noinspection SpellCheckingInspection
class UwbDemodMode(Enum):
	"""3 Members, BPRF ... HRP"""
	BPRF = 0
	HPRF = 1
	HRP = 2


# noinspection SpellCheckingInspection
class WbBandwidth(Enum):
	"""4 Members, AUTO ... BW512"""
	AUTO = 0
	BW1200 = 1
	BW160 = 2
	BW512 = 3


# noinspection SpellCheckingInspection
class WindowDirection(Enum):
	"""4 Members, ABOVe ... RIGHt"""
	ABOVe = 0
	BELow = 1
	LEFT = 2
	RIGHt = 3


# noinspection SpellCheckingInspection
class WindowDirReplace(Enum):
	"""5 Members, ABOVe ... RIGHt"""
	ABOVe = 0
	BELow = 1
	LEFT = 2
	REPLace = 3
	RIGHt = 4


# noinspection SpellCheckingInspection
class WindowFunction(Enum):
	"""5 Members, BHARris ... SWEPt"""
	BHARris = 0
	CHEByshev = 1
	GAUSsian = 2
	RECTangular = 3
	SWEPt = 4


# noinspection SpellCheckingInspection
class WindowName(Enum):
	"""1 Members, FOCus ... FOCus"""
	FOCus = 0


# noinspection SpellCheckingInspection
class WindowTypeBase(Enum):
	"""5 Members, Diagram ... Spectrogram"""
	Diagram = "DIAGram"
	MarkePeakList = "PEAKlist"
	MarkeTable = "MTABle"
	ResultSummary = "RSUMmary"
	Spectrogram = "SGRam"


# noinspection SpellCheckingInspection
class WindowTypeIq(Enum):
	"""9 Members, Diagram ... Spectrum"""
	Diagram = "DIAGram"
	IqImagReal = "RIMAG"
	IqVector = "VECT"
	Magnitude = "MAGN"
	MarkePeakList = "PEAKlist"
	MarkeTable = "MTABle"
	ResultSummary = "RSUMmary"
	Spectrogram = "SGRam"
	Spectrum = "FREQ"


# noinspection SpellCheckingInspection
class WindowTypeK10X(Enum):
	"""39 Members, AllocIdVsSymbolXcarrier ... UeRsPhase"""
	AllocIdVsSymbolXcarrier = "AISC"
	AllocSummary = "ASUM"
	BeamformingAllocSummary = "URWA"
	Bitstream = "BSTR"
	CaptureBuffer = "CBUF"
	CCDF = "CCDF"
	CellRsMagnitude = "CRWM"
	CellRsPhase = "CRWP"
	ChannelDecoderResults = "CDEC"
	ChannelFlatness = "FLAT"
	ConstellationDiagram = "CONS"
	CsiRsMagnitude = "IRWM"
	CsiRsPhase = "IRWP"
	Diagram = "DIAG"
	EvmVsCarrier = "EVCA"
	EvmVsRb = "EVRP"
	EvmVsSubframe = "EVSU"
	EvmVsSymbol = "EVSY"
	EvmVsSymbolXcarrier = "EVSC"
	FallingPeriod = "FALL"
	FreqErrorVsSymbol = "FEVS"
	GroupDelay = "GDEL"
	InbandEmission = "IE"
	InbandEmissionAll = "IEA"
	MarkerTable = "MTAB"
	OnOffPowerList = "OOPL"
	PeakList = "PEAK"
	PowerSpectrum = "PSPE"
	PowerVsRbPdsch = "PVRP"
	PowerVsRbRs = "PVRR"
	PowerVsSymbolXcarrier = "PVSC"
	ResultSummary = "RSUM"
	RisingPeriod = "RIS"
	SpectrumFlatness = "SFL"
	SpectrumFlatnessDiff = "SFD"
	SpectrumFlatnessSrs = "SFSR"
	TimeAlignmentError = "TAL"
	UeRsMagnitude = "URWM"
	UeRsPhase = "URWP"


# noinspection SpellCheckingInspection
class WindowTypeK149(Enum):
	"""11 Members, ChipPhaseJitter ... SymbolTimeJitter"""
	ChipPhaseJitter = "CJPH"
	ChipTimeJitter = "CJT"
	CorrelatedPulse = "XCOR"
	MagnitudeCapture = "MCAP"
	MarkerTable = "MTAB"
	PacketInsights = "PINS"
	PacketSpectrum = "PSP"
	Pulse = "PULS"
	ResultSummary = "RSUM"
	SymbolPhaseJitter = "SJPH"
	SymbolTimeJitter = "SJT"


# noinspection SpellCheckingInspection
class WindowTypeK14X(Enum):
	"""28 Members, AllocIDvsSymbolXcarrier ... TimeAlignmentError"""
	AllocIDvsSymbolXcarrier = "AISC"
	AllocSummary = "ASUM"
	BeamformSummary = "BSUM"
	CaptureBuffer = "CBUF"
	Ccdf = "CCDF"
	ChannelDecoder = "CDEC"
	ChannelFlatness = "FLAT"
	CombinedResultSummary = "CMSummary"
	ConstellationDiagram = "CONS"
	Diagram = "DIAG"
	EvmVsCarrier = "EVCA"
	EvmVsRb = "EVRP"
	EvmVsSymbol = "EVSY"
	EvmVsSymbolXcarrier = "EVSC"
	FallingPeriod = "FALL"
	FreqErrorVsSubframe = "FVSU"
	FreqErrorVsSymbol = "FEVS"
	MarkerTable = "MTAB"
	OnOffPowerList = "OOPL"
	PeakList = "PEAK"
	PowerSpectrum = "PSPE"
	PowerVsSymbolXcarrier = "PVSC"
	ResultSummary = "RSUM"
	RisingPeriod = "RIS"
	RsMagnitude = "RSMA"
	RsPhase = "RSWP"
	RsPhaseDifference = "RSPD"
	TimeAlignmentError = "TAL"


# noinspection SpellCheckingInspection
class WindowTypeK17(Enum):
	"""8 Members, Gain ... PhaseVsFreqRefData"""
	Gain = "GAIN"
	GroupDelayVsFreq = "GDELay"
	MagnVsFreq = "MAGNitude"
	MagnVsFreqRefData = "RMAGnitude"
	MarkerTable = "MTABle"
	PhaseDifferenceVsFreq = "DPHase"
	PhaseVsFreq = "PHASe"
	PhaseVsFreqRefData = "RPHase"


# noinspection SpellCheckingInspection
class WindowTypeK18(Enum):
	"""33 Members, AdjChPowerTable ... VccVsPower"""
	AdjChPowerTable = "ACP"
	AmAm = "AMAM"
	AmPm = "AMPM"
	ChannelRespMagnitude = "MRES"
	ChannelRespPhase = "PRES"
	DdpdResults = "DDPD"
	EvmVsPower = "AMEVm"
	GainCompression = "GCOMpression"
	GainDeviationVsTime = "GDVTime"
	GroupDelay = "GDEL"
	IccVsPower = "ICCPower"
	IpartMagnitudeCapture = "IMAGnitude"
	IpartSpectrumFft = "ISPectrum"
	MarkerTable = "MTABle"
	MemoryDpdCoefficients = "MDPD"
	PaeInputPower = "PAEI"
	PaeOutputPower = "PAEO"
	PaeTime = "PAETime"
	ParameterSweepDiagram = "PSWeep"
	ParameterSweepTable = "PTABle"
	PhaseDeviationVsTime = "PDVTime"
	PowerVsTimeIxQ = "PVTime"
	QpartMagnitudeCapture = "QMAGnitude"
	QpartSpectrumFft = "QSPectrum"
	RawEvm = "REVM"
	ResultSummaryTable = "RTABle"
	RfMagnitudeCapture = "RFMagnitude"
	SpectrumEvm = "SEVM"
	SpectrumFft = "RFSPectrum"
	StatisticsTable = "STAB"
	TimeDomain = "TDOMain"
	VccVsIcc = "VICC"
	VccVsPower = "VCCPower"


# noinspection SpellCheckingInspection
class WindowTypeK30(Enum):
	"""12 Members, CalPowerCold ... YfactorResult"""
	CalPowerCold = "CPCold"
	CalPowerHot = "CPHot"
	CalYfactor = "CYFactor"
	EnrMeasured = "ENR"
	GainResult = "GAIN"
	MarkerTable = "MTABle"
	NoiseFigureResult = "NOISe"
	NoiseTemperatureResult = "TEMPerature"
	PowerColdResult = "PCOLd"
	PowerHotResult = "PHOT"
	ResultTable = "RESults"
	YfactorResult = "YFACtor"


# noinspection SpellCheckingInspection
class WindowTypeK40(Enum):
	"""9 Members, FrequencyDrift ... SweepResultList"""
	FrequencyDrift = "FDRift"
	MarkerTable = "MTABle"
	PhaseNoiseDiagram = "PNOise"
	ResidualNoiseTable = "RNOise"
	SpectrumMonitor = "SPECtrum"
	SpotNoiseTable = "SNOise"
	SpurList = "SPURs"
	StabilityFreqLevel = "STABility"
	SweepResultList = "SRESults"


# noinspection SpellCheckingInspection
class WindowTypeK50(Enum):
	"""5 Members, MarkerTable ... SpurDetectionTable"""
	MarkerTable = "MTABle"
	NoiseFloorEstimate = "NESTimate"
	SpectralOverview = "SOVerview"
	SpurDetectionSpectrum = "SDETection"
	SpurDetectionTable = "SDTable"


# noinspection SpellCheckingInspection
class WindowTypeK6(Enum):
	"""18 Members, CorrelatedMagnitudeCapture ... ResultRangeSpectrum"""
	CorrelatedMagnitudeCapture = "CMCapture"
	CorrelatedPulseMagnitude = "CPMagnitude"
	MagnitudeCaptureBuffer = "MCAPture"
	MarkerTable = "MTABle"
	ParamDistribution = "PDIStribution"
	ParameterSpectrum = "PSPectrum"
	ParameterTrend = "PTRend"
	PulseFreq = "PFRequency"
	PulseFreqError = "PFERror"
	PulseIq = "PIAQ"
	PulseMagnitude = "PMAGnitude"
	PulsePhase = "PPHase"
	PulsePhaseError = "PPERor"
	PulsePhaseWrapped = "PPWrapped"
	PulsePulseSpectrum = "PPSPectrum"
	PulseResults = "PRESults"
	PulseStatistics = "PSTatistics"
	ResultRangeSpectrum = "RRSPectrum"


# noinspection SpellCheckingInspection
class WindowTypeK60(Enum):
	"""15 Members, ChirpRateTimeDomain ... StatisticsTable"""
	ChirpRateTimeDomain = "CRTime"
	FmTimeDomain = "FMTime"
	FreqDeviationTimeDomain = "FDEViation"
	IqTimeDomain = "IQTime"
	MarkerTable = "MTABle"
	ParameterDistribution = "PDIStribution"
	ParameterTrend = "PTRend"
	PhaseDeviationTimeDomain = "PDEViation"
	PmTimeDomain = "PMTime"
	PMTimeDomainWrapped = "PMWRapped"
	ResultsTable = "RTABle"
	RfPowerTimeDomain = "RFPTime"
	RfSpectrum = "RFSPectrum"
	Spectrogram = "SGR"
	StatisticsTable = "STABle"


# noinspection SpellCheckingInspection
class WindowTypeK7(Enum):
	"""11 Members, AmSpectrum ... RfTimeDomain"""
	AmSpectrum = "'XTIM:AM:RELative:AFSPectrum'"
	AmTimeDomain = "'XTIM:AM:RELative'"
	FmSpectrum = "'XTIM:FM:AFSPectrum'"
	FmTimeDomain = "'XTIM:FM'"
	MarkerPeakList = "PEAKlist"
	MarkerTable = "MTABle"
	PmSpectrum = "'XTIM:PM:AFSPectrum'"
	PmTimeDomain = "'XTIM:PM'"
	ResultSummary = "RSUMmary"
	RfSpectrum = "'XTIM:SPECtrum'"
	RfTimeDomain = "'XTIM:AM'"


# noinspection SpellCheckingInspection
class WindowTypeK70(Enum):
	"""9 Members, CaptureBufferMagnAbs ... SymbolsHexa"""
	CaptureBufferMagnAbs = "CBUFfer"
	Equalizer = "EQUalizer"
	ErrorVectorMagnitude = "EVECtor"
	MeasMagnRel = "MEAS"
	ModulationAccuracy = "MACCuracy"
	ModulationErrors = "MERRor"
	MultiSource = "MCOMbination"
	RefMagnRel = "REF"
	SymbolsHexa = "SYMB"


# noinspection SpellCheckingInspection
class WindowTypeK91(Enum):
	"""32 Members, AmAm ... UnusedToneErrorSumm"""
	AmAm = "AMAM"
	AmEvm = "AMEV"
	AmPm = "AMPM"
	Bitstream = "BITStream"
	Constellation = "CONStellation"
	ConstellationVsCarrier = "CVCarrier"
	Diagram = "DIAGram"
	EvmVsCarrier = "EVCarrier"
	EvmVsChip = "EVCHip"
	EvmVsSymbol = "EVSYmbol"
	FftSpectrum = "FSPectrum"
	FreqErrorVsPreamble = "FEVPreamble"
	GainImbalanceVsCarrier = "GAIN"
	GroupDelay = "GDELay"
	MagnitudeCapture = "CMEMory"
	MarkerPeakList = "PEAKlist"
	MarkerTable = "MTABle"
	PhaseErrorVsPreamble = "PEVPreamble"
	PhaseTrackingVsSymbol = "PTRacking"
	PwrVsTimeFallingEdge = "PFALling"
	PwrVsTimeFullPpdu = "PFPPdu"
	PwrVsTimeRisingEdge = "PRISing"
	QuadratureErrorVsCarrier = "QUAD"
	ResultSummary = "RSUMmary"
	ResultSummDetailed = "RSDetailed"
	ResultSummGlobal = "RSGLobal"
	SignalContentDetailed = "SCDetailed"
	SignalField = "SFIeld"
	SpectrumFlatness = "SFLatness"
	SpectrumFlatnessResultSumm = "SFSummary"
	UnusedToneError = "UTERror"
	UnusedToneErrorSumm = "UTESummary"


# noinspection SpellCheckingInspection
class WindowTypeK9X(Enum):
	"""21 Members, ChannelFreqResponse ... ResultSummaryGlobal"""
	ChannelFreqResponse = "CFR"
	Constellation = "CONStellation"
	DataBitstreamDecoded = "DDBStream"
	DataBitstreamRaw = "DBSTream"
	Diagram = "DIAGram"
	EvmVsSymbol = "EVSYmbol"
	FreqErrorVsSymbol = "FEVSymbol"
	HeaderBitstreamDecoded = "HDBStream"
	HeaderBitstreamRaw = "HBSTream"
	HeaderInfo = "HEADer"
	MagnitudeCapture = "MCAPture"
	MarkerPeakList = "PEAKlist"
	MarkerTable = "MTABle"
	PhaseErrorVsSymbol = "PEVSymbol"
	PhaseTrackingVsSymbol = "PTVSymbol"
	PowerSpectrum = "PSPectrum"
	PowerVsTimeFallingEdge = "PFALling"
	PowerVsTimeFullPpdu = "PFPPdu"
	PowerVsTimeRisingEdge = "PRISing"
	ResultSummary = "RSUMmary"
	ResultSummaryGlobal = "RSGLobal"


# noinspection SpellCheckingInspection
class XaXisPmSettling(Enum):
	"""3 Members, PMSLength ... PMSTime"""
	PMSLength = 0
	PMSPoint = 1
	PMSTime = 2


# noinspection SpellCheckingInspection
class XaxisUnitScale(Enum):
	"""2 Members, SYMBol ... TIME"""
	SYMBol = 0
	TIME = 1


# noinspection SpellCheckingInspection
class Xdistribution(Enum):
	"""2 Members, BINCentered ... STARtstop"""
	BINCentered = 0
	STARtstop = 1


# noinspection SpellCheckingInspection
class XyDirection(Enum):
	"""2 Members, HORizontal ... VERTical"""
	HORizontal = 0
	VERTical = 1


# noinspection SpellCheckingInspection
class YaXisItems(Enum):
	"""2 Members, COUNt ... OCCurrence"""
	COUNt = 0
	OCCurrence = 1
