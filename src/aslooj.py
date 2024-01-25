import sys,os,time,re



def processor (line):
    if line.startswith(emojis[0]):
        params = line.strip()[1:].strip()
        for string in re.findall(r'(<(.*?)>)',params):
            params = params.replace(string[0], '"'+string[1]+'"')
        pycode = f'print({params})'
    elif line.startswith(emojis[1]):
        varname = line.strip()[1:].strip().split(' ')[0]
        params = ' '.join(line.strip()[1:].strip().split(' ')[1:])
        for string in re.findall(r'(<(.*?)>)',params):
            params = params.replace(string[0], '"'+string[1]+'"')
        pycode = f'{varname} = {params}'
    elif line.startswith(emojis[2]):
        varname = line.strip()[1:].strip().split(' ')[0]
        params = ' '.join(line.strip()[1:].strip().split(' ')[1:])
        for string in re.findall(r'(<(.*?)>)',params):
            params = params.replace(string[0], '"'+string[1]+'"')
        pycode = f'{varname} = input( {params} )'
    elif line.startswith(emojis[3]):
        varname = line.strip()[1:].strip().split(' ')[0]
        mathsign = line.strip()[1:].strip().split(' ')[1]
        num = line.strip()[1:].strip().split(' ')[2]
        try:    int(num)
        except: raise SyntaxError('Math Error : you should use a number')
        if not(mathsign in ['+','-','*','/','**','%']): raise SyntaxError('Math Error : use a real math sign')
        pycode = f'{varname} {mathsign}= {num}'
    elif line.startswith(emojis[4]):
        params = line.strip()[1:].strip().split(' ')
        pycode = ''
        for sec in params:
            try:    int(sec)
            except: raise SyntaxError('Sleep Error : you should use a number')
            pycode += f'time.sleep({sec})\n'
    elif line.startswith(emojis[5]):
        pycode = 'sys.exit("")'
    elif line.startswith(emojis[6]):
        params = line.strip()[1:].replace(' ','')
        for e,c in colors.items():
            params = params.replace(e,c)
        pycode = f'os.system("color {params}")'
    else:
        raise SyntaxError('Command Error : command not found')
    return pycode



def executor (pycode):
    try:
        exec(pycode,MEMORY)
    except Exception as e:
        raise SyntaxError('Executor Error : unknown error')


emojis = [ '🍭', '👽', '😭', '😼', '😴', '👹', '😺','🤖']
colors = {
    '⚫️':'0',
    '🔴':'4',
    '🟡':'6',
    '🟢':'a',
    '🔵':'1',
    '🟣':'5',
    '⚪️':'7'
}
MEMORY = {'sys':sys,'os':os,'time':time}

# from a file
if len(sys.argv) == 2:
    try:
        as_file = open(sys.argv[1],'r',encoding='utf-8')
    except:
        print('File Error : file not found')
        sys.exit('')
    context = as_file.read()
    as_file.close()
    lineno = 0
    func_head = ''
    func_body = []
    is_func = 0
    for line in context.split('\n'):
        for comment in re.findall(r'#.*',line):
            line = line.replace(comment,'').rstrip()
        lineno+=1
        
        if not( line.startswith('  ') or line.startswith('    ') or line.startswith('  ') or line.startswith('\t') ):
            if is_func:
                pycode = func_head
                for l in func_body:
                    pycode += '\n\t'+processor(l)
                executor(pycode)
                is_func=0
                func_body=[]
                func_head=''
        
        if line.strip() == '' : continue
        elif line.startswith(emojis[7]) and line.strip().endswith(':'):
            func_name = line.replace(emojis[7],'').replace(':','').strip()
            func_head = f'def {func_name} () :'
            is_func = 1
            continue
        elif line.startswith(emojis[7]) and not(line.strip().endswith(':')):
            line = line.replace(emojis[7],'').strip() + '()'
            try:
                executor(line)
            except Exception as e:
                os.system('color 4')
                print('Unknown Error :',str(e))
                print('Error is in line',lineno)
                sys.exit('')
            continue
        elif line.startswith('  ') or line.startswith('    ') or line.startswith('  ') or line.startswith('\t'):
            func_body.append( line.strip() )
            continue
        
        try:
            proc = processor(line)
            executor(proc)
        except Exception as e:
            os.system('color 4')
            print('Unknown Error :',str(e))
            print('Error is in line',lineno)
            sys.exit('')
else:
    print('ASLOOJ PROGRAMMING LANGUAGE\n')
    print('Usage:')
    print('     aslooj file.as\n')


input()