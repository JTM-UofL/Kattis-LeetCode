running_sum = 0
p1, p2 = 0,1
s : str = "MCMXCIVIXV"
length = len(str)

if length < 1: return 0

while(p1 < len(s) - 1):
    
    match s[p1]+s[p2]:
        case 'IV':
            print("FOUND! IV")
            p1 += 2
            p2 += 2
            running_sum += 4
        case 'IX':
            print("FOUND! IX")
            p1 += 2
            p2 += 2
            running_sum += 9
        case 'XL':
            print("FOUND! XL")
            p1 += 2
            p2 += 2
            running_sum += 40
        case 'XC':
            print("FOUND! XC")
            p1 += 2
            p2 += 2
            running_sum += 90
        case 'CD':
            print("FOUND! CD")
            p1 += 2
            p2 += 2
            running_sum += 400
        case 'CM':
            print("FOUND! CM")
            p1 += 2
            p2 += 2      
            running_sum += 900
        case _: 
          match p1:
              case 'I':
                  running_sum += 1
              case 'V':
                  running_sum += 5
              case "X":
                  running_sum += 10
              case "L":
                  running_sum += 50
              case "C":
                  running_sum += 100
              case "D": 
                  running_sum += 500
              case "M":
                  running_sum += 1000
          p1 += 1
          p2 += 1