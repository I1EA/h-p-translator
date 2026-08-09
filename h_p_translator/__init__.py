import pandas as pd
import os

data_dir = os.path.dirname(__file__)
h_df = pd.read_csv(os.path.join(data_dir, "data/h_codes.csv"))
p_df = pd.read_csv(os.path.join(data_dir, "data/p_codes.csv"))

H_CODES = dict(zip(h_df["code"], h_df["meaning"]))
P_CODES = dict(zip(p_df["code"], p_df["meaning"]))

def translate(code):
    """Translate an H or P code to its meaning."""
    if code in H_CODES:
        return H_CODES[code]
    elif code in P_CODES:
        return P_CODES[code]
    else:
        return f"Code {code} not found"

def translate_multiple(codes):
    """Translate multiple codes at once."""
    results = {}
    for code in codes:
        results[code] = translate(code)
    return results

def translate_h(codes_string):
    """Convert a string of H codes to human-readable text."""
    if not codes_string or codes_string == "nan":
        return ""
    codes = [c.strip() for c in codes_string.split(",")]
    return ". ".join([translate(c) for c in codes if c in H_CODES])

def translate_p(codes_string):
    """Convert a string of P codes to human-readable text."""
    if not codes_string or codes_string == "nan":
        return ""
    codes = [c.strip() for c in codes_string.split(",")]
    return ". ".join([translate(c) for c in codes if c in P_CODES])