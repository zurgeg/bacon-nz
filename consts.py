XOR_PAD_BEGIN = "!SDW"

BEACON_NINT_TAG = 0xDD

BEACON_SIZE = 0x70

BEACON_PLAINTEXT_FMT = b"{ssid}{aparam}\x00\x00McDonalds Japan\x00\x00\x00\x00\x00\x00\x00\x00{wkey}\x00\x00\x00\x00mario\x42\x00\x00\x00"

assert len(BEACON_PLAINTEXT_FMT.format(ssid="spoink is the best pokemon!\x00\x00\x00\x00", aparam="\x00" * 10, wkey="\x00" * 32)) == 0x70

BEACON_SUMMED_FMT = b"{ssid}{aparam}\x00\x00McDonalds Japan\x00\x00\x00\x00\x00\x00\x00\x00{wkey}\x00\x00\x00\x00mario\x42\x00{crc}"

BEACON_ENCD_FMT = b"{tag}{encd}"
