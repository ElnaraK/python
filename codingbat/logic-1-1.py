def cigar_party(cigars, is_weekend):
    if not is_weekend and cigars in range(40,61):
        return True
    if is_weekend and cigars>=40:
        return True
    else:
        return False
