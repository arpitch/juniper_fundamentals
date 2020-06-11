import string




def create_ip_address_4( a='172', b='16', c='254', d='1'):
    if isinstance(a,str) and a.isdigit() and len(a)==3 and int(a)<= 255:
        if isinstance(b,str) and b.isdigit() and len(b)==2 and int(b)<= 99:
            if isinstance(c, str) and c.isdigit() and len(c) == 3 and int(a) <= 255:
                if isinstance(d, str) and d.isdigit() and len(d) == 1 and int(d) <= 9:
                    print("Great this ip address is valid")
                    print('{}.{}.{}.{}'.format(a, b, c, d))
                else:
                    raise ValueError("This 4th octet is wrong ;please correct it")
            else:
                raise ValueError("This 3rd  octet is wrong ;please correct it")
        else:
            raise ValueError("This 2nd octet is wrong ;please correct it")
    else:
        raise ValueError("This 1st octet is wrong ;please correct it")


create_ip_address_4(a='172',b='16',c='254',d='1')