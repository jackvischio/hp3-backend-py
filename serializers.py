def serializeItem(a) -> dict:
    return { **{ i: str(a[i]) for i in a if i=='_id' }, **{ i: a[i] for i in a if i!='_id' } }

def serializeList(l) -> list:
    return [serializeItem(a) for a in l]