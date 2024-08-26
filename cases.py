def find_x(g, public_key, p):
    if public_key == 1:
        return 0  # since g^x mod p = 1 then x = 0 
    for x in range(1, p):
        if pow(g, x, p) == public_key:
            return x
    return None

def find_message(c1, c2, p, x):
    for message in range(0,1024):
        check =  ( (c1 ** (x)) * message ) %  p
        if check == c2:
            break
    
    if message != None:
        print("message = " + str(message))
        # print(check) 
    else: 
        print("message not found")
        return None

def find_message_case_4(c1, c2, p):
    for message in range(0,1024):
        check =  ( (c1 ) * message ) %  p
        if check == c2:
            break
    
    if message != None:
        print("message = " + str(message))
        # print(check) 
    else: 
        print("message not found")
        return None

def process_case(case_number):
    cases = {
        1: {
            'case_number': 1,
            'p': 23,
            'public_key': 21,
            'c1': 10,
            'generator': 5,
            'c2': 9
        },
        2: {
            'case_number': 2,
            'p': 95768907671470685161834890931411566592455689334949078397684923142851642341551,
            'public_key': 47884453835735342580917445465705783296227844667474539198842461571425821170776,
            'c1': 47884453835735342580917445465705783296227844667474539198842461571425821170776,
            'generator': 47884453835735342580917445465705783296227844667474539198842461571425821170776,
            'c2': 100
        },
        4: {
            'case_number': 4,
            'p': 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503753865831008441973494225499923250055784177410756159608183883985327442870672832045437787339365040606923860277363437139134990143853263608877373248332082093166171808999999,
            'public_key': 3058843465936720333571907537725961041445031134453247421217185542206828644502906784194608582991418620833696922836830311881252747881608871133767925544901090328582111139148688377491811122951242633999813074099087252076850494427651656770450334365948532267385429949222801830757731142576124548,
            'c1': 73330855740916146039866451341029067140760645910390429209230106550516911504466438328923058185249844928564599320433311362370624303450590310387520157712792451622437642898288798595482625546931933534370505271689851499772227787077899796419929447185618944933985625760186645614061067964804714315,
            'generator': 7,
            'c2': 23817611852541090570125290828834115548322095407545827778109272490358219512895580542655269250789752794176101844937408655750501617781279486874013125242032019811365018873416201884242522404612407005416448968588993784743249351647076271205671486963550181746045366582617470394981029601045001247
        },
        5: {
            'case_number': 5,
            'p': 95768907671470685161834890931411566592455689334949078397684923142851642341551,
            'public_key': 1,
            'c1': 47884453835735342580917445465705783296227844667474539198842461571425821170776,
            'generator': 47884453835735342580917445465705783296227844667474539198842461571425821170776,
            'c2': 720
        }
    }

    case = cases.get(case_number)
    if case is None:
        print("Invalid case number.")
        return

    case_number = case['case_number']
    p = case['p']
    public_key = case['public_key']
    c1 = case['c1']
    generator = case['generator']
    c2 = case['c2']
    
    if case_number == 4:
        find_message_case_4(c1=c1, c2=c2, p=p) 
    else:   
        x = find_x(g=generator, public_key=public_key, p=p)
        # print("x =", x)
        find_message(c1=c1, c2=c2, p=p, x=x)

    
    for j in range(0, 1024):
        check =  ( generator ** (j) ) %  p
        if check == c1:
            # print("y=" , end="")
            # print(check)
            break
    # else:
        # print("y not found")

# process_case(1)

number = input("Enter the Number of Scenario: ")
process_case(int(number))