def transform(legacy_data):
    return {ch.lower(): points
            for points, letters in legacy_data.items()
            for ch in letters}
