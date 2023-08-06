class _NotDefined(Exception):
    pass


def _select_key(k):
    def f(d):
        return d[k]

    return f


def _identity(ele):
    return ele


def groupby(l, by, transform=_identity):
    if isinstance(by, str):
        by = _select_key(by)
    o = {}
    for ele in l:
        k = by(ele)
        o.setdefault(k, []).append(transform(ele))
    return o


def frequency(l, key=_identity):
    o = {}
    for ele in l:
        k = key(ele)
        o[k] = o.setdefault(k, 0) + 1
    return o


def is_unique(l, key=_identity):
    return all(cnt == 1 for cnt in frequency(l, key=key).values())


def duplicated(l, key=_identity):
    return {k: cnt for k, cnt in frequency(l, key=key).items() if cnt > 1}
