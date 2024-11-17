from utils import get_data, get_invalid_data
from checksum import calculate_checksum, serialize_result
from config import PATH_CSV, PATH_RESULT, PATTERNS, VARIANT


if __name__ == '__main__':
    data = get_data(PATH_CSV)
    invalid_data_idx = get_invalid_data(data, PATTERNS)
    checksum = calculate_checksum(invalid_data_idx)
    serialize_result(VARIANT, checksum, PATH_RESULT)
 