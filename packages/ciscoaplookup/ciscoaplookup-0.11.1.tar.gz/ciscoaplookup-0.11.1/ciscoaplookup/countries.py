from re import compile, IGNORECASE, Pattern
import country_converter as coco


def get_country_regex(country: str) -> Pattern:
    pat = coco.convert(names=country, to="regex", not_found=None)
    if not pat:
        raise ValueError("Unknown country: {}".format(country))

    return compile(pat, IGNORECASE)
