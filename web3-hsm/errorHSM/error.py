ERROR_XX = {
    "00":  "Response to test message",
    "01":  "Length out of range",
    "02":  "Invalid character",
    "03":  "Value out of range",
    "04":  "Invalid number of parameters",
    "05":  "Parity error",
    "06":  "Key usage error",
    "07":  "Key usage error",
    "08":  "Execution error",
    "09":  "Execution error",
    "10":  "Key Length error",
    "11":  "Printing error",
    "12":  "Marker string not found",
    "20":  "Serial number set, cannot modify it",
    "21":  "The HSM not in a Security Association, or serial number is not present.",
    "22*": "Non-existent command or option",
    "23*": "Invalid command or option",
    "24":  "Incorrect challenge",
    "25":  "Incorrect Acknowledgment",
    "26*": "Duplicate command or option",
    "27":  "No challenge to verify, a command 109 has been received without a prior command 108",
    "28":  "The configuration string in command 108 is too long.",
    "29":  "Unable to allocate memory for the configuration string.",
    "41":  "ASRM timed out waiting for the response from the HSM.",
    "73":  "Header mismatch",
    "92":  "Autokey error",
    "93":  "Factory keys already generated",
    "94":  "No factory keys generated",
}

ERROR_ZZ = {
    "1":    "Invalid command string length",
    "2":    "Invalid command length",
    "3":    "Invalid parameter length",
    "4":    "Passcode length not matched with user data",
    "5":    "Non empty field - conflicts with other fields",
    "101":  "Invalid command string format",
    "102":  "Invalid character",
    "200":  "Value out of range",
    "201":  "Invalid command",
    "202":  "Invalid parameter value",
    "209":  "Invalid key length specified",
    "211":  "Invalid ANSI-formatted message authentication code",
    "212":  "Invalid MAC",
    "215":  "Invalid checksum on string",
    "216":  "Value in field is not the same as other field",
    "217":  "Count value not greater than zero",
    "218":  "Command count table is full",
    "220":  "No free key slot for RSA key",
    "230":  "Command does not exist",
    "301":  "Too many fields",
    "302":  "Too few response fields",
    "303":  "Too few fields",
    "304":  "Initialization vector is missing",
    "305":  "Wrong combination of keys",
    "306":  "Invalid number of parameters",
    "307":  "PAN does not match validation data",
    "501":  "Table entry in use",
    "502":  "Table full",
    "509":  "Key did not have odd parity",
    "510":  "Specified variant cannot be used",
    "511":  "KD1 or KD2 check digits do not match expected check digits",
    "512":  "Single length key not allowed",
    "513":  "Command 14-5, weak key",
    "514":  "Command 14-5, keys have different length",
    "516":  "Session key check digits do not match expected check digits",
    "517":  "Key check digits do not match expected check digits",
    "518":  "MAC does not match",
    "519":  "Cannot load key into key table",
    "520":  "MFK already loaded",
    "521":  "Not in factory state",
    "601":  "Non-existent module key entry",
    "602":  "Non-existent MFK",
    "603":  "Non-existent KEK",
    "604":  "Non-existent Pending MFK",
    "605":  "Incorrect entry of double-length key location",
    "607":  "Security violation",
    "612":  "MFK name in command does not match the MFK name",
    "613":  "Pending MFK name in command does not match the pending MFK name",
    "623":  "Key location empty",
    "630":  "TR31 key block MAC error",
    "631":  "TR31 clear key length error",
    "632":  "Invalid TR31 header",
    "702":  "Internal error",
    "708":  "Internal error",
    "713":  "Internal error",
    "714":  "RSA cryptographic error",
    "715":  "DUKPT error",
    "716":  "Random number generator error",
    "717":  "Failed self-test",
    "718":  "Command not allowed in PCI-HSM mode",
    "801":  "Failed hardware function",
    "802":  "Failed ACS function (general)",
    "805":  "Failed ACS function (Response returned smaller than minimum)",
    "806":  "Failed ACS function (Response length invalid)",
    "807":  "Failed ACS function (Response ID incorrect)",
    "808":  "Failed ACS function (Response ID invalid)",
    "809":  "Failed ACS function (Command had NULL error)",
    "810":  "Failed ACS function (Command had NULL first item)",
    "811":  "Failed ACS function (Response had NULL item)",
    "812":  "Failed ACS function (Response had NULL first item)",
    "813":  "Failed ACS function (Command ID was modified)",
    "814":  "Failed ACS function (Command has invalid item)",
    "815":  "Failed ACS function (Command has invalid first item)",
    "816":  "Failed ACS function (Response has invalid item)",
    "817":  "Failed ACS function (Response has invalid first item)",
    "818":  "Failed ACS function (Command contains too many fields)",
    "819":  "Failed ACS function (Response contains too many fields)",
    "820":  "Failed ACS function (Command buffer format is invalid)",
    "821":  "Failed ACS function (Response buffer format is invalid)",
    "822":  "Failed ACS function (Monitor process already running)",
    "823":  "Failed ACS function (Monitor process not running)",
    "901":  "Expecting a single-length key and received a double length key",
    "902":  "Expecting a double-length key and received a single length key",
    "903":  "The double-length key is a replicated single-length key",
    "1100": "No continuation indexes are available",
    "1101": "Specified continuation index is empty",
    "1102": "Invalid print job length",
    "1103": "Unable to obtain a socket on the printer",
    "1104": "Unable to connect to printer",
    "1105": "Unable to send print job to printer, error returned from printer",
    "1200": "Marker string not found",
    "2000": "The serial number is already set, it cannot be modified",
    "2100": "The serial number is not loaded",
    "2101": "HSM is not in a security association",
    "2200": "Non-existent command item in the configuration string",
    "2300": "Invalid command item format",
    "2301": "Command 105 has not been received",
    "2303": "The command is a counted command",
    "2304": "Option E5 is not enabled",
    "2400": "The input HASH in command 109 does not match the stored hash",
    "2500": "The acknowledgment text is incorrect or missing",
    "2600": "Conflicting duplication of a configuration parameter",
    "2700": "Command 109 was received without a prior command 108",
    "7300": "The variant of the key in table incorrect",
    "7301": "The variant for a decimalization table is wrong",
    "9201": "RSA keys already exists",
    "9202": "Global key data is corrupted",
    "9203": "Cannot allocate memory with mymalloc",
    "9205": "Failed signature verification",
    "9208": "Failed certificate verification",
    "9209": "Cannot sign the certificate or bad signature",
    "9210": "CBC encryption/decryption failed",
    "9211": "No communication key",
    "9212": "No session key",
    "9213": "MAC computation or verification failed",
    "9214": "Invalid buffer data length",
    "9215": "Invalid data length inside the header",
    "9219": "RSA key generation failed",
}

def ErrorType(error:list):
    error_x = ERROR_XX[error[0]];
    error_z = ERROR_ZZ[error[2]];
    return error_x+ " " + error_z;
