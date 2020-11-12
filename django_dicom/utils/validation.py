fields = {
    "ScanningSequence": (0x0018, 0x0020),
    "SequenceVariant": (0x0018, 0x0021),
    "RepetitionTime": (0x0018, 0x0080),
    "InversionTime": (0x0018, 0x0082),
    "PixelSpacing": (0x0028, 0x0030),
    "SliceThickness": (0x0018, 0x0050),
    "SeriesDescription": (0x0008, 0x103E),
    "SequenceName": (0x0018, 0x0024),
    "PulseSequenceName": (0x0018, 0x9005),
    "StudyTime": (0x0008, 0x0030),
    "StudyDate": (0x0008, 0x0020),
    "Manufacturer": (0x0008, 0x0070),
    "InternalPulseSequenceName": (0x0019, 0x109E),
}


def header_getter(field, header):
    data = header.get(fields[field])
    return data.value if data else None


def positive_checker(value, field, header_value):
    if header_value:
        return value == header_value
    return False


def negative_checker(value, field, header_value):
    if header_value:
        return value != header_value
    return False


def positive_string_checker(values, field, header_value):
    if header_value:
        return any(
            value in str(header_value) or value.lower() in str(header_value)
            for value in values
        )
    return False


def negative_string_checker(values, field, header_value):
    if header_value:
        return not any(
            value in str(header_value) or value.lower() in str(header_value)
            for value in values
        )
    return False


def positive_list_checker(values, field, header_value):
    if header_value:
        return all(value in header_value for value in values)
    return False


def negative_list_checker(values, field, header_value):
    if header_value:
        return not all(value in header_value for value in values)
    return False


def run_checks(search_values, header):
    fields_check = [field_checker(item, header) for item in search_values]
    return all(fields_check)


def field_checker(field, value, header):
    global checking_fields
    func = "negative" if field[0] == "-" else "positive"
    field = field[1:]
    header_value = header_getter(field, header)
    return checking_fields[field][func](value, field, header_value)


def scan_details(scan_id, header):
    return {
        "ID": scan_id,
        "RepetitionTime": header_getter("RepetitionTime", header),
        "InversionTime": header_getter("InversionTime", header),
        "PixelSpacing": header_getter("PixelSpacing", header),
        "SliceThickness": header_getter("SliceThickness", header),
        "SeriesDescription": header_getter("SeriesDescription", header),
        "SequenceName": header_getter("SequenceName", header),
        "InternalPulseSequenceName": header_getter(
            "InternalPulseSequenceName", header
        ),
        "StudyTime": header_getter("StudyTime", header),
        "StudyDate": header_getter("StudyDate", header),
        "Manufacturer": header_getter("Manufacturer", header),
        "ScanningSequence": header_getter("ScanningSequence", header),
        "SequenceVariant": header_getter("SequenceVariant", header),
    }


checking_fields = {
    "ScanningSequence": {
        "positive": positive_list_checker,
        "negative": negative_list_checker,
    },
    "SequenceVariant": {
        "positive": positive_list_checker,
        "negative": negative_list_checker,
    },
    "SequenceName": {
        "positive": positive_string_checker,
        "negative": negative_string_checker,
    },
    "InternalPulseSequenceName": {
        "positive": positive_string_checker,
        "negative": negative_string_checker,
    },
    "InversionTime": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
    "RepetitionTime": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
    "Manufacturer": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
    "PixelSpacing": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
    "SliceThickness": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
    "SeriesDescription": {
        "positive": positive_checker,
        "negative": negative_checker,
    },
}
