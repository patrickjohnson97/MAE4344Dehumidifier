

# rawCFMSignal represents the analog signal from channel 0 on the multiplexer
def calculateCFM(rawCFMSignal):
    calibration_constant = 3.0
    maxWaterColumnReading = 0.5
    CFMVoltage = abs(rawCFMSignal) / 500.0
    waterColumnRatio = CFMVoltage / 5.0
    actualWaterColumn = waterColumnRatio * maxWaterColumnReading
    s = calibration_constant * ((actualWaterColumn)**0.5) * 4004.4*0.82*(1.0/18.0)

    # Here is another way to look at it if this is easier to understand
    # s = calibration_constant * ((abs(rawCFMSignal)/(5.0*500)*0.5)**0.5) * 4004.4*0.82*(1.0/18.0)

    s = round(s,1)
    return s
