#### Bassam Rizk YUid 303525

# csda 1050 F18 S1

### Sprint 1
#Moved back to APIs from QuantMod & QuantTools (vs Kaggle)
#downloaded S&P100 stocks individually
#calculated trailing volatility for each stock
#prepared the files to be aggregated by adding Stock symbol to each row
#Added dividend & stock splits events so to model causality / correlation of events with abnormal volatility
#Pending for Tuesday (before Class) - add charts & visual to wrap up sprint 1

---
title: "Straddle Screening Tool"
output: script for R Studio

---

library(quandl)
library(QuantTools)
library(quantmod)
library(derivmkts)
library(RND)
setDefaults(getSymbols.av, api.key="V7YC53BOMBUB28FJ")



####Downloading Data

#Got a list of S&P 100 from Wikipedia
#Coverted that list from table to csv using Excel / notepad (trying doing that using R - it was too complicated...)
#Copy/ pasted that list into a getSymbols function from Quantmod.


getSymbols(c('AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AGN', 'AIG', 'ALL', 'AMGN', 'AMZN', 'AXP', 'BA', 'BAC', 'BIIB', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK.B', 'C', 'CAT', 'CELG', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CSCO', 'CVS', 'CVX', 'DD', 'DHR', 'DIS', 'DOW', 'DUK', 'EMR', 'EXC', 'F', 'FB', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KHC', 'KMI', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'OXY', 'PEP', 'PFE', 'PG', 'PM', 'PYPL', 'QCOM', 'RTN', 'SBUX', 'SLB', 'SO', 'SPG', 'T', 'TGT', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'UTX', 'V', 'VZ', 'WBA', 'WFC', 'WMT', 'XOM'
))
#This worked!!!!!!
# I received in my environment 100 xts object with history from 2007-01-03 to 2019-08-02



##MEASURE VOLATILITY
#add a column to measure volatility of each stock 
AAPL$VOLA<- volatility(AAPL)
ABBV$VOLA<- volatility(ABBV)
ABT$VOLA<- volatility(ABT)
ACN$VOLA<- volatility(ACN)
ADBE$VOLA<- volatility(ADBE)
AGN$VOLA<- volatility(AGN)
AIG$VOLA<- volatility(AIG)
ALL$VOLA<- volatility(ALL)
AMGN$VOLA<- volatility(AMGN)
AMZN$VOLA<- volatility(AMZN)
AXP$VOLA<- volatility(AXP)
BA$VOLA<- volatility(BA)
BAC$VOLA<- volatility(BAC)
BIIB$VOLA<- volatility(BIIB)
BK$VOLA<- volatility(BK)
BKNG$VOLA<- volatility(BKNG)
BLK$VOLA<- volatility(BLK)
BMY$VOLA<- volatility(BMY)
C$VOLA<- volatility(C)
CAT$VOLA<- volatility(CAT)
CELG$VOLA<- volatility(CELG)
CHTR$VOLA<- volatility(CHTR)
CL$VOLA<- volatility(CL)
CMCSA$VOLA<- volatility(CMCSA)
COF$VOLA<- volatility(COF)
COP$VOLA<- volatility(COP)
COST$VOLA<- volatility(COST)
CSCO$VOLA<- volatility(CSCO)
CVS$VOLA<- volatility(CVS)
CVX$VOLA<- volatility(CVX)
DD$VOLA<- volatility(DD)
DHR$VOLA<- volatility(DHR)
DIS$VOLA<- volatility(DIS)
DOW$VOLA<- volatility(DOW)
DUK$VOLA<- volatility(DUK)
EMR$VOLA<- volatility(EMR)
EXC$VOLA<- volatility(EXC)
F$VOLA<- volatility(F)
FB$VOLA<- volatility(FB)
FDX$VOLA<- volatility(FDX)
GD$VOLA<- volatility(GD)
GE$VOLA<- volatility(GE)
GILD$VOLA<- volatility(GILD)
GM$VOLA<- volatility(GM)
GOOG$VOLA<- volatility(GOOG)
GOOGL$VOLA<- volatility(GOOGL)
GS$VOLA<- volatility(GS)
HD$VOLA<- volatility(HD)
HON$VOLA<- volatility(HON)
IBM$VOLA<- volatility(IBM)
INTC$VOLA<- volatility(INTC)
JNJ$VOLA<- volatility(JNJ)
JPM$VOLA<- volatility(JPM)
KHC$VOLA<- volatility(KHC)
KMI$VOLA<- volatility(KMI)
KO$VOLA<- volatility(KO)
LLY$VOLA<- volatility(LLY)
LMT$VOLA<- volatility(LMT)
LOW$VOLA<- volatility(LOW)
MA$VOLA<- volatility(MA)
MCD$VOLA<- volatility(MCD)
MDLZ$VOLA<- volatility(MDLZ)
MDT$VOLA<- volatility(MDT)
MET$VOLA<- volatility(MET)
MMM$VOLA<- volatility(MMM)
MO$VOLA<- volatility(MO)
MRK$VOLA<- volatility(MRK)
MS$VOLA<- volatility(MS)
MSFT$VOLA<- volatility(MSFT)
NEE$VOLA<- volatility(NEE)
NFLX$VOLA<- volatility(NFLX)
NKE$VOLA<- volatility(NKE)
NVDA$VOLA<- volatility(NVDA)
ORCL$VOLA<- volatility(ORCL)
OXY$VOLA<- volatility(OXY)
PEP$VOLA<- volatility(PEP)
PFE$VOLA<- volatility(PFE)
PG$VOLA<- volatility(PG)
PM$VOLA<- volatility(PM)
PYPL$VOLA<- volatility(PYPL)
QCOM$VOLA<- volatility(QCOM)
RTN$VOLA<- volatility(RTN)
SBUX$VOLA<- volatility(SBUX)
SLB$VOLA<- volatility(SLB)
SO$VOLA<- volatility(SO)
SPG$VOLA<- volatility(SPG)
T$VOLA<- volatility(T)
TGT$VOLA<- volatility(TGT)
TXN$VOLA<- volatility(TXN)
UNH$VOLA<- volatility(UNH)
UNP$VOLA<- volatility(UNP)
UPS$VOLA<- volatility(UPS)
USB$VOLA<- volatility(USB)
UTX$VOLA<- volatility(UTX)
V$VOLA<- volatility(V)
VZ$VOLA<- volatility(VZ)
WBA$VOLA<- volatility(WBA)
WFC$VOLA<- volatility(WFC)
WMT$VOLA<- volatility(WMT)
XOM$VOLA<- volatility(XOM)

#remove NAs

AAPL[is.na(AAPL)] <-0
ABBV[is.na(ABBV)] <-0
ABT[is.na(ABT)] <-0
ACN[is.na(ACN)] <-0
ADBE[is.na(ADBE)] <-0
AGN[is.na(AGN)] <-0
AIG[is.na(AIG)] <-0
ALL[is.na(ALL)] <-0
AMGN[is.na(AMGN)] <-0
AMZN[is.na(AMZN)] <-0
AXP[is.na(AXP)] <-0
BA[is.na(BA)] <-0
BAC[is.na(BAC)] <-0
BIIB[is.na(BIIB)] <-0
BK[is.na(BK)] <-0
BKNG[is.na(BKNG)] <-0
BLK[is.na(BLK)] <-0
BMY[is.na(BMY)] <-0
C[is.na(C)] <-0
CAT[is.na(CAT)] <-0
CELG[is.na(CELG)] <-0
CHTR[is.na(CHTR)] <-0
CL[is.na(CL)] <-0
CMCSA[is.na(CMCSA)] <-0
COF[is.na(COF)] <-0
COP[is.na(COP)] <-0
COST[is.na(COST)] <-0
CSCO[is.na(CSCO)] <-0
CVS[is.na(CVS)] <-0
CVX[is.na(CVX)] <-0
DD[is.na(DD)] <-0
DHR[is.na(DHR)] <-0
DIS[is.na(DIS)] <-0
DOW[is.na(DOW)] <-0
DUK[is.na(DUK)] <-0
EMR[is.na(EMR)] <-0
EXC[is.na(EXC)] <-0
F[is.na(F)] <-0
FB[is.na(FB)] <-0
FDX[is.na(FDX)] <-0
GD[is.na(GD)] <-0
GE[is.na(GE)] <-0
GILD[is.na(GILD)] <-0
GM[is.na(GM)] <-0
GOOG[is.na(GOOG)] <-0
GOOGL[is.na(GOOGL)] <-0
GS[is.na(GS)] <-0
HD[is.na(HD)] <-0
HON[is.na(HON)] <-0
IBM[is.na(IBM)] <-0
INTC[is.na(INTC)] <-0
JNJ[is.na(JNJ)] <-0
JPM[is.na(JPM)] <-0
KHC[is.na(KHC)] <-0
KMI[is.na(KMI)] <-0
KO[is.na(KO)] <-0
LLY[is.na(LLY)] <-0
LMT[is.na(LMT)] <-0
LOW[is.na(LOW)] <-0
MA[is.na(MA)] <-0
MCD[is.na(MCD)] <-0
MDLZ[is.na(MDLZ)] <-0
MDT[is.na(MDT)] <-0
MET[is.na(MET)] <-0
MMM[is.na(MMM)] <-0
MO[is.na(MO)] <-0
MRK[is.na(MRK)] <-0
MS[is.na(MS)] <-0
MSFT[is.na(MSFT)] <-0
NEE[is.na(NEE)] <-0
NFLX[is.na(NFLX)] <-0
NKE[is.na(NKE)] <-0
NVDA[is.na(NVDA)] <-0
ORCL[is.na(ORCL)] <-0
OXY[is.na(OXY)] <-0
PEP[is.na(PEP)] <-0
PFE[is.na(PFE)] <-0
PG[is.na(PG)] <-0
PM[is.na(PM)] <-0
PYPL[is.na(PYPL)] <-0
QCOM[is.na(QCOM)] <-0
RTN[is.na(RTN)] <-0
SBUX[is.na(SBUX)] <-0
SLB[is.na(SLB)] <-0
SO[is.na(SO)] <-0
SPG[is.na(SPG)] <-0
T[is.na(T)] <-0
TGT[is.na(TGT)] <-0
TXN[is.na(TXN)] <-0
UNH[is.na(UNH)] <-0
UNP[is.na(UNP)] <-0
UPS[is.na(UPS)] <-0
USB[is.na(USB)] <-0
UTX[is.na(UTX)] <-0
V[is.na(V)] <-0
VZ[is.na(VZ)] <-0
WBA[is.na(WBA)] <-0
WFC[is.na(WFC)] <-0
WMT[is.na(WMT)] <-0
XOM[is.na(XOM)] <-0


## Add a column for ticker symbol - might be useful as we agreggate information
AAPL$Ticker <- NA
ABBV$Ticker <- NA
ABT$Ticker <- NA
ACN$Ticker <- NA
ADBE$Ticker <- NA
AGN$Ticker <- NA
AIG$Ticker <- NA
ALL$Ticker <- NA
AMGN$Ticker <- NA
AMZN$Ticker <- NA
AXP$Ticker <- NA
BA$Ticker <- NA
BAC$Ticker <- NA
BIIB$Ticker <- NA
BK$Ticker <- NA
BKNG$Ticker <- NA
BLK$Ticker <- NA
BMY$Ticker <- NA
C$Ticker <- NA
CAT$Ticker <- NA
CELG$Ticker <- NA
CHTR$Ticker <- NA
CL$Ticker <- NA
CMCSA$Ticker <- NA
COF$Ticker <- NA
COP$Ticker <- NA
COST$Ticker <- NA
CSCO$Ticker <- NA
CVS$Ticker <- NA
CVX$Ticker <- NA
DD$Ticker <- NA
DHR$Ticker <- NA
DIS$Ticker <- NA
DOW$Ticker <- NA
DUK$Ticker <- NA
EMR$Ticker <- NA
EXC$Ticker <- NA
F$Ticker <- NA
FB$Ticker <- NA
FDX$Ticker <- NA
GD$Ticker <- NA
GE$Ticker <- NA
GILD$Ticker <- NA
GM$Ticker <- NA
GOOG$Ticker <- NA
GOOGL$Ticker <- NA
GS$Ticker <- NA
HD$Ticker <- NA
HON$Ticker <- NA
IBM$Ticker <- NA
INTC$Ticker <- NA
JNJ$Ticker <- NA
JPM$Ticker <- NA
KHC$Ticker <- NA
KMI$Ticker <- NA
KO$Ticker <- NA
LLY$Ticker <- NA
LMT$Ticker <- NA
LOW$Ticker <- NA
MA$Ticker <- NA
MCD$Ticker <- NA
MDLZ$Ticker <- NA
MDT$Ticker <- NA
MET$Ticker <- NA
MMM$Ticker <- NA
MO$Ticker <- NA
MRK$Ticker <- NA
MS$Ticker <- NA
MSFT$Ticker <- NA
NEE$Ticker <- NA
NFLX$Ticker <- NA
NKE$Ticker <- NA
NVDA$Ticker <- NA
ORCL$Ticker <- NA
OXY$Ticker <- NA
PEP$Ticker <- NA
PFE$Ticker <- NA
PG$Ticker <- NA
PM$Ticker <- NA
PYPL$Ticker <- NA
QCOM$Ticker <- NA
RTN$Ticker <- NA
SBUX$Ticker <- NA
SLB$Ticker <- NA
SO$Ticker <- NA
SPG$Ticker <- NA
T$Ticker <- NA
TGT$Ticker <- NA
TXN$Ticker <- NA
UNH$Ticker <- NA
UNP$Ticker <- NA
UPS$Ticker <- NA
USB$Ticker <- NA
UTX$Ticker <- NA
V$Ticker <- NA
VZ$Ticker <- NA
WBA$Ticker <- NA
WFC$Ticker <- NA
WMT$Ticker <- NA
XOM$Ticker <- NA


#Replace "NA"s with ticker symbol of each stock
AAPL[is.na(AAPL)] <- "AAPL"
ABBV[is.na(ABBV)] <- "ABBV"
ABT[is.na(ABT)] <- "ABT"
ACN[is.na(ACN)] <- "ACN"
ADBE[is.na(ADBE)] <- "ADBE"
AGN[is.na(AGN)] <- "AGN"
AIG[is.na(AIG)] <- "AIG"
ALL[is.na(ALL)] <- "ALL"
AMGN[is.na(AMGN)] <- "AMGN"
AMZN[is.na(AMZN)] <- "AMZN"
AXP[is.na(AXP)] <- "AXP"
BA[is.na(BA)] <- "BA"
BAC[is.na(BAC)] <- "BAC"
BIIB[is.na(BIIB)] <- "BIIB"
BK[is.na(BK)] <- "BK"
BKNG[is.na(BKNG)] <- "BKNG"
BLK[is.na(BLK)] <- "BLK"
BMY[is.na(BMY)] <- "BMY"
C[is.na(C)] <- "C"
CAT[is.na(CAT)] <- "CAT"
CELG[is.na(CELG)] <- "CELG"
CHTR[is.na(CHTR)] <- "CHTR"
CL[is.na(CL)] <- "CL"
CMCSA[is.na(CMCSA)] <- "CMCSA"
COF[is.na(COF)] <- "COF"
COP[is.na(COP)] <- "COP"
COST[is.na(COST)] <- "COST"
CSCO[is.na(CSCO)] <- "CSCO"
CVS[is.na(CVS)] <- "CVS"
CVX[is.na(CVX)] <- "CVX"
DD[is.na(DD)] <- "DD"
DHR[is.na(DHR)] <- "DHR"
DIS[is.na(DIS)] <- "DIS"
DOW[is.na(DOW)] <- "DOW"
DUK[is.na(DUK)] <- "DUK"
EMR[is.na(EMR)] <- "EMR"
EXC[is.na(EXC)] <- "EXC"
F[is.na(F)] <- "F"
FB[is.na(FB)] <- "FB"
FDX[is.na(FDX)] <- "FDX"
GD[is.na(GD)] <- "GD"
GE[is.na(GE)] <- "GE"
GILD[is.na(GILD)] <- "GILD"
GM[is.na(GM)] <- "GM"
GOOG[is.na(GOOG)] <- "GOOG"
GOOGL[is.na(GOOGL)] <- "GOOGL"
GS[is.na(GS)] <- "GS"
HD[is.na(HD)] <- "HD"
HON[is.na(HON)] <- "HON"
IBM[is.na(IBM)] <- "IBM"
INTC[is.na(INTC)] <- "INTC"
JNJ[is.na(JNJ)] <- "JNJ"
JPM[is.na(JPM)] <- "JPM"
KHC[is.na(KHC)] <- "KHC"
KMI[is.na(KMI)] <- "KMI"
KO[is.na(KO)] <- "KO"
LLY[is.na(LLY)] <- "LLY"
LMT[is.na(LMT)] <- "LMT"
LOW[is.na(LOW)] <- "LOW"
MA[is.na(MA)] <- "MA"
MCD[is.na(MCD)] <- "MCD"
MDLZ[is.na(MDLZ)] <- "MDLZ"
MDT[is.na(MDT)] <- "MDT"
MET[is.na(MET)] <- "MET"
MMM[is.na(MMM)] <- "MMM"
MO[is.na(MO)] <- "MO"
MRK[is.na(MRK)] <- "MRK"
MS[is.na(MS)] <- "MS"
MSFT[is.na(MSFT)] <- "MSFT"
NEE[is.na(NEE)] <- "NEE"
NFLX[is.na(NFLX)] <- "NFLX"
NKE[is.na(NKE)] <- "NKE"
NVDA[is.na(NVDA)] <- "NVDA"
ORCL[is.na(ORCL)] <- "ORCL"
OXY[is.na(OXY)] <- "OXY"
PEP[is.na(PEP)] <- "PEP"
PFE[is.na(PFE)] <- "PFE"
PG[is.na(PG)] <- "PG"
PM[is.na(PM)] <- "PM"
PYPL[is.na(PYPL)] <- "PYPL"
QCOM[is.na(QCOM)] <- "QCOM"
RTN[is.na(RTN)] <- "RTN"
SBUX[is.na(SBUX)] <- "SBUX"
SLB[is.na(SLB)] <- "SLB"
SO[is.na(SO)] <- "SO"
SPG[is.na(SPG)] <- "SPG"
T[is.na(T)] <- "T"
TGT[is.na(TGT)] <- "TGT"
TXN[is.na(TXN)] <- "TXN"
UNH[is.na(UNH)] <- "UNH"
UNP[is.na(UNP)] <- "UNP"
UPS[is.na(UPS)] <- "UPS"
USB[is.na(USB)] <- "USB"
UTX[is.na(UTX)] <- "UTX"
V[is.na(V)] <- "V"
VZ[is.na(VZ)] <- "VZ"
WBA[is.na(WBA)] <- "WBA"
WFC[is.na(WFC)] <- "WFC"
WMT[is.na(WMT)] <- "WMT"
XOM[is.na(XOM)] <- "XOM"


# Track historical dividends & stock splits events for each stocl
SiDiAAPL<- get_yahoo_splits_and_dividends('AAPL','2007-01-03', '2019-08-02')
SiDiABBV<- get_yahoo_splits_and_dividends('ABBV','2007-01-03', '2019-08-02')
SiDiABT<- get_yahoo_splits_and_dividends('ABT','2007-01-03', '2019-08-02')
SiDiACN<- get_yahoo_splits_and_dividends('ACN','2007-01-03', '2019-08-02')
SiDiADBE<- get_yahoo_splits_and_dividends('ADBE','2007-01-03', '2019-08-02')
SiDiAGN<- get_yahoo_splits_and_dividends('AGN','2007-01-03', '2019-08-02')
SiDiAIG<- get_yahoo_splits_and_dividends('AIG','2007-01-03', '2019-08-02')
SiDiALL<- get_yahoo_splits_and_dividends('ALL','2007-01-03', '2019-08-02')
SiDiAMGN<- get_yahoo_splits_and_dividends('AMGN','2007-01-03', '2019-08-02')
SiDiAMZN<- get_yahoo_splits_and_dividends('AMZN','2007-01-03', '2019-08-02')
SiDiAXP<- get_yahoo_splits_and_dividends('AXP','2007-01-03', '2019-08-02')
SiDiBA<- get_yahoo_splits_and_dividends('BA','2007-01-03', '2019-08-02')
SiDiBAC<- get_yahoo_splits_and_dividends('BAC','2007-01-03', '2019-08-02')
SiDiBIIB<- get_yahoo_splits_and_dividends('BIIB','2007-01-03', '2019-08-02')
SiDiBK<- get_yahoo_splits_and_dividends('BK','2007-01-03', '2019-08-02')
SiDiBKNG<- get_yahoo_splits_and_dividends('BKNG','2007-01-03', '2019-08-02')
SiDiBLK<- get_yahoo_splits_and_dividends('BLK','2007-01-03', '2019-08-02')
SiDiBMY<- get_yahoo_splits_and_dividends('BMY','2007-01-03', '2019-08-02')
SiDiC<- get_yahoo_splits_and_dividends('C','2007-01-03', '2019-08-02')
SiDiCAT<- get_yahoo_splits_and_dividends('CAT','2007-01-03', '2019-08-02')
SiDiCELG<- get_yahoo_splits_and_dividends('CELG','2007-01-03', '2019-08-02')
SiDiCHTR<- get_yahoo_splits_and_dividends('CHTR','2007-01-03', '2019-08-02')
SiDiCL<- get_yahoo_splits_and_dividends('CL','2007-01-03', '2019-08-02')
SiDiCMCSA<- get_yahoo_splits_and_dividends('CMCSA','2007-01-03', '2019-08-02')
SiDiCOF<- get_yahoo_splits_and_dividends('COF','2007-01-03', '2019-08-02')
SiDiCOP<- get_yahoo_splits_and_dividends('COP','2007-01-03', '2019-08-02')
SiDiCOST<- get_yahoo_splits_and_dividends('COST','2007-01-03', '2019-08-02')
SiDiCSCO<- get_yahoo_splits_and_dividends('CSCO','2007-01-03', '2019-08-02')
SiDiCVS<- get_yahoo_splits_and_dividends('CVS','2007-01-03', '2019-08-02')
SiDiCVX<- get_yahoo_splits_and_dividends('CVX','2007-01-03', '2019-08-02')
SiDiDD<- get_yahoo_splits_and_dividends('DD','2007-01-03', '2019-08-02')
SiDiDHR<- get_yahoo_splits_and_dividends('DHR','2007-01-03', '2019-08-02')
SiDiDIS<- get_yahoo_splits_and_dividends('DIS','2007-01-03', '2019-08-02')
SiDiDOW<- get_yahoo_splits_and_dividends('DOW','2007-01-03', '2019-08-02')
SiDiDUK<- get_yahoo_splits_and_dividends('DUK','2007-01-03', '2019-08-02')
SiDiEMR<- get_yahoo_splits_and_dividends('EMR','2007-01-03', '2019-08-02')
SiDiEXC<- get_yahoo_splits_and_dividends('EXC','2007-01-03', '2019-08-02')
SiDiF<- get_yahoo_splits_and_dividends('F','2007-01-03', '2019-08-02')
SiDiFB<- get_yahoo_splits_and_dividends('FB','2007-01-03', '2019-08-02')
SiDiFDX<- get_yahoo_splits_and_dividends('FDX','2007-01-03', '2019-08-02')
SiDiGD<- get_yahoo_splits_and_dividends('GD','2007-01-03', '2019-08-02')
SiDiGE<- get_yahoo_splits_and_dividends('GE','2007-01-03', '2019-08-02')
SiDiGILD<- get_yahoo_splits_and_dividends('GILD','2007-01-03', '2019-08-02')
SiDiGM<- get_yahoo_splits_and_dividends('GM','2007-01-03', '2019-08-02')
SiDiGOOG<- get_yahoo_splits_and_dividends('GOOG','2007-01-03', '2019-08-02')
SiDiGOOGL<- get_yahoo_splits_and_dividends('GOOGL','2007-01-03', '2019-08-02')
SiDiGS<- get_yahoo_splits_and_dividends('GS','2007-01-03', '2019-08-02')
SiDiHD<- get_yahoo_splits_and_dividends('HD','2007-01-03', '2019-08-02')
SiDiHON<- get_yahoo_splits_and_dividends('HON','2007-01-03', '2019-08-02')
SiDiIBM<- get_yahoo_splits_and_dividends('IBM','2007-01-03', '2019-08-02')
SiDiINTC<- get_yahoo_splits_and_dividends('INTC','2007-01-03', '2019-08-02')
SiDiJNJ<- get_yahoo_splits_and_dividends('JNJ','2007-01-03', '2019-08-02')
SiDiJPM<- get_yahoo_splits_and_dividends('JPM','2007-01-03', '2019-08-02')
SiDiKHC<- get_yahoo_splits_and_dividends('KHC','2007-01-03', '2019-08-02')
SiDiKMI<- get_yahoo_splits_and_dividends('KMI','2007-01-03', '2019-08-02')
SiDiKO<- get_yahoo_splits_and_dividends('KO','2007-01-03', '2019-08-02')
SiDiLLY<- get_yahoo_splits_and_dividends('LLY','2007-01-03', '2019-08-02')
SiDiLMT<- get_yahoo_splits_and_dividends('LMT','2007-01-03', '2019-08-02')
SiDiLOW<- get_yahoo_splits_and_dividends('LOW','2007-01-03', '2019-08-02')
SiDiMA<- get_yahoo_splits_and_dividends('MA','2007-01-03', '2019-08-02')
SiDiMCD<- get_yahoo_splits_and_dividends('MCD','2007-01-03', '2019-08-02')
SiDiMDLZ<- get_yahoo_splits_and_dividends('MDLZ','2007-01-03', '2019-08-02')
SiDiMDT<- get_yahoo_splits_and_dividends('MDT','2007-01-03', '2019-08-02')
SiDiMET<- get_yahoo_splits_and_dividends('MET','2007-01-03', '2019-08-02')
SiDiMMM<- get_yahoo_splits_and_dividends('MMM','2007-01-03', '2019-08-02')
SiDiMO<- get_yahoo_splits_and_dividends('MO','2007-01-03', '2019-08-02')
SiDiMRK<- get_yahoo_splits_and_dividends('MRK','2007-01-03', '2019-08-02')
SiDiMS<- get_yahoo_splits_and_dividends('MS','2007-01-03', '2019-08-02')
SiDiMSFT<- get_yahoo_splits_and_dividends('MSFT','2007-01-03', '2019-08-02')
SiDiNEE<- get_yahoo_splits_and_dividends('NEE','2007-01-03', '2019-08-02')
SiDiNFLX<- get_yahoo_splits_and_dividends('NFLX','2007-01-03', '2019-08-02')
SiDiNKE<- get_yahoo_splits_and_dividends('NKE','2007-01-03', '2019-08-02')
SiDiNVDA<- get_yahoo_splits_and_dividends('NVDA','2007-01-03', '2019-08-02')
SiDiORCL<- get_yahoo_splits_and_dividends('ORCL','2007-01-03', '2019-08-02')
SiDiOXY<- get_yahoo_splits_and_dividends('OXY','2007-01-03', '2019-08-02')
SiDiPEP<- get_yahoo_splits_and_dividends('PEP','2007-01-03', '2019-08-02')
SiDiPFE<- get_yahoo_splits_and_dividends('PFE','2007-01-03', '2019-08-02')
SiDiPG<- get_yahoo_splits_and_dividends('PG','2007-01-03', '2019-08-02')
SiDiPM<- get_yahoo_splits_and_dividends('PM','2007-01-03', '2019-08-02')
SiDiPYPL<- get_yahoo_splits_and_dividends('PYPL','2007-01-03', '2019-08-02')
SiDiQCOM<- get_yahoo_splits_and_dividends('QCOM','2007-01-03', '2019-08-02')
SiDiRTN<- get_yahoo_splits_and_dividends('RTN','2007-01-03', '2019-08-02')
SiDiSBUX<- get_yahoo_splits_and_dividends('SBUX','2007-01-03', '2019-08-02')
SiDiSLB<- get_yahoo_splits_and_dividends('SLB','2007-01-03', '2019-08-02')
SiDiSO<- get_yahoo_splits_and_dividends('SO','2007-01-03', '2019-08-02')
SiDiSPG<- get_yahoo_splits_and_dividends('SPG','2007-01-03', '2019-08-02')
SiDiT<- get_yahoo_splits_and_dividends('T','2007-01-03', '2019-08-02')
SiDiTGT<- get_yahoo_splits_and_dividends('TGT','2007-01-03', '2019-08-02')
SiDiTXN<- get_yahoo_splits_and_dividends('TXN','2007-01-03', '2019-08-02')
SiDiUNH<- get_yahoo_splits_and_dividends('UNH','2007-01-03', '2019-08-02')
SiDiUNP<- get_yahoo_splits_and_dividends('UNP','2007-01-03', '2019-08-02')
SiDiUPS<- get_yahoo_splits_and_dividends('UPS','2007-01-03', '2019-08-02')
SiDiUSB<- get_yahoo_splits_and_dividends('USB','2007-01-03', '2019-08-02')
SiDiUTX<- get_yahoo_splits_and_dividends('UTX','2007-01-03', '2019-08-02')
SiDiV<- get_yahoo_splits_and_dividends('V','2007-01-03', '2019-08-02')
SiDiVZ<- get_yahoo_splits_and_dividends('VZ','2007-01-03', '2019-08-02')
SiDiWBA<- get_yahoo_splits_and_dividends('WBA','2007-01-03', '2019-08-02')
SiDiWFC<- get_yahoo_splits_and_dividends('WFC','2007-01-03', '2019-08-02')
SiDiWMT<- get_yahoo_splits_and_dividends('WMT','2007-01-03', '2019-08-02')
SiDiXOM<- get_yahoo_splits_and_dividends('XOM','2007-01-03', '2019-08-02')


##USING DATES MERGE dividends & split view with stock historical data
AAPL<- merge(AAPL, SiDiAAPL)
ABBV<- merge(ABBV, SiDiAAPL)
ABT<- merge(ABT, SiDiAAPL)
ACN<- merge(ACN, SiDiAAPL)
ADBE<- merge(ADBE, SiDiAAPL)
AGN<- merge(AGN, SiDiAAPL)
AIG<- merge(AIG, SiDiAAPL)
ALL<- merge(ALL, SiDiAAPL)
AMGN<- merge(AMGN, SiDiAAPL)
AMZN<- merge(AMZN, SiDiAAPL)
AXP<- merge(AXP, SiDiAAPL)
BA<- merge(BA, SiDiAAPL)
BAC<- merge(BAC, SiDiAAPL)
BIIB<- merge(BIIB, SiDiAAPL)
BK<- merge(BK, SiDiAAPL)
BKNG<- merge(BKNG, SiDiAAPL)
BLK<- merge(BLK, SiDiAAPL)
BMY<- merge(BMY, SiDiAAPL)
C<- merge(C, SiDiAAPL)
CAT<- merge(CAT, SiDiAAPL)
CELG<- merge(CELG, SiDiAAPL)
CHTR<- merge(CHTR, SiDiAAPL)
CL<- merge(CL, SiDiAAPL)
CMCSA<- merge(CMCSA, SiDiAAPL)
COF<- merge(COF, SiDiAAPL)
COP<- merge(COP, SiDiAAPL)
COST<- merge(COST, SiDiAAPL)
CSCO<- merge(CSCO, SiDiAAPL)
CVS<- merge(CVS, SiDiAAPL)
CVX<- merge(CVX, SiDiAAPL)
DD<- merge(DD, SiDiAAPL)
DHR<- merge(DHR, SiDiAAPL)
DIS<- merge(DIS, SiDiAAPL)
DOW<- merge(DOW, SiDiAAPL)
DUK<- merge(DUK, SiDiAAPL)
EMR<- merge(EMR, SiDiAAPL)
EXC<- merge(EXC, SiDiAAPL)
F<- merge(F, SiDiAAPL)
FB<- merge(FB, SiDiAAPL)
FDX<- merge(FDX, SiDiAAPL)
GD<- merge(GD, SiDiAAPL)
GE<- merge(GE, SiDiAAPL)
GILD<- merge(GILD, SiDiAAPL)
GM<- merge(GM, SiDiAAPL)
GOOG<- merge(GOOG, SiDiAAPL)
GOOGL<- merge(GOOGL, SiDiAAPL)
GS<- merge(GS, SiDiAAPL)
HD<- merge(HD, SiDiAAPL)
HON<- merge(HON, SiDiAAPL)
IBM<- merge(IBM, SiDiAAPL)
INTC<- merge(INTC, SiDiAAPL)
JNJ<- merge(JNJ, SiDiAAPL)
JPM<- merge(JPM, SiDiAAPL)
KHC<- merge(KHC, SiDiAAPL)
KMI<- merge(KMI, SiDiAAPL)
KO<- merge(KO, SiDiAAPL)
LLY<- merge(LLY, SiDiAAPL)
LMT<- merge(LMT, SiDiAAPL)
LOW<- merge(LOW, SiDiAAPL)
MA<- merge(MA, SiDiAAPL)
MCD<- merge(MCD, SiDiAAPL)
MDLZ<- merge(MDLZ, SiDiAAPL)
MDT<- merge(MDT, SiDiAAPL)
MET<- merge(MET, SiDiAAPL)
MMM<- merge(MMM, SiDiAAPL)
MO<- merge(MO, SiDiAAPL)
MRK<- merge(MRK, SiDiAAPL)
MS<- merge(MS, SiDiAAPL)
MSFT<- merge(MSFT, SiDiAAPL)
NEE<- merge(NEE, SiDiAAPL)
NFLX<- merge(NFLX, SiDiAAPL)
NKE<- merge(NKE, SiDiAAPL)
NVDA<- merge(NVDA, SiDiAAPL)
ORCL<- merge(ORCL, SiDiAAPL)
OXY<- merge(OXY, SiDiAAPL)
PEP<- merge(PEP, SiDiAAPL)
PFE<- merge(PFE, SiDiAAPL)
PG<- merge(PG, SiDiAAPL)
PM<- merge(PM, SiDiAAPL)
PYPL<- merge(PYPL, SiDiAAPL)
QCOM<- merge(QCOM, SiDiAAPL)
RTN<- merge(RTN, SiDiAAPL)
SBUX<- merge(SBUX, SiDiAAPL)
SLB<- merge(SLB, SiDiAAPL)
SO<- merge(SO, SiDiAAPL)
SPG<- merge(SPG, SiDiAAPL)
T<- merge(T, SiDiAAPL)
TGT<- merge(TGT, SiDiAAPL)
TXN<- merge(TXN, SiDiAAPL)
UNH<- merge(UNH, SiDiAAPL)
UNP<- merge(UNP, SiDiAAPL)
UPS<- merge(UPS, SiDiAAPL)
USB<- merge(USB, SiDiAAPL)
UTX<- merge(UTX, SiDiAAPL)
V<- merge(V, SiDiAAPL)
VZ<- merge(VZ, SiDiAAPL)
WBA<- merge(WBA, SiDiAAPL)
WFC<- merge(WFC, SiDiAAPL)
WMT<- merge(WMT, SiDiAAPL)
XOM<- merge(XOM, SiDiAAPL)



#REMOVE NAs FROM TICKER SYMBOLS (THIS WAS LOST IN THE MERGE)
AAPL$Ticker[is.na(AAPL$Ticker)] <- "AAPL"
ABBV$Ticker[is.na(ABBV$Ticker)] <- "ABBV"
ABT$Ticker[is.na(ABT$Ticker)] <- "ABT"
ACN$Ticker[is.na(ACN$Ticker)] <- "ACN"
ADBE$Ticker[is.na(ADBE$Ticker)] <- "ADBE"
AGN$Ticker[is.na(AGN$Ticker)] <- "AGN"
AIG$Ticker[is.na(AIG$Ticker)] <- "AIG"
ALL$Ticker[is.na(ALL$Ticker)] <- "ALL"
AMGN$Ticker[is.na(AMGN$Ticker)] <- "AMGN"
AMZN$Ticker[is.na(AMZN$Ticker)] <- "AMZN"
AXP$Ticker[is.na(AXP$Ticker)] <- "AXP"
BA$Ticker[is.na(BA$Ticker)] <- "BA"
BAC$Ticker[is.na(BAC$Ticker)] <- "BAC"
BIIB$Ticker[is.na(BIIB$Ticker)] <- "BIIB"
BK$Ticker[is.na(BK$Ticker)] <- "BK"
BKNG$Ticker[is.na(BKNG$Ticker)] <- "BKNG"
BLK$Ticker[is.na(BLK$Ticker)] <- "BLK"
BMY$Ticker[is.na(BMY$Ticker)] <- "BMY"
C$Ticker[is.na(C$Ticker)] <- "C"
CAT$Ticker[is.na(CAT$Ticker)] <- "CAT"
CELG$Ticker[is.na(CELG$Ticker)] <- "CELG"
CHTR$Ticker[is.na(CHTR$Ticker)] <- "CHTR"
CL$Ticker[is.na(CL$Ticker)] <- "CL"
CMCSA$Ticker[is.na(CMCSA$Ticker)] <- "CMCSA"
COF$Ticker[is.na(COF$Ticker)] <- "COF"
COP$Ticker[is.na(COP$Ticker)] <- "COP"
COST$Ticker[is.na(COST$Ticker)] <- "COST"
CSCO$Ticker[is.na(CSCO$Ticker)] <- "CSCO"
CVS$Ticker[is.na(CVS$Ticker)] <- "CVS"
CVX$Ticker[is.na(CVX$Ticker)] <- "CVX"
DD$Ticker[is.na(DD$Ticker)] <- "DD"
DHR$Ticker[is.na(DHR$Ticker)] <- "DHR"
DIS$Ticker[is.na(DIS$Ticker)] <- "DIS"
DOW$Ticker[is.na(DOW$Ticker)] <- "DOW"
DUK$Ticker[is.na(DUK$Ticker)] <- "DUK"
EMR$Ticker[is.na(EMR$Ticker)] <- "EMR"
EXC$Ticker[is.na(EXC$Ticker)] <- "EXC"
F$Ticker[is.na(F$Ticker)] <- "F"
FB$Ticker[is.na(FB$Ticker)] <- "FB"
FDX$Ticker[is.na(FDX$Ticker)] <- "FDX"
GD$Ticker[is.na(GD$Ticker)] <- "GD"
GE$Ticker[is.na(GE$Ticker)] <- "GE"
GILD$Ticker[is.na(GILD$Ticker)] <- "GILD"
GM$Ticker[is.na(GM$Ticker)] <- "GM"
GOOG$Ticker[is.na(GOOG$Ticker)] <- "GOOG"
GOOGL$Ticker[is.na(GOOGL$Ticker)] <- "GOOGL"
GS$Ticker[is.na(GS$Ticker)] <- "GS"
HD$Ticker[is.na(HD$Ticker)] <- "HD"
HON$Ticker[is.na(HON$Ticker)] <- "HON"
IBM$Ticker[is.na(IBM$Ticker)] <- "IBM"
INTC$Ticker[is.na(INTC$Ticker)] <- "INTC"
JNJ$Ticker[is.na(JNJ$Ticker)] <- "JNJ"
JPM$Ticker[is.na(JPM$Ticker)] <- "JPM"
KHC$Ticker[is.na(KHC$Ticker)] <- "KHC"
KMI$Ticker[is.na(KMI$Ticker)] <- "KMI"
KO$Ticker[is.na(KO$Ticker)] <- "KO"
LLY$Ticker[is.na(LLY$Ticker)] <- "LLY"
LMT$Ticker[is.na(LMT$Ticker)] <- "LMT"
LOW$Ticker[is.na(LOW$Ticker)] <- "LOW"
MA$Ticker[is.na(MA$Ticker)] <- "MA"
MCD$Ticker[is.na(MCD$Ticker)] <- "MCD"
MDLZ$Ticker[is.na(MDLZ$Ticker)] <- "MDLZ"
MDT$Ticker[is.na(MDT$Ticker)] <- "MDT"
MET$Ticker[is.na(MET$Ticker)] <- "MET"
MMM$Ticker[is.na(MMM$Ticker)] <- "MMM"
MO$Ticker[is.na(MO$Ticker)] <- "MO"
MRK$Ticker[is.na(MRK$Ticker)] <- "MRK"
MS$Ticker[is.na(MS$Ticker)] <- "MS"
MSFT$Ticker[is.na(MSFT$Ticker)] <- "MSFT"
NEE$Ticker[is.na(NEE$Ticker)] <- "NEE"
NFLX$Ticker[is.na(NFLX$Ticker)] <- "NFLX"
NKE$Ticker[is.na(NKE$Ticker)] <- "NKE"
NVDA$Ticker[is.na(NVDA$Ticker)] <- "NVDA"
ORCL$Ticker[is.na(ORCL$Ticker)] <- "ORCL"
OXY$Ticker[is.na(OXY$Ticker)] <- "OXY"
PEP$Ticker[is.na(PEP$Ticker)] <- "PEP"
PFE$Ticker[is.na(PFE$Ticker)] <- "PFE"
PG$Ticker[is.na(PG$Ticker)] <- "PG"
PM$Ticker[is.na(PM$Ticker)] <- "PM"
PYPL$Ticker[is.na(PYPL$Ticker)] <- "PYPL"
QCOM$Ticker[is.na(QCOM$Ticker)] <- "QCOM"
RTN$Ticker[is.na(RTN$Ticker)] <- "RTN"
SBUX$Ticker[is.na(SBUX$Ticker)] <- "SBUX"
SLB$Ticker[is.na(SLB$Ticker)] <- "SLB"
SO$Ticker[is.na(SO$Ticker)] <- "SO"
SPG$Ticker[is.na(SPG$Ticker)] <- "SPG"
T$Ticker[is.na(T$Ticker)] <- "T"
TGT$Ticker[is.na(TGT$Ticker)] <- "TGT"
TXN$Ticker[is.na(TXN$Ticker)] <- "TXN"
UNH$Ticker[is.na(UNH$Ticker)] <- "UNH"
UNP$Ticker[is.na(UNP$Ticker)] <- "UNP"
UPS$Ticker[is.na(UPS$Ticker)] <- "UPS"
USB$Ticker[is.na(USB$Ticker)] <- "USB"
UTX$Ticker[is.na(UTX$Ticker)] <- "UTX"
V$Ticker[is.na(V$Ticker)] <- "V"
VZ$Ticker[is.na(VZ$Ticker)] <- "VZ"
WBA$Ticker[is.na(WBA$Ticker)] <- "WBA"
WFC$Ticker[is.na(WFC$Ticker)] <- "WFC"
WMT$Ticker[is.na(WMT$Ticker)] <- "WMT"
XOM$Ticker[is.na(XOM$Ticker)] <- "XOM"


#REMOVE NAs FROM DIVIDEND VALUE

AAPL$value[is.na(AAPL$value)] <- 0
ABBV$value[is.na(ABBV$value)] <-  0
ABT$value[is.na(ABT$value)] <-  0
ACN$value[is.na(ACN$value)] <-  0
ADBE$value[is.na(ADBE$value)] <-  0
AGN$value[is.na(AGN$value)] <-  0
AIG$value[is.na(AIG$value)] <-  0
ALL$value[is.na(ALL$value)] <-  0
AMGN$value[is.na(AMGN$value)] <-  0
AMZN$value[is.na(AMZN$value)] <-  0
AXP$value[is.na(AXP$value)] <-  0
BA$value[is.na(BA$value)] <-  0
BAC$value[is.na(BAC$value)] <-  0
BIIB$value[is.na(BIIB$value)] <-  0
BK$value[is.na(BK$value)] <-  0
BKNG$value[is.na(BKNG$value)] <-  0
BLK$value[is.na(BLK$value)] <-  0
BMY$value[is.na(BMY$value)] <-  0
C$value[is.na(C$value)] <-  0
CAT$value[is.na(CAT$value)] <-  0
CELG$value[is.na(CELG$value)] <-  0
CHTR$value[is.na(CHTR$value)] <-  0
CL$value[is.na(CL$value)] <-  0
CMCSA$value[is.na(CMCSA$value)] <-  0
COF$value[is.na(COF$value)] <-  0
COP$value[is.na(COP$value)] <-  0
COST$value[is.na(COST$value)] <-  0
CSCO$value[is.na(CSCO$value)] <-  0
CVS$value[is.na(CVS$value)] <-  0
CVX$value[is.na(CVX$value)] <-  0
DD$value[is.na(DD$value)] <-  0
DHR$value[is.na(DHR$value)] <-  0
DIS$value[is.na(DIS$value)] <-  0
DOW$value[is.na(DOW$value)] <-  0
DUK$value[is.na(DUK$value)] <-  0
EMR$value[is.na(EMR$value)] <-  0
EXC$value[is.na(EXC$value)] <-  0
F$value[is.na(F$value)] <-  0
FB$value[is.na(FB$value)] <-  0
FDX$value[is.na(FDX$value)] <-  0
GD$value[is.na(GD$value)] <-  0
GE$value[is.na(GE$value)] <-  0
GILD$value[is.na(GILD$value)] <-  0
GM$value[is.na(GM$value)] <-  0
GOOG$value[is.na(GOOG$value)] <-  0
GOOGL$value[is.na(GOOGL$value)] <-  0
GS$value[is.na(GS$value)] <-  0
HD$value[is.na(HD$value)] <-  0
HON$value[is.na(HON$value)] <-  0
IBM$value[is.na(IBM$value)] <-  0
INTC$value[is.na(INTC$value)] <-  0
JNJ$value[is.na(JNJ$value)] <-  0
JPM$value[is.na(JPM$value)] <-  0
KHC$value[is.na(KHC$value)] <-  0
KMI$value[is.na(KMI$value)] <-  0
KO$value[is.na(KO$value)] <-  0
LLY$value[is.na(LLY$value)] <-  0
LMT$value[is.na(LMT$value)] <-  0
LOW$value[is.na(LOW$value)] <-  0
MA$value[is.na(MA$value)] <-  0
MCD$value[is.na(MCD$value)] <-  0
MDLZ$value[is.na(MDLZ$value)] <-  0
MDT$value[is.na(MDT$value)] <-  0
MET$value[is.na(MET$value)] <-  0
MMM$value[is.na(MMM$value)] <-  0
MO$value[is.na(MO$value)] <-  0
MRK$value[is.na(MRK$value)] <-  0
MS$value[is.na(MS$value)] <-  0
MSFT$value[is.na(MSFT$value)] <-  0
NEE$value[is.na(NEE$value)] <-  0
NFLX$value[is.na(NFLX$value)] <-  0
NKE$value[is.na(NKE$value)] <-  0
NVDA$value[is.na(NVDA$value)] <-  0
ORCL$value[is.na(ORCL$value)] <-  0
OXY$value[is.na(OXY$value)] <-  0
PEP$value[is.na(PEP$value)] <-  0
PFE$value[is.na(PFE$value)] <-  0
PG$value[is.na(PG$value)] <-  0
PM$value[is.na(PM$value)] <-  0
PYPL$value[is.na(PYPL$value)] <-  0
QCOM$value[is.na(QCOM$value)] <-  0
RTN$value[is.na(RTN$value)] <-  0
SBUX$value[is.na(SBUX$value)] <-  0
SLB$value[is.na(SLB$value)] <-  0
SO$value[is.na(SO$value)] <-  0
SPG$value[is.na(SPG$value)] <-  0
T$value[is.na(T$value)] <-  0
TGT$value[is.na(TGT$value)] <-  0
TXN$value[is.na(TXN$value)] <-  0
UNH$value[is.na(UNH$value)] <-  0
UNP$value[is.na(UNP$value)] <-  0
UPS$value[is.na(UPS$value)] <-  0
USB$value[is.na(USB$value)] <-  0
UTX$value[is.na(UTX$value)] <-  0
V$value[is.na(V$value)] <-  0
VZ$value[is.na(VZ$value)] <-  0
WBA$value[is.na(WBA$value)] <-  0
WFC$value[is.na(WFC$value)] <-  0
WMT$value[is.na(WMT$value)] <-  0
XOM$value[is.na(XOM$value)] <-  0



## Merge all in one data frame
SnP100<- rbind(AAPL, ABBV, ABT, ACN, ADBE, AGN, AIG, ALL, AMGN, AMZN, AXP, BA, BAC, BIIB, BK, BKNG, BLK, BMY, C, CAT, CELG, CHTR, CL, CMCSA, COF, COP, COST, CSCO, CVS, CVX, DD, DHR, DIS, DOW, DUK, EMR, EXC, F, FB, FDX, GD, GE, GILD, GM, GOOG, GOOGL, GS, HD, HON, IBM, INTC, JNJ, JPM, KHC, KMI, KO, LLY, LMT, LOW, MA, MCD, MDLZ, MDT, MET, MMM, MO, MRK, MS, MSFT, NEE, NFLX, NKE, NVDA, ORCL, OXY, PEP, PFE, PG, PM, PYPL, QCOM, RTN, SBUX, SLB, SO, SPG, T, TGT, TXN, UNH, UNP, UPS, USB, UTX, V, VZ, WBA, WFC, WMT, XOM)
#successfully merged all data sets and added ticker - but the date replicating...
#ask Matthew on how to fix the data...

summary(SnP100)

### Data Exploration

#Sample View of few stocks

head(SBUX)
head.matrix(SLB, n = 4L)

summary(TGT)


#Chart 

barChart(AAPL,multi.col=TRUE,theme="white")
# Specify lookup parameters, and save for future sessions. 


candleChart(GOOG, subset= "last 4 months",multi.col=TRUE,theme="white", addMACD(fast = 12, slow = 26, signal = 9, type = "EMA"))
#This worked before the data cleanup...

barChart(c(AAPL, ABBV, ABT, ACN, ADBE, AGN, AIG, ALL, AMGN, AMZN, AXP, BA, BAC, BIIB, BK, BKNG, BLK, BMY, C, CAT, CELG, CHTR, CL, CMCSA, COF, COP, COST, CSCO, CVS, CVX, DD, DHR, DIS, DOW, DUK, EMR, EXC, F, FB, FDX, GD, GE, GILD, GM, GOOG, GOOGL, GS, HD, HON, IBM, INTC, JNJ, JPM, KHC, KMI, KO, LLY, LMT, LOW, MA, MCD, MDLZ, MDT, MET, MMM, MO, MRK, MS, MSFT, NEE, NFLX, NKE, NVDA, ORCL, OXY, PEP, PFE, PG, PM, PYPL, QCOM, RTN, SBUX, SLB, SO, SPG, T, TGT, TXN, UNH, UNP, UPS, USB, UTX, V, VZ, WBA, WFC, WMT, XOM), subset="last 4 months" ,multi.col=TRUE,theme="white")
#This worked before the data cleanup...

chart_Series(c(AAPL$VOLA, ABBV$VOLA, ABT$VOLA, ACN$VOLA, ADBE$VOLA, AGN$VOLA, AIG$VOLA, ALL$VOLA, AMGN$VOLA, AMZN$VOLA, AXP$VOLA, BA$VOLA, BAC$VOLA, BIIB$VOLA, BK$VOLA, BKNG$VOLA, BLK$VOLA, BMY$VOLA, C$VOLA, CAT$VOLA, CELG$VOLA, CHTR$VOLA, CL$VOLA, CMCSA$VOLA, COF$VOLA, COP$VOLA, COST$VOLA, CSCO$VOLA, CVS$VOLA, CVX$VOLA, DD$VOLA, DHR$VOLA, DIS$VOLA, DOW$VOLA, DUK$VOLA, EMR$VOLA, EXC$VOLA, F$VOLA, FB$VOLA, FDX$VOLA, GD$VOLA, GE$VOLA, GILD$VOLA, GM$VOLA, GOOG$VOLA, GOOGL$VOLA, GS$VOLA, HD$VOLA, HON$VOLA, IBM$VOLA, INTC$VOLA, JNJ$VOLA, JPM$VOLA, KHC$VOLA, KMI$VOLA, KO$VOLA, LLY$VOLA, LMT$VOLA, LOW$VOLA, MA$VOLA, MCD$VOLA, MDLZ$VOLA, MDT$VOLA, MET$VOLA, MMM$VOLA, MO$VOLA, MRK$VOLA, MS$VOLA, MSFT$VOLA, NEE$VOLA, NFLX$VOLA, NKE$VOLA, NVDA$VOLA, ORCL$VOLA, OXY$VOLA, PEP$VOLA, PFE$VOLA, PG$VOLA, PM$VOLA, PYPL$VOLA, QCOM$VOLA, RTN$VOLA, SBUX$VOLA, SLB$VOLA, SO$VOLA, SPG$VOLA, T$VOLA, TGT$VOLA, TXN$VOLA, UNH$VOLA, UNP$VOLA, UPS$VOLA, USB$VOLA, UTX$VOLA, V$VOLA, VZ$VOLA, WBA$VOLA, WFC$VOLA, WMT$VOLA, XOM$VOLA))
#didn't work

VolAvg <- mean(c(AAPL$VOLA, ABBV$VOLA, ABT$VOLA, ACN$VOLA, ADBE$VOLA, AGN$VOLA, AIG$VOLA, ALL$VOLA, AMGN$VOLA, AMZN$VOLA, AXP$VOLA, BA$VOLA, BAC$VOLA, BIIB$VOLA, BK$VOLA, BKNG$VOLA, BLK$VOLA, BMY$VOLA, C$VOLA, CAT$VOLA, CELG$VOLA, CHTR$VOLA, CL$VOLA, CMCSA$VOLA, COF$VOLA, COP$VOLA, COST$VOLA, CSCO$VOLA, CVS$VOLA, CVX$VOLA, DD$VOLA, DHR$VOLA, DIS$VOLA, DOW$VOLA, DUK$VOLA, EMR$VOLA, EXC$VOLA, F$VOLA, FB$VOLA, FDX$VOLA, GD$VOLA, GE$VOLA, GILD$VOLA, GM$VOLA, GOOG$VOLA, GOOGL$VOLA, GS$VOLA, HD$VOLA, HON$VOLA, IBM$VOLA, INTC$VOLA, JNJ$VOLA, JPM$VOLA, KHC$VOLA, KMI$VOLA, KO$VOLA, LLY$VOLA, LMT$VOLA, LOW$VOLA, MA$VOLA, MCD$VOLA, MDLZ$VOLA, MDT$VOLA, MET$VOLA, MMM$VOLA, MO$VOLA, MRK$VOLA, MS$VOLA, MSFT$VOLA, NEE$VOLA, NFLX$VOLA, NKE$VOLA, NVDA$VOLA, ORCL$VOLA, OXY$VOLA, PEP$VOLA, PFE$VOLA, PG$VOLA, PM$VOLA, PYPL$VOLA, QCOM$VOLA, RTN$VOLA, SBUX$VOLA, SLB$VOLA, SO$VOLA, SPG$VOLA, T$VOLA, TGT$VOLA, TXN$VOLA, UNH$VOLA, UNP$VOLA, UPS$VOLA, USB$VOLA, UTX$VOLA, V$VOLA, VZ$VOLA, WBA$VOLA, WFC$VOLA, WMT$VOLA, XOM$VOLA))








This is an [R Markdown](http://rmarkdown.rstudio.com) Notebook. When you execute code within the notebook, the results appear beneath the code. 

Try executing this chunk by clicking the *Run* button within the chunk or by placing your cursor inside it and pressing *Ctrl+Shift+Enter*. 

```{r}
plot(cars)
```

Add a new chunk by clicking the *Insert Chunk* button on the toolbar or by pressing *Ctrl+Alt+I*.

When you save the notebook, an HTML file containing the code and output will be saved alongside it (click the *Preview* button or press *Ctrl+Shift+K* to preview the HTML file).

The preview shows you a rendered HTML copy of the contents of the editor. Consequently, unlike *Knit*, *Preview* does not run any R code chunks. Instead, the output of the chunk when it was last run in the editor is displayed.


