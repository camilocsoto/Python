
def count_ip(first: str, last: str) ->int:
    # (("20.0.0.10", "20.0.1.0"))    246
    def ip_to_int(ip:str) -> int:
        parts = list(map(int, ip.split('.')))
        return parts[0] * 256**3 + parts[1] * 256**2 + parts[2] * 256 + parts[3]
    return ip_to_int(last) - ip_to_int(first)

print(count_ip('10.8.0.1','100.8.0.252'))