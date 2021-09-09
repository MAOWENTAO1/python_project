def arithmetic_arranger(problems,tf=False):
  arranged_problems = ''
  error = None
  if len (problems) > 5:#rule1
    error = 'Error: Too many problems.'
  else:
    for i in problems:
      pieces = i.split(' ')
      try:#rule 3
        int(pieces[0])
        int(pieces[2])
      except:
        error = 'Error: Numbers must only contain digits.'
        break
      if (pieces[1] != '+') and (pieces[1] != '-'):#rule 2
        error = 'Error: Operator must be \'+\' or \'-\'.'
        break
      elif (len(pieces[0])>4 or len(pieces[2])>4):#rule 4
        error = 'Error: Numbers cannot be more than four digits.'
        break
  if error != None:
    arranged_problems = error
  else:
    numbers1 = []
    numbers2 = []
    operators = []
    results = []
    longs = []
    line1,line2,line3,line4='','','',''
    for i in problems:
      pieces = i.split(' ')
      #print(pieces)
      (number1,operator,number2)=(int(pieces[0]),pieces[1],int(pieces[2]))
      if operator == '+': result = number1 + number2
      else: result = number1 - number2
      numbers1.append(number1)
      numbers2.append(number2)
      operators.append(operator)
      results.append(result)
    for i in range(len(numbers1)):
      #print(numbers1[i])
      if len(str(numbers1[i]))<len(str(numbers2[i])):#upper is smaller than bottom
        longs.append(len(str(numbers2[i]))+2)
      else:
        longs.append(len(str(numbers1[i]))+2)
      if i == len(numbers1)-1:
        line1+=' '*(longs[i]-len(str(numbers1[i])))+str(numbers1[i])
        line2+=operators[i]+' '*(longs[i]-1-len(str(numbers2[i])))+str(numbers2[i])
        line3+='-'*longs[i]
        line4+=' '*(longs[i]-len(str(results[i])))+str(results[i])
      else:
        line1+=' '*(longs[i]-len(str(numbers1[i])))+str(numbers1[i])+' '*4
        line2+=operators[i]+' '*(longs[i]-1-len(str(numbers2[i])))+str(numbers2[i])+' '*4
        line3+='-'*longs[i]+' '*4
        line4+=' '*(longs[i]-len(str(results[i])))+str(results[i])+' '*4
    #print(line1)
    #print(line2)
    #print(line3)
    #print(line4)
    if tf == True:
      arranged_problems = '\n'.join((line1,line2,line3,line4))
    else:
      arranged_problems = '\n'.join((line1,line2,line3))
  return arranged_problems


